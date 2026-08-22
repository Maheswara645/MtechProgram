import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. CREATE STUDENT PERFORMANCE DATASET
# --------------------------------------------------

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 116, 117, 118, 119, 120],

    "Name": ["Arun", "Bala", "Charan", "Deepak", "Esha",
             "Farhan", "Gokul", "Hari", "Isha", "Jeeva",
             "Karthik", "Lavanya", "Manoj", "Nisha", "Prakash",
             "Rahul", "Sneha", "Tarun", "Varun", "Yash"],

    "Math": [85, 72, 90, 65, 78, 92, 55, 81, 88, 70,
             95, 68, 82, 76, 89, 61, 94, 73, 86, 79],

    "Science": [78, 88, 92, 70, 85, 89, 60, 76, 91, 74,
                93, 72, 79, 83, 87, 65, 90, 69, 84, 77],

    "English": [82, 75, 89, 68, 80, 94, 58, 85, 86, 72,
                96, 75, 84, 78, 91, 63, 92, 76, 88, 80],

    "Computer": [90, 80, 95, 72, 88, 91, 65, 79, 90, 77,
                 98, 70, 81, 85, 88, 68, 96, 74, 87, 82]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# --------------------------------------------------
# 2. ADD MISSING VALUES MANUALLY
# --------------------------------------------------

df.loc[2, "Math"] = None
df.loc[5, "Science"] = None
df.loc[8, "English"] = None
df.loc[12, "Computer"] = None

print("\nMissing Values:")
print(df.isnull().sum())


# --------------------------------------------------
# 3. ADD DUPLICATE RECORD FOR PRACTICE
# --------------------------------------------------

df = pd.concat([df, df.iloc[[3]]], ignore_index=True)

print("\nDataset after adding duplicate:")
print(df)


# --------------------------------------------------
# 4. HANDLE MISSING MARKS
# --------------------------------------------------

subjects = ["Math", "Science", "English", "Computer"]

for subject in subjects:
    df[subject] = df[subject].fillna(df[subject].mean())

print("\nAfter handling missing values:")
print(df.isnull().sum())


# --------------------------------------------------
# 5. REMOVE DUPLICATE RECORDS
# --------------------------------------------------

df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print(df)


# --------------------------------------------------
# 6. CONVERT DATA TYPES
# --------------------------------------------------

df["Student_ID"] = df["Student_ID"].astype(int)

for subject in subjects:
    df[subject] = pd.to_numeric(df[subject])

print("\nData Types:")
print(df.dtypes)


# --------------------------------------------------
# 7. CREATE TOTAL AND AVERAGE COLUMNS
# --------------------------------------------------

df["Total"] = df[subjects].sum(axis=1)

df["Average"] = df[subjects].mean(axis=1)

print("\nFinal Dataset:")
print(df)


# ==================================================
# SEABORN VISUALIZATIONS
# ==================================================

# --------------------------------------------------
# 8. HISTOGRAM - DISTRIBUTION OF MARKS
# --------------------------------------------------

sns.histplot(df["Average"], bins=10, kde=True)

plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")

plt.show()


# --------------------------------------------------
# 9. BOXPLOT - DETECT OUTLIERS
# --------------------------------------------------

sns.boxplot(data=df[subjects])

plt.title("Boxplot of Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()


# --------------------------------------------------
# 10. HEATMAP - CORRELATION
# --------------------------------------------------

correlation = df[subjects + ["Total", "Average"]].corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation Between Student Performance")

plt.show()


# ==================================================
# MATPLOTLIB VISUALIZATIONS
# ==================================================

# --------------------------------------------------
# 11. BAR CHART - AVERAGE MARKS PER SUBJECT
# --------------------------------------------------

subject_average = df[subjects].mean()

plt.bar(subject_average.index, subject_average.values)

plt.title("Average Marks Per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")

plt.show()


# --------------------------------------------------
# 12. LINE CHART - STUDENT PERFORMANCE TREND
# --------------------------------------------------

plt.plot(
    df["Student_ID"],
    df["Average"],
    marker="o"
)

plt.title("Student Performance Trend")
plt.xlabel("Student ID")
plt.ylabel("Average Marks")

plt.grid(True)

plt.show()