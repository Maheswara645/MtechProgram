"""Pandas practice questions: DataFrames, cleaning, transformation, and filtering."""

import numpy as np
import pandas as pd


def main():
    # 1. Create a DataFrame. Extra rows make head() and tail() meaningful.
    data = {
        "Name": ["Asha", "Bharat", "Charan", "Divya", "Esha", "Farhan", "Asha"],
        "Age": [19, 21, np.nan, 18, 20, 22, 19],
        "Marks": [85, 78, np.nan, 91, 88, 67, 85],
        "Course": ["Python", "Python", None, "Data Science", "Python", "Data Science", "Python"],
        "ExamDate": ["2026-01-10", "2026-01-11", "2026-01-12", "2026-01-13", "2026-01-14", "2026-01-15", "2026-01-10"],
    }
    students = pd.DataFrame(data)
    print("Original DataFrame:\n", students)

    # 2. Display rows.
    print("\nFirst 5 rows:\n", students.head())
    print("\nLast 3 rows:\n", students.tail(3))

    # 3 and 4. Explore the data.
    print("\nSummary statistics:\n", students.describe())
    print("\nColumn names:", students.columns.tolist())

    # 5. Replace missing values: mean for Marks and a constant for Course.
    students["Marks"] = students["Marks"].fillna(students["Marks"].mean())
    students["Course"] = students["Course"].fillna("Not Assigned")
    print("\nAfter filling Marks and Course:\n", students)

    # 6. Drop rows still containing missing values (Age is missing in one row).
    cleaned_students = students.dropna().copy()
    print("\nAfter dropping remaining missing rows:\n", cleaned_students)

    # 7. Convert columns to integer and category.
    cleaned_students["Age"] = cleaned_students["Age"].astype(int)
    cleaned_students["Course"] = cleaned_students["Course"].astype("category")

    # 8. Convert a date column to datetime.
    cleaned_students["ExamDate"] = pd.to_datetime(cleaned_students["ExamDate"])

    # 9. Filtering with one condition.
    print("\nMarks > 80:\n", cleaned_students[cleaned_students["Marks"] > 80])
    print("\nAge < 20:\n", cleaned_students[cleaned_students["Age"] < 20])

    # 10. Multiple conditions: use &, | and parentheses around each condition.
    print("\nMarks > 80 AND Age < 20:\n", cleaned_students[(cleaned_students["Marks"] > 80) & (cleaned_students["Age"] < 20)])
    print("\nMarks > 80 OR Age < 20:\n", cleaned_students[(cleaned_students["Marks"] > 80) | (cleaned_students["Age"] < 20)])

    # 11. Remove duplicate Name values, keeping the first occurrence.
    unique_names = cleaned_students.drop_duplicates(subset="Name")
    print("\nAfter removing duplicate Names:\n", unique_names)


if __name__ == "__main__":
    main()
