# Week 2: Medical Image Arrays & Clinical Data Cleaning

## Scripts
- `image_preprocessing.py`: Simulates a 12-bit grayscale X-ray slice using NumPy, computes pixel intensity statistics (`analyze_scan`), scales intensities to `[0.0, 1.0]` via Min-Max normalization (`normalize_image`), and extracts a centered Region of Interest (`crop_center`).
- `cohort_cleaning.py`: Cleans a raw clinical metadata DataFrame using Pandas (`clean_cohort`) by dropping unlabeled diagnoses, standardizing scan modality strings, replacing invalid ages with median imputation, imputing missing confidence scores with the mean, and filtering for high-confidence records (`>= 0.85`).

## Key Concepts Practiced
- Vectorized array operations and broadcasting in NumPy (`dtype=np.float32`, Min-Max scaling)
- 2D NumPy array indexing and centered ROI slicing
- Tabular clinical data cleaning in Pandas (`.dropna()`, `.str` methods, `.loc[]` conditional assignment, `.fillna()`)
- Boolean DataFrame filtering and class balance inspection using `.value_counts()`

## Usage
Run either script from the root of the repository:

```bash
python week-02-numpy-pandas/image_preprocessing.py
python week-02-numpy-pandas/cohort_cleaning.py