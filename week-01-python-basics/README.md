# Week 1: Python Basics for Medical Imaging Metadata

## Objective
Simulate how radiology scan metadata (modality, pixel resolution, physical spacing, and contrast usage) is structured, validated, and filtered in Python before being passed into a medical imaging AI pipeline.

## Scripts
- `patient_basics.py`: Stores simulated X-ray, CT, and MRI patient records, converts pixel dimensions into physical centimeters using pixel spacing, flags high-priority scans, and counts scans by imaging modality.
- `dicom_filter.py`: Evaluates scan dimensions against a minimum pixel threshold (`512x512`) using modular helper functions (`is_high_res` and `filter_scans`) and returns a summary of accepted patient IDs, rejected scan counts, and contrast-enhanced scans.

## Key Concepts Practiced
- Structuring metadata with nested lists, dictionaries, and tuples
- Tuple unpacking and type annotations (`list[dict]`, `-> bool`, `-> dict`)
- Modular function design and conditional filtering logic
- Dictionary iteration using `.items()` for formatted terminal reporting

## Usage
Run either script from the root of the repository:

```bash
python week-01-python-basics/patient_basics.py
python week-01-python-basics/dicom_filter.py