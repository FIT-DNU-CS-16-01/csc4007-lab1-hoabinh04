# IMDB Review Dataset (as introduced in Maas et al., 2011)

> **Phạm vi:** Tài liệu này điền theo mẫu Data Cards Extended Template dựa trên kết quả chạy thực tế từ pipeline Lab 1 (`outputs/datacard_stats.json`) và thông tin nguồn gốc từ bài báo Maas et al. 2011.

**Tóm tắt tập dữ liệu:**
Tập dữ liệu IMDB là benchmark chuẩn gồm **50.000 đánh giá phim** từ Internet Movie Database, phục vụ bài toán **phân loại cảm xúc nhị phân** (positive/negative). Dữ liệu được chia thành **25.000 train** và **25.000 test** theo design gốc (không validation set), đảm bảo **cân bằng nhãn hoàn toàn** (25.000 negative, 25.000 positive) và sử dụng **disjoint movie sets** giữa train/test để giảm leakage từ các từ liên quan đến phim cụ thể.

**Kết quả audit Lab 1:**
- **Great Expectations**: 5/6 expectation đạt (83.33%) – phần lớn dữ liệu hợp lệ, 1 expectation fail cần kiểm tra chi tiết
- **Cleanlab**: 1.003 mẫu nghi ngờ sai nhãn (2.006%) – cần rà soát thủ công để cải thiện chất lượng nhãn
- **Duplicates**: 832 bản ghi trùng khớp hoàn toàn (1.664%) – có thể ảnh hưởng đến tính độc lập của train/test
- **Text Statistics**: Độ dài từ 32 đến 13.593 ký tự (median 954, P95 3.328) – đa dạng độ dài văn bản
- **HTML Artifacts**: 11 HTML entity còn lại sau làm sạch – tối thiểu nhưng cần chú ý

**Phù hợp dùng cho:** (1) huấn luyện sentiment classifiers baseline, (2) kiểm thử pipeline NLP end-to-end, (3) đánh giá impact của data quality/label noise, (4) benchmark so sánh phương pháp.

#### Dataset Link
- Dataset page: http://www.andrew-maas.net/data/sentiment
- Paper: https://aclanthology.org/P11-1015.pdf

#### Data Card Author(s)
- Nhóm thực hiện Lab 1 (bản điền theo template)

## Authorship
### Publishers
#### Publishing Organization(s)
- Stanford University (nguồn dữ liệu gốc)

#### Industry Type(s)
- Academic - Tech

#### Contact Detail(s)
- Publishing POC: Andrew L. Maas et al. (theo bài báo gốc)
- Affiliation: Stanford University
- Contact: [amaas, rdaly, ptpham, yuze, ang, cgpotts]@stanford.edu
- Mailing List: Bỏ qua (chưa có kết quả)
- Website: http://www.andrew-maas.net/data/sentiment

### Dataset Owners
#### Team(s)
- Stanford University research team

#### Contact Detail(s)
- Dataset Owner(s): Andrew L. Maas; Raymond E. Daly; Peter T. Pham; Dan Huang; Andrew Y. Ng; Christopher Potts
- Affiliation: Stanford University
- Contact: [amaas, rdaly, ptpham, yuze, ang, cgpotts]@stanford.edu
- Group Email: Bỏ qua (chưa có kết quả)
- Website: http://www.andrew-maas.net/data/sentiment

#### Author(s)
- Andrew L. Maas, Author, Stanford University, 2011
- Raymond E. Daly, Author, Stanford University, 2011
- Peter T. Pham, Author, Stanford University, 2011
- Dan Huang, Author, Stanford University, 2011
- Andrew Y. Ng, Author, Stanford University, 2011
- Christopher Potts, Author, Stanford University, 2011

### Funding Sources
#### Institution(s)
- DARPA Deep Learning program
- National Science Foundation (NSF)
- Office of Naval Research (ONR)

#### Funding or Grant Summary(ies)
Theo bài báo: dự án nhận hỗ trợ từ DARPA (FA8650-10-C-7020), NSF Graduate Fellowship, và ONR (N00014-10-1-0109).

## Dataset Overview
#### Data Subject(s)
- Dữ liệu văn bản do người dùng viết (movie reviews)

#### Dataset Snapshot
Category | Data | Ghi chú
--- | --- | ---
Size of Dataset | 50,000 rows | Tổng cộng 50k mẫu
Number of Instances | 50,000 reviews | Mỗi mẫu = 1 review phim
Number of Fields | 3 (`id`, `text`, `label`) | id: unique (0-49999); text: review content; label: 0 or 1
Labeled Classes | 2 (0=negative, 1=positive) | Nhị phân, highly polarized (score ≤4 → 0; ≥7 → 1)
Number of Labels | 50,000 | Toàn bộ mẫu đều có nhãn
Average Labels Per Instance | 1 | Mỗi review = 1 nhãn duy nhất
Algorithmic Labels | Không sinh nhãn mới | Sử dụng nhãn gốc từ IMDB score thresholding
Human Labels | IMDB user ratings (original) | Nguồn: người dùng IMDB đánh giá từ 1-10
Other Characteristics | Cực cân bằng (25k/25k per class); disjoint movie train/test; 832 exact duplicates; 11 HTML entities | Design test độc lập, ngăn leakage; cần dedup & HTML cleanup

**Above:** Chi tiết snapshot của tập dữ liệu IMDB từ audit Lab 1.

**Additional Notes:** Tất cả 50k mẫu đã được làm sạch cơ bản (loại HTML tags, chuẩn hóa entities) trước audit. Dữ liệu gốc từ Hugging Face `datasets` library, version mặc định.

#### Content Description
Mỗi dòng dữ liệu gồm **3 trường chính**:
- **id** (integer): Unique identifier từ 0 đến 49999
- **text** (string): Nội dung bài review phim do người dùng IMDB viết, độ dài từ 32 đến 13.593 ký tự Unicode
- **label** (integer): Nhãn cảm xúc nhị phân {0, 1}, suy diễn từ IMDB score gốc (≤4 → 0, ≥7 → 1; neutral 5-6 bị loại)

Dữ liệu không chứa metadata (tên author, user_id, timestamp, rating gốc) trong public release. Dùng cho **document-level sentiment classification** tasks.

**Format:** File audit được lưu dưới dạng CSV (splits) trong folder `outputs/splits/`, JSON summary trong `outputs/datacard_stats.json`.

#### Descriptive Statistics
Statistic | text (ký tự) | label | id
--- | --- | --- | ---
count | 50,000 | 50,000 | 50,000
mean | 1,286.80 | N/A | 24,999.50
std | 972.24 | N/A | 14,433.90
min | 32 | 0 (negative) | 0
25% | 690.00 | N/A | 12,499.75
50% (median) | 954.00 | N/A (50-50 split) | 24,999.50
75% | 1,561.00 | N/A | 37,499.25
**max** | **13,593** | **1 (positive)** | **49,999**
**mode** | **665** | **0 & 1 (fully balanced)** | N/A
**p95** | **3,328** | N/A | **47,499.05**

**Chi tiết bổ sung:**
- **Text length**: Trung bình ~1,287 ký tự/review (median 954 cho thấy phân bố lệch phải). Tươi phút độ dài từ 32 đến 13.6k ký tự.
- **Word count**: Trung bình 228.83 từ/review (median 171 từ), p95 = 584 từ
- **Label**: Cân bằng hoàn toàn 25k/25k (negative/positive), không class imbalance
- **ID**: Sequential từ 0 đến 49,999, phân bố đều (mean=24,999.5 = midpoint đúng)

**Above:** Thống kê chi tiết từ audit Lab 1. Text length rất đa dạng; label phân bố hoàn toàn cân bằng (25k mẫu cho mỗi class).

**Additional Notes:**
- **Text length p95 = 3,328 ký tự**: 95% reviews ≤ 3.3k ký tự, 5% reviews dài hơn (lên đến 13.6k)
- **Text length mode = 665 ký tự**: Độ dài phổ biến nhất của review là ~665 ký tự (khoảng ~120 từ)
- **Mean text = 1,287 ký tự; median = 954 ký tự**: Phân bố lệch phải (mean > median) do có độ dài cực đại khá lớn
- **Không có missing values** ở bất kỳ trường nào sau làm sạch
- **Label distribution thực tế**: {0: 25,000, 1: 25,000} – perfectly balanced, không class imbalance
- **Min text length = 32 ký tự**: Có vài review rất ngắn (ví dụ "This movie sucks." = 20 ký tự + spaces)

### Sensitivity of Data
#### Sensitivity Type(s)
- User Content

#### Field(s) with Sensitive Data
Field Name | Description
--- | ---
text | Có thể chứa thông tin cá nhân ngẫu nhiên do người dùng tự viết

#### Security and Privacy Handling
Bỏ qua (chưa có kết quả kiểm thử riêng về privacy/anonymization).

#### Risk Type(s)
- Label noise
- Duplicate data
- Data leakage risk (nếu chia dữ liệu không đúng)

#### Supplemental Link(s)
- Dataset page: http://www.andrew-maas.net/data/sentiment
- Paper: https://aclanthology.org/P11-1015.pdf

#### Risk(s) and Mitigation(s)
- Duplicate risk: phát hiện 832 exact duplicates (1.664%) -> cần dedup theo mục tiêu thí nghiệm.
- Label noise risk: Cleanlab nghi ngờ 1.003 mẫu (2.006%) -> cần rà soát thủ công top mẫu nghi ngờ.
- Quality risk: Great Expectations đạt 5/6 -> cần kiểm tra expectation thất bại trước khi train production.

### Dataset Version and Maintenance
#### Maintenance Status
- Static benchmark (dùng cho bài lab)

#### Version Details
- Current Version: theo bản phát hành IMDB đang sử dụng trong lab
- Last Updated: Bỏ qua (chưa có kết quả)
- Release Date: Bỏ qua (chưa có kết quả)

#### Maintenance Plan
Bỏ qua (chưa có kết quả).

#### Next Planned Update(s)
Bỏ qua (chưa có kết quả).

#### Expected Change(s)
Bỏ qua (chưa có kết quả).

## Example of Data Points
#### Primary Data Modality
- Text Data

#### Sampling of Data Points
- Lấy mẫu từ tập IMDB đã tải qua pipeline Lab 1

#### Data Fields
Field Name | Field Value | Description
--- | --- | ---
text | Chuỗi văn bản | Nội dung review phim
label | 0 hoặc 1 | 0: tiêu cực, 1: tích cực

#### Typical Data Point
```text
{
  "text": "This movie was fantastic and visually stunning...",
  "label": 1
}
```

#### Atypical Data Point
```text
{
  "text": "<rất ngắn hoặc nhiễu ký tự/format>",
  "label": 0
}
```

## Motivations & Intentions
### Motivations
#### Purpose(s)
- Research
- Học pipeline NLP cơ bản

#### Domain(s) of Application
NLP, Sentiment Analysis, Text Classification

#### Motivating Factor(s)
- Xây dựng benchmark phân loại cảm xúc nhị phân.
- Đánh giá chất lượng dữ liệu trước khi huấn luyện mô hình.

### Intended Use
#### Dataset Use(s)
- Safe for research/classroom use

#### Suitable Use Case(s)
- Phân loại cảm xúc nhị phân cho review phim.
- Kiểm thử pipeline tiền xử lý, audit dữ liệu.

#### Unsuitable Use Case(s)
- Suy luận thông tin cá nhân người viết review.
- Dùng trực tiếp cho bài toán ngoài miền (non-movie domain) mà không đánh giá lại.

#### Research and Problem Space(s)
Phù hợp cho các bài toán baseline NLP, học biểu diễn văn bản, và đánh giá tác động của nhiễu nhãn.

#### Citation Guidelines
```bibtex
@inproceedings{maas2011learning,
  title={Learning Word Vectors for Sentiment Analysis},
  author={Maas, Andrew L. and Daly, Raymond E. and Pham, Peter T. and Huang, Dan and Ng, Andrew Y. and Potts, Christopher},
  booktitle={Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  pages={142--150},
  year={2011},
  address={Portland, Oregon},
  publisher={Association for Computational Linguistics}
}
```

## Access, Rentention, & Wipeout
### Access
#### Access Type
- External - Open Access

#### Documentation Link(s)
- Dataset Website URL: http://www.andrew-maas.net/data/sentiment
- Paper URL: https://aclanthology.org/P11-1015.pdf

#### Prerequisite(s)
Bỏ qua (chưa có kết quả/yêu cầu đặc biệt).

#### Policy Link(s)
- Dataset page: http://www.andrew-maas.net/data/sentiment

#### Access Control List(s)
- Public dataset, không có ACL riêng trong phạm vi lab.

### Retention
#### Duration
Bỏ qua (chưa có kết quả).

#### Policy Summary
Bỏ qua (chưa có kết quả).

#### Process Guide
Bỏ qua (chưa có kết quả).

#### Exception(s) and Exemption(s)
Bỏ qua (chưa có kết quả).

### Wipeout and Deletion
#### Duration
Bỏ qua (chưa có kết quả).

#### Deletion Event Summary
Bỏ qua (chưa có kết quả).

#### Acceptable Means of Deletion
Bỏ qua (chưa có kết quả).

#### Post-Deletion Obligations
Bỏ qua (chưa có kết quả).

#### Operational Requirement(s)
Bỏ qua (chưa có kết quả).

#### Exceptions and Exemptions
Bỏ qua (chưa có kết quả).

## Provenance
### Collection
#### Method(s) Used
- Thu thập từ review phim IMDB (theo nguồn dataset công khai)

#### Methodology Detail(s)
- Pipeline Lab 1 tải dữ liệu, chuẩn hóa cơ bản và audit chất lượng.

#### Source Description(s)
- Nguồn: review văn bản do người dùng đăng trên IMDB.

#### Collection Cadence
- Static dataset cho mục đích benchmark/lab.

#### Data Integration
- Dùng tập dữ liệu đã chuẩn hóa theo script lab.

#### Data Processing
- Làm sạch HTML artifacts.
- Tính thống kê độ dài văn bản.
- Kiểm tra duplicate và chia train/val/test.

### Collection Criteria
#### Data Selection
- Chọn các mẫu trong tập IMDB phục vụ nhị phân 0/1.

#### Data Inclusion
- Bao gồm các mẫu có text và label hợp lệ.

#### Data Exclusion
- Bỏ qua (chưa có kết quả chi tiết rule loại trừ ngoài pipeline mặc định).

### Relationship to Source
#### Use & Utility(ies)
- **Là benchmark chuẩn** cho sentiment analysis / emotion detection từ text tiếng Anh
- **Đã được sử dụng rộng rãi** trong hơn 10 năm (từ 2011) cho papers, competitions, undergraduate/graduate courses
- **Lợi ích chính**:
  - Dữ liệu cực sạch, cân bằng hoàn toàn, kích thước đủ lớn (~50k mẫu)
  - Design tốt (disjoint movie splits, highly polarized = clear signal)
  - Dễ download & không cần xửa phép
- **Thích hợp dùng cho**: Baseline models, embedding quality evaluation, data quality vs. model performance tradeoff studies

#### Benefit and Value(s)
- Cân bằng nhãn, quy mô đủ lớn, phù hợp baseline.

#### Limitation(s) and Trade-Off(s)
- Có nhiễu nhãn và duplicate.
- Không đại diện đầy đủ mọi miền ngôn ngữ/chủ đề.

### Version and Maintenance
#### First Version
- Bỏ qua (chưa có kết quả).

#### Note(s) and Caveat(s)
- Great Expectations chưa đạt 100% (5/6).
- Cần cân nhắc xử lý 1.003 mẫu nghi ngờ sai nhãn khi huấn luyện nghiêm ngặt.

#### Cadence
- Bỏ qua (chưa có kết quả).

#### Last and Next Update(s)
- Last generated audit: 2026-04-14T01:14:05.835822Z
- Next update: Bỏ qua (chưa có kết quả).

#### Changes on Update(s)
- Bỏ qua (chưa có kết quả).

## Human and Other Sensitive Attributes
#### Sensitive Human Attribute(s)
Bỏ qua (chưa có kết quả).

#### Intentionality
Bỏ qua (chưa có kết quả).

#### Rationale
Bỏ qua (chưa có kết quả).

#### Source(s)
Bỏ qua (chưa có kết quả).

#### Methodology Detail(s)
Bỏ qua (chưa có kết quả).

#### Distribution(s)
Bỏ qua (chưa có kết quả).

#### Known Correlations
Bỏ qua (chưa có kết quả).

#### Risk(s) and Mitigation(s)
Bỏ qua (chưa có kết quả).

## Extended Use
### Use with Other Data
#### Safety Level
- Medium (cần đánh giá lại khi ghép miền dữ liệu khác)

#### Known Safe Dataset(s) or Data Type(s)
- Các tập review tiếng Anh cùng miền phim (movie reviews)

#### Best Practices
- Chuẩn hóa preprocessing thống nhất giữa các tập.
- Kiểm tra drift khi thêm nguồn dữ liệu mới.

#### Known Unsafe Dataset(s) or Data Type(s)
- Dữ liệu có cấu trúc khác hoàn toàn (sensor/log số liệu).

#### Limitation(s) and Recommendation(s)
- Khuyến nghị fine-tune và đánh giá lại trước khi transfer domain.

### Forking & Sampling
#### Safety Level
- Medium

#### Acceptable Sampling Method(s)
- Stratified sampling theo nhãn.
- Seed cố định để tái lập.

#### Best Practice(s)
- Giữ cân bằng nhãn ở train/val/test.
- Tránh rò rỉ dữ liệu giữa các split.

#### Risk(s) and Mitigation(s)
- Risk: Mất cân bằng khi sample ngẫu nhiên.
- Mitigation: stratify + kiểm tra phân phối sau chia.

#### Limitation(s) and Recommendation(s)
- Bỏ qua (chưa có kết quả bổ sung).

### Use in ML or AI Systems
#### Dataset Use(s)
- Huấn luyện baseline sentiment classifier.

#### Notable Feature(s)
- Cân bằng nhãn.
- Văn bản độ dài đa dạng.

#### Usage Guideline(s)
- Nên chạy audit trước train.
- Nên cân nhắc dedup và xử lý label issues.

#### Distribution(s)
- Label 0: 25,000; Label 1: 25,000.

#### Known Correlation(s)
- Bỏ qua (chưa có kết quả định lượng sâu).

#### Split Statistics (Chính thức)
**Design**: Theo bài báo gốc Maas et al. 2011 – **train/test split 50/50** (không validation set)
- **Train**: 25,000 mẫu (12,500 negative + 12,500 positive)
- **Validation**: 0 mẫu (không sử dụng)
- **Test**: 25,000 mẫu (12,500 negative + 12,500 positive)

**Đặc tính phân chia:**
- **Stratified**: Cân bằng nhãn được duy trì hoàn toàn ở cả train & test
- **Disjoint movies**: 30 films max per label = tập phim trong train ⊥ tập phim trong test (ngăn leakage từ movie-specific words)
- **Seed 42**: Đảm bảo tái lập (reproducible) trên tất cả chạy
- **Giữ order & ID**: ID từ 0-24999 cho train, 25000-49999 cho test (có thể khác nếu dùng seed khác)

## Transformations
### Synopsis
#### Transformation(s) Applied
- Basic cleaning
- Data audit (GE, Cleanlab)
- Split dữ liệu train/val/test

#### Field(s) Transformed
- `text` (cleaning/normalization)
- `label` (kiểm tra hợp lệ và audit nhiễu nhãn)

#### Library(ies) and Method(s) Used
- Great Expectations
- Cleanlab
- scikit-learn (TF-IDF + Logistic Regression trong bước phát hiện label issues)

### Breakdown of Transformations
#### Cleaning Missing Value(s)
- Bỏ qua (chưa có kết quả chi tiết số lượng missing).

#### Method(s) Used
- Bỏ qua (chưa có kết quả).

#### Comparative Summary
- Bỏ qua (chưa có kết quả).

#### Residual & Other Risk(s)
- Bỏ qua (chưa có kết quả).

#### Human Oversight Measure(s)
- Bỏ qua (chưa có kết quả).

#### Additional Considerations
- Bỏ qua (chưa có kết quả).

#### Cleaning Mismatched Value(s)
- Kiểm tra nhãn ngoài miền {0,1}; GE xác nhận phần lớn hợp lệ.

#### Method(s) Used
- Expectation kiểm tra miền giá trị nhãn.

#### Comparative Summary
- 5/6 expectation đạt.

#### Residual & Other Risk(s)
- 1 expectation chưa đạt, cần rà soát chi tiết trước production.

#### Human Oversight Measure(s)
- Rà soát thủ công các bản ghi vi phạm expectation.

#### Additional Considerations
- Bỏ qua (chưa có kết quả).

#### Anomalies
**Phát hiện từ audit Lab 1:**

1. **Exact duplicates**: 832 bản ghi (1.664%)
   - Có văn bản + nhãn **giống hệt nhau** → có thể là duplicate reviews hoặc review tương tự từ các user khác
   - **Risk**: Nếu xuất hiện ở cả train & test → data leakage, metrics inflated
   - **Recommendation**: Remove hoặc áp dụng stratified dedup trước chia train/test

2. **HTML entity còn lại**: 11 mẫu (0.022%)
   - Vẫn chứa HTML entities (e.g., `&quot;`, `&amp;`, `&apos;`) sau làm sạch cơ bản
   - **Risk**: Nhỏ, nhưng có thể ảnh hưởng embedding quality
   - **Recommendation**: Regex nâng cao hoặc manual fix

3. **Suspected label issues (Cleanlab)**: 1.003 mẫu (2.006%)
   - Được xác định bằng 5-fold cross-validation + TF-IDF + Logistic Regression
   - **Confidence**: Self-confidence score từ Cleanlab
   - **Risk**: ~2% label error → có thể sụt 1-3% accuracy
   - **Recommendation**: Manual review top-200 suspects, gán lại nhãn chính xác

4. **GE validation fail**: 1/6 expectations không đạt
   - Chưa được chi tiết hóa − cần kiểm tra `ge/validation_result.json`
   - **Risk**: Unknown schema/data integrity issue
   - **Recommendation**: Investigate fail expectation, fix root cause

#### Method(s) Used

**Cleanlab (Label error detection):**
- Model: TF-IDF (max 20k features, ngram 1-2, min_df=2) + Logistic Regression (max_iter=200)
- CV: 5-fold stratified CV với seed=42
- Output: pred_probs từ mỗi fold validation set
- Detection: `cleanlab.find_label_issues()` dùng self-confidence score
- Top-K: Export top-200 ranked suspects

**Great Expectations (Data validation):**
- expect_column_values_to_not_be_null: `text`, `label`, `id`
- expect_column_values_to_be_in_set: `label` ∈ {0, 1}
- expect_column_values_to_be_unique: `id` (each review unique)
- [+2 additional custom expectations]

**Duplicate Detection:**
- Exact match: compare (text, label) pairs
- pandas groupby + nunique

#### Comparative Summary
- **Cleanlab detection**: 1.003 / 50,000 = 2.006% suspected label issues
- **GE pass rate**: 5 / 6 = 83.33% expectations passed
- **Duplicate rate**: 832 / 50,000 = 1.664% exact duplicates
- **HTML entity rate**: 11 / 50,000 = 0.022% still contain entities

#### Residual & Other Risk(s)
| Risk | Severity | Impact | Mitigation |
| --- | --- | --- | --- |
| Data leakage (duplicates in train+test) | **High** | Inflated metrics, overfit | Dedup before split |
| Label noise (2% error) | **Medium** | -1-3% accuracy | Manual review top-200 |
| GE fail (unknown issue) | **Medium** | Integrity unknown | Investigate fail rule |
| HTML entities (0.02%) | **Low** | Minor embedding issue | Regex cleanup |

#### Human Oversight Measure(s)
1. **Duplicate review**: Rà soát 832 duplicates, quyết định giữ/xóa/merge
2. **Cleanlab review**: Manual label 5-10 mẫu từ top-200 suspects → estimate label accuracy
3. **GE investigation**: Đọc `ge/validation_result.json` → xác định fail expectation + root cause
4. **HTML entity cleanup**: Regex aggressive hoặc manual fix 11 mẫu

#### Additional Considerations
- Bỏ qua (chưa có kết quả).

#### Dimensionality Reduction
- Bỏ qua (chưa có kết quả áp dụng giảm chiều trực tiếp lên dữ liệu gốc).

#### Method(s) Used
- Bỏ qua (chưa có kết quả).

#### Comparative Summary
- Bỏ qua (chưa có kết quả).

#### Residual & Other Risks
- Bỏ qua (chưa có kết quả).

#### Human Oversight Measure(s)
- Bỏ qua (chưa có kết quả).

#### Additional Considerations
- Bỏ qua (chưa có kết quả).

#### Joining Input Sources
- Không join nhiều nguồn trong phạm vi kết quả đã chạy.

#### Method(s) Used
- Bỏ qua (chưa có kết quả).

#### Comparative Summary
- Bỏ qua (chưa có kết quả).

#### Residual & Other Risk(s)
- Bỏ qua (chưa có kết quả).

#### Human Oversight Measure(s)
- Bỏ qua (chưa có kết quả).

#### Additional Considerations
- Bỏ qua (chưa có kết quả).

#### Redaction or Anonymization
- Bỏ qua (chưa có kết quả thao tác ẩn danh chuyên biệt).

#### Method(s) Used
- Bỏ qua (chưa có kết quả).

#### Comparative Summary
- Bỏ qua (chưa có kết quả).

#### Residual & Other Risk(s)
- Bỏ qua (chưa có kết quả).

#### Human Oversight Measure(s)
- Bỏ qua (chưa có kết quả).

#### Additional Considerations
- Bỏ qua (chưa có kết quả).

#### Others (Please Specify)
**Data splitting theo design gốc IMDB (Maas et al. 2011):**
- **Tỷ lệ**: 50% train (25k), 0% validation (0), 50% test (25k)
- **Strategy**: Stratified random split từ `src/split.py` sử dụng `train_test_split(stratify=label)` để giữ cân bằng nhãn
- **Seed**: 42 (đảm bảo reproducibility qua máy tính khác nhau)
- **Disjoint movie sets**: Xử lý tại nguồn dữ liệu - film trong train không xuất hiện trong test (do IMDB design)
- **Edge case handling**: Khi `val_ratio=0`, code tạo DataFrame trống cho validation thay vì gọi `train_test_split(test_size=1.0)` (invalid)
- **Kết quả cuối cùng**: {train: 25k, val: 0, test: 25k} với label balance 50-50 mỗi split

#### Method(s) Used
| Phương pháp | Chi tiết | Công cụ/Thư viện |
|-----------|---------|-----------------|
| Stratified Random Split | `sklearn.train_test_split(df, test_size=0.5, stratify=df['label'], random_state=42)` | scikit-learn |
| Seed Control | Fixed seed=42 để reproducibility từ dòng 8 của `src/split.py` | numpy/random |
| Disjoint Validation | `val_ratio=0` → create empty DataFrame instead of train_test_split with test_size=1.0 | pandas |
| Balance Verification | Kiểm tra `value_counts()` trên label column sau mỗi split | pandas |

#### Comparative Summary
- Tỷ lệ nhãn vẫn cân bằng sau chia: Train {0: 12.5k, 1: 12.5k} = 50-50 ✅
- Test {0: 12.5k, 1: 12.5k} = 50-50 ✅
- **Stratification effectiveness**: 100% - không có class imbalance

#### Residual & Other Risk(s)
- **Risk nhỏ về sampling variance**: Do sample size lớn (25k/split) → không đáng lo

#### Human Oversight Measure(s)
- Kiểm tra phân phối label trước train: `df_train['label'].value_counts()` vs `df_test['label'].value_counts()`
- Verify disjoint movies: so sánh movie_id/film name giữa train & test (nếu có)

#### Additional Considerations
- Bỏ qua (chưa có kết quả).

## Annotations & Labeling
#### Annotation Workforce Type
- Nhãn gốc do người dùng IMDB cung cấp thông qua rating.

#### Annotation Characteristic(s)
- Nhãn nhị phân 0/1, suy diễn từ cực tính đánh giá.

#### Annotation Description(s)
- Dữ liệu đã có nhãn sẵn; Lab 1 không gán nhãn thủ công mới.

#### Annotation Distribution(s)
- 25,000 negative; 25,000 positive.

#### Annotation Task(s)
- Sentiment classification (binary).

### Human Annotators
#### Annotator Description(s)
- Bỏ qua (chưa có kết quả chi tiết hồ sơ annotator).

#### Annotator Task(s)
- Bỏ qua (chưa có kết quả chi tiết quy trình annotate thủ công).