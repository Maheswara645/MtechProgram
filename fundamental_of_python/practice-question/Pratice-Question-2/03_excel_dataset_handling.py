"""Excel dataset handling examples. Install support once with: pip install openpyxl"""

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "employee_data.xlsx"
OUTPUT_FILE = BASE_DIR / "employee_data_cleaned.xlsx"


def create_sample_file():
    """Creates input data only when employee_data.xlsx does not already exist."""
    if INPUT_FILE.exists():
        return

    sample_data = pd.DataFrame({
        "Employee": ["Anil", "Beena", "Chetan", "Divya", "Anil"],
        "Salary": [60000, None, 48000, 75000, 60000],
        "Department": ["IT", "HR", None, "IT", "IT"],
        "JoiningDate": ["2024-01-15", "2024-04-20", "2023-10-05", "2025-02-01", "2024-01-15"],
    })
    sample_data.to_excel(INPUT_FILE, index=False)


def main():
    create_sample_file()

    # 1. Read an Excel file into a DataFrame.
    employees = pd.read_excel(INPUT_FILE)
    print("Read from Excel:\n", employees)

    # 3. Fill numeric missing values with the mean and another column with 0.
    employees["Salary"] = employees["Salary"].fillna(employees["Salary"].mean())
    employees["Department"] = employees["Department"].fillna(0)

    # 4. Remove duplicate records.
    employees = employees.drop_duplicates()

    # 5. Convert date column to datetime.
    employees["JoiningDate"] = pd.to_datetime(employees["JoiningDate"])

    # 6. Extract selected columns.
    selected_columns = employees[["Employee", "Salary", "Department"]]
    print("\nSelected columns:\n", selected_columns)

    # 7. Single-condition filters.
    print("\nSalary > 50000:\n", employees[employees["Salary"] > 50000])
    print("\nDepartment is IT:\n", employees[employees["Department"] == "IT"])

    # 8. Multiple conditions.
    it_high_salary = employees[(employees["Salary"] > 50000) & (employees["Department"] == "IT")]
    print("\nSalary > 50000 AND Department is IT:\n", it_high_salary)

    # 2. Write the processed DataFrame back to Excel.
    employees.to_excel(OUTPUT_FILE, index=False)
    print(f"\nCleaned data saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
