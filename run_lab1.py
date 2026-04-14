from __future__ import annotations
import argparse
from pathlib import Path
import json
import datetime

from src.utils import set_seed
from src.load_data import load_dataset_any
from src.preprocess import basic_clean
from src.split import make_splits

from src.audit_core import (
    AuditConfig,
    audit_schema_missingness,
    audit_html_artifacts,
    audit_distribution_length,
    audit_duplicates,
    leakage_demo_tfidf,
    render_audit_md,
)

def ensure_datacard_templates(base_dir: Path = Path(".")) -> None:
    templates = {
        base_dir / "data_card.md": """# Data Card (copy từ Google Docs template)

Link Google Docs: ...

## Version
- v1.0 — ...
- v1.1 — ...

Dán nội dung Data Card bên dưới.
""",
        base_dir / "datacard" / "heuristics_scorecard.md": """# Heuristics Scorecard (Module 4)

- Completeness: __/5
- Accuracy: __/5
- Clarity: __/5
- Timeliness: __/5
- Actionability: __/5

Ghi chú:
""",
        base_dir / "datacard" / "metadata_register.md": """# Metadata Register — Verified / Estimated / To be measured

## Verified
- N, label counts, length stats: outputs/datacard_stats.json
- GE pass/fail: outputs/ge/validation_summary.md
- Cleanlab suspected issues: outputs/logs/cleanlab_summary.md

## Estimated
- ...

## To be measured
- ...
""",
    }
    for path, content in templates.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(content, encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default="imdb", choices=["imdb"])
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--max_rows", type=int, default=None)
    ap.add_argument("--use_great_expectations", action="store_true")
    ap.add_argument("--use_cleanlab", action="store_true")
    args = ap.parse_args()

    set_seed(args.seed)
    ensure_datacard_templates()

    out_dir = Path("outputs")
    (out_dir / "logs").mkdir(parents=True, exist_ok=True)
    (out_dir / "splits").mkdir(parents=True, exist_ok=True)

    df = load_dataset_any(args.dataset, max_rows=args.max_rows)
    df["text"] = df["text"].fillna("").astype(str)

    cfg = AuditConfig(seed=args.seed)

    sec_before = [
        ("Schema / Missingness", audit_schema_missingness(df)),
        ("HTML tags / Entities", audit_html_artifacts(df)),
        ("Distribution / Length", audit_distribution_length(df)),
        ("Duplicates / Near-duplicates", audit_duplicates(df, cfg)),
        ("Leakage demo (TF-IDF fit all vs train-only)", leakage_demo_tfidf(df, cfg)),
    ]
    render_audit_md(str(out_dir / "logs" / "audit_before.md"), "Audit BEFORE preprocessing", sec_before)

    df_clean = df.copy()
    df_clean["text"] = df_clean["text"].map(basic_clean)

    sec_after = [
        ("Schema / Missingness", audit_schema_missingness(df_clean)),
        ("HTML tags / Entities", audit_html_artifacts(df_clean)),
        ("Distribution / Length", audit_distribution_length(df_clean)),
        ("Duplicates / Near-duplicates", audit_duplicates(df_clean, cfg)),
        ("Leakage demo (TF-IDF fit all vs train-only)", leakage_demo_tfidf(df_clean, cfg)),
    ]
    render_audit_md(str(out_dir / "logs" / "audit_after.md"), "Audit AFTER preprocessing", sec_after)

    splits = make_splits(df_clean, seed=args.seed)
    for name, d in splits.items():
        d.to_csv(out_dir / "splits" / f"{name}.csv", index=False)

    ge_info = None
    if args.use_great_expectations:
        from src.ge_audit import run_great_expectations
        ge_info = run_great_expectations(df_clean[["id","text","label"]].copy(), out_dir / "ge")

    cl_info = None
    if args.use_cleanlab:
        from src.cleanlab_audit import run_cleanlab
        cv = 3 if args.max_rows else 5
        cl_info = run_cleanlab(df_clean[["id","text","label"]].copy(), out_dir / "logs", seed=args.seed, cv=cv)

    schema_stats = audit_schema_missingness(df_clean)
    dist_stats = audit_distribution_length(df_clean)
    dup_stats = audit_duplicates(df_clean, cfg)
    html_stats = audit_html_artifacts(df_clean)

    stats = {
        "dataset": args.dataset,
        "seed": args.seed,
        "max_rows": args.max_rows,
        "n_rows": schema_stats["n_rows"],
        "label_counts": schema_stats["label_counts"],
        "text_length": {k: dist_stats[k] for k in ["len_chars_min","len_chars_median","len_chars_p95","len_chars_max"]},
        "html_artifacts": html_stats,
        "duplicates": dup_stats,
        "splits": {k: int(len(v)) for k, v in splits.items()},
        "great_expectations": ge_info,
        "cleanlab": cl_info,
        "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
    }
    (out_dir / "datacard_stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")

    print("DONE.")

if __name__ == "__main__":
    main()
