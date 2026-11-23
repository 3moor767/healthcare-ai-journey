import pandas as pd
import numpy as np

raw_cohort = {
    "patient_id": ["P001", "P002", "P003", "P004", "P005", "P006", "P007"],
    "age": [64, 45, np.nan, 72, -5, 58, 51],
    "modality": ["xray", "CT", "mri", "X-RAY", "ct", "MRI", "xray"],
    "diagnosis": ["Pneumonia", "Normal", "Tumor", np.nan, "Normal", "Normal", "Pneumonia"],
    "confidence_score": [0.92, 0.88, 0.95, 0.79, 0.84, np.nan, 0.91],
}

df = pd.DataFrame(raw_cohort)

def clean_cohort(df: pd.DataFrame) -> pd.DataFrame:
    #remove all na from diagnosis
    df = df.dropna(subset=["diagnosis"]).copy()

    #Standrising the modality to make all upper case, and change XRAY TO X-RAY
    df["modality"] = df["modality"].str.upper().str.replace("XRAY","X-RAY")

    #removing all invalid ages with nan and filling missing ages with the median
    df.loc[df["age"] <= 0, "age"] = np.nan
    df["age"] = df["age"].fillna(df["age"].median())

    #filling missing confidence_score score with the mean
    df["confidence_score"] = df["confidence_score"].fillna(df["confidence_score"].mean())

    #filtering the table where confidence_score >= 0.85
    df = df[df["confidence_score"] >= 0.85]

    return df


print("--- RAW DATA ---")
print(df)

cleaned_df = clean_cohort(df)
print("\n--- CLEANED DATA ---")
print(cleaned_df)
print("\n--- DIAGNOSIS COUNTS ---")
print(cleaned_df["diagnosis"].value_counts())
