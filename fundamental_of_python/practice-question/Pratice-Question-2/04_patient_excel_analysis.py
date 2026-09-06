"""Integrated Excel question: clean hospital patient data and filter Cardiology bills."""

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "patient_data.xlsx"
OUTPUT_FILE = BASE_DIR / "cardiology_high_bills.xlsx"
REQUIRED_COLUMNS = {"PatientID", "Name", "Age", "Gender", "Department", "AdmissionDate", "BillAmount"}


def create_sample_file():
    """Creates a demonstration input file only if no patient_data.xlsx is provided."""
    if INPUT_FILE.exists():
        return

    sample_data = pd.DataFrame({
        "PatientID": [101, 102, 103, 104, 101],
        "Name": ["Ravi", "Meera", "John", "Sara", "Ravi"],
        "Age": [55, None, 42, 61, 55],
        "Gender": ["Male", "Female", "Male", "Female", "Male"],
        "Department": ["Cardiology", "Neurology", None, "Cardiology", "Cardiology"],
        "AdmissionDate": ["2026-01-05", "2026-01-06", "2026-01-08", "2026-01-10", "2026-01-05"],
        "BillAmount": [75000, 45000, None, 51000, 75000],
    })
    sample_data.to_excel(INPUT_FILE, index=False)


def main():
    create_sample_file()
    patients = pd.read_excel(INPUT_FILE)

    missing_columns = REQUIRED_COLUMNS.difference(patients.columns)
    if missing_columns:
        raise ValueError(f"Excel file is missing columns: {sorted(missing_columns)}")

    # Handle missing numeric values with the column mean and text values with "Unknown".
    patients["Age"] = patients["Age"].fillna(patients["Age"].mean())
    patients["BillAmount"] = patients["BillAmount"].fillna(patients["BillAmount"].mean())
    patients["Department"] = patients["Department"].fillna("Unknown")
    patients["Gender"] = patients["Gender"].fillna("Unknown")

    # Remove duplicate patient records and convert the date.
    patients = patients.drop_duplicates()
    patients["AdmissionDate"] = pd.to_datetime(patients["AdmissionDate"], errors="coerce")

    # Department = Cardiology AND BillAmount > 50000.
    result = patients[(patients["Department"] == "Cardiology") & (patients["BillAmount"] > 50000)]
    print("Filtered patient records:\n", result)

    result.to_excel(OUTPUT_FILE, index=False)
    print(f"\nFiltered records saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
