import json
from pathlib import Path

# Simulated raw incoming scan batch (notice P002 has bad spacing and P003 is missing 'modality')
raw_batch = [
    {"patient_id": "P001", "modality": "X-RAY", "width_px": 2048, "pixel_spacing_mm": 0.15},
    {"patient_id": "P002", "modality": "CT", "width_px": 512, "pixel_spacing_mm": -0.50},
    {"patient_id": "P003", "width_px": 512, "pixel_spacing_mm": 0.70},
    {"patient_id": "P004", "modality": "MRI", "width_px": 256, "pixel_spacing_mm": 0.80},
    {"patient_id": "P005", "modality": "CT", "width_px": "Test", "pixel_spacing_mm": 0.55},
]


def validate_and_process(batch: list[dict]) -> tuple[list[dict], list[dict]]:
    """Separates valid scans from corrupted records without crashing the pipeline."""
    valid_scans = []
    rejected_scans = []

    for record in batch:
        try:
            patient_id = record["patient_id"]
            modality = record["modality"]  # Raises KeyError if missing
            spacing = float(record["pixel_spacing_mm"])
            width = int(record["width_px"])

            if spacing <= 0 or width <= 0:
                raise ValueError("Pixel dimensions and spacing must be positive.")

            record["physical_width_cm"] = round((width * spacing) / 10, 2)
            valid_scans.append(record)

        except (KeyError, ValueError, TypeError) as error:
            rejected_scans.append({
                "patient_id": record.get("patient_id", "UNKNOWN"),
                "reason": str(error),
            })

    return valid_scans, rejected_scans


def save_report(data: list[dict], filename: str) -> None:
    """Saves structured scan results to a JSON file inside the Week 1 folder."""
    output_path = Path(__file__).parent / filename
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"Saved {len(data)} records to {output_path.name}")


if __name__ == "__main__":
    valid, rejected = validate_and_process(raw_batch)
    save_report(valid, "valid_scans.json")
    save_report(rejected, "rejected_scans.json")

    valid_ids = [scan["patient_id"] for scan in valid]
    print(f"Ready for AI model: {valid_ids}")