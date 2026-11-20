#Patient records to test code on them
scans = [
    {"patient_id": "P101", "modality": "X-RAY", "resolution": (2048, 2048), "contrast_used": False},
    {"patient_id": "P102", "modality": "CT", "resolution": (512, 512), "contrast_used": True},
    {"patient_id": "P103", "modality": "MRI", "resolution": (256, 256), "contrast_used": True},
    {"patient_id": "P104", "modality": "CT", "resolution": (1024, 512), "contrast_used": False},
    {"patient_id": "P105", "modality": "X-RAY", "resolution": (512, 256), "contrast_used": False},
    {"patient_id": "P106", "modality": "MRI", "resolution": (1024, 1024), "contrast_used": True},
]

def is_high_res(scan: dict, min_pixels: int = 512) -> bool:
    width_res, height_res = scan["resolution"]
    if(width_res >= min_pixels and height_res >= min_pixels):
        return True
    else:
        return False

def filter_scans(scans: list[dict]) -> dict:
    accepted_ids = []
    rejected_amount = 0
    contrast_scans = 0
    for i in scans:
        if is_high_res(i):
            accepted_ids.append(i["patient_id"])
            if i["contrast_used"] is True:
                contrast_scans += 1
        else:
            rejected_amount += 1

    return {
        "accepted_ids" : accepted_ids,
        "rejected_amount" : rejected_amount,
        "contrast_scans" : contrast_scans,
    }

print (filter_scans(scans))
