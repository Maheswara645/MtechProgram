import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    "Name": ["Arun", "Bala", "Chitra", "David", "Elena", "Fahad", "Gokul", "Hari", "Isha", "John", "Kiran", "Latha", "Manoj", "Nisha", "Priya"],
    "Maths": [85, 72, 90, 65, np.nan, 78, 88, 55, 92, 70, 80, 95, 60, 75, 85],
    "Science": [80, 75, 88, 70, 82, np.nan, 90, 60, 95, 68, 85, 92, 65, 78, 80],
    "English": [78, 80, 85, 68, 75, 82, np.nan, 58, 90, 72, 88, 94, 62, 76, 83]
}

df = pd.DataFrame(data)

df = pd.concat([df, df.iloc[[2]]], ignore_index=True)

print(df.isnull().sum())

df["Maths"] = df["Maths"].fillna(df["Maths"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())
df["English"] = df["English"].fillna(df["English"].mean())

df = df.drop_duplicates()

df["Student_ID"] = pd.to_numeric(df["Student_ID"])
df["Maths"] = pd.to_numeric(df["Maths"])
df["Science"] = pd.to_numeric(df["Science"])
df["English"] = pd.to_numeric(df["English"])

df["Total"] = df["Maths"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

print(df)

sns.histplot(df["Maths"], bins=5, kde=True)
plt.title("Distribution of Maths Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Number of Students")
plt.show()

sns.boxplot(data=df[["Maths", "Science", "English"]])
plt.title("Boxplot of Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

correlation = df[["Maths", "Science", "English", "Total", "Average"]].corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Between Student Marks")
plt.show()

subjects = ["Maths", "Science", "English"]

subject_averages = [
    df["Maths"].mean(),
    df["Science"].mean(),
    df["English"].mean()
]

plt.bar(subjects, subject_averages)
plt.title("Average Marks Per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.show()

plt.plot(df["Student_ID"], df["Average"], marker="o")
plt.title("Student Performance Trend")
plt.xlabel("Student ID")
plt.ylabel("Average Marks")
plt.show()