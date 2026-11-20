#creating a list with pations
scans = [
    {
        "patient_id": "P001",
        "modality": "X-RAY",
        "body_part": "Chest",
        "width_px": 2048,
        "height_px": 2048,
        "pixel_spacing_mm": 0.15,
        "urgent": True,
    },
    {
        "patient_id": "P002",
        "modality": "MRI",
        "body_part": "Brain",
        "width_px": 512,
        "height_px": 512,
        "pixel_spacing_mm": 0.50,
        "urgent": False,
    },
    {
        "patient_id": "P003",
        "modality": "CT",
        "body_part": "Lung",
        "width_px": 512,
        "height_px": 512,
        "pixel_spacing_mm": 0.70,
        "urgent": True,
    },
    {
        "patient_id" : "P004",
        "modality" : "CT",
        "body_part": "Head",
        "width_px": 512,
        "height_px": 512,
        "pixel_spacing_mm": 0.65,
        "urgent": False,
    }
]


def calculate_physical_size_cm(width_px: int, height_px: int, spacing_mm: float) -> tuple[float, float]:
    """Converts pixel dimensions into real-world centimeters using pixel spacing."""
    width_cm = (width_px * spacing_mm) / 10
    height_cm = (height_px * spacing_mm) / 10
    return round(width_cm, 2), round(height_cm, 2)


def triage_scans(scan_list: list[dict]) -> None:
    """Prints scan summary and flags urgent cases for priority AI inference."""
    print(f"Total scans in queue: {len(scan_list)}\n")

    for scan in scan_list:
        w_cm, h_cm = calculate_physical_size_cm(
            scan["width_px"], scan["height_px"], scan["pixel_spacing_mm"]
        )
        priority = "HIGH PRIORITY" if scan["urgent"] else "Routine"
        print(
            f"[{priority}] {scan['patient_id']} | {scan['modality']} ({scan['body_part']}) "
            f"- Physical Size: {w_cm} cm x {h_cm} cm"
        )

def count_by_modality(scan_list: list[dict], modality_type: str) -> int:
    count = 0
    for scan in scan_list:
        if scan["modality"].lower() == modality_type.lower():
            count += 1
    return count


if __name__ == "__main__":
    triage_scans(scans)
    ct_total = count_by_modality(scans, "CT")
    print(f"\nTotal CT scans in queue: {ct_total}")