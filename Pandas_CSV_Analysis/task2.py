import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("students.csv")

print("Full data:")
print(df)

# First 5 rows
print("\nHead (first 5 rows):")
print(df.head())

# Last 5 rows
print("\nTail (last 5 rows):")
print(df.tail())

# Data type of each column
print("\nData types:")
print(df.dtypes)

# Number of rows and columns
print("\nShape (rows, columns):", df.shape)

# Column names
print("\nColumns:", list(df.columns))

# Short summary of the whole DataFrame
print("\nInfo:")
df.info()
# ---------- Step 2: Summary Statistics ----------
print("\n===== STEP 2: SUMMARY STATISTICS =====")

# Statistics of a single column
print("\nMean of marks:", df["marks"].mean())
print("Median of marks:", df["marks"].median())
print("Minimum marks:", df["marks"].min())
print("Maximum marks:", df["marks"].max())
print("Count of marks:", df["marks"].count())

# Other useful ones
print("Sum of marks:", df["marks"].sum())
print("Standard deviation:", df["marks"].std())

# All statistics at once for numeric columns
print("\nDescribe:")
print(df.describe())

# Group-wise statistics: average marks per department
print("\nAverage marks by department:")
print(df.groupby("department")["marks"].mean())

# Count of students in each city
print("\nStudents per city:")
print(df["city"].value_counts())
# ---------- Step 3: Filter, Select, Slice ----------
print("\n===== STEP 3: FILTER, SELECT, SLICE =====")

# --- Selecting columns ---
print("\nOne column (name):")
print(df["name"])

print("\nMultiple columns (name, city, marks):")
print(df[["name", "city", "marks"]])

# --- Filtering rows ---
print("\nStudents with marks above 80:")
top_students = df[df["marks"] > 80]
print(top_students)

print("\nStudents from Lahore:")
print(df[df["city"] == "Lahore"])

# Multiple conditions: use & for AND, | for OR (each condition in brackets)
print("\nLahore students with marks above 80:")
print(df[(df["city"] == "Lahore") & (df["marks"] > 80)])

print("\nStudents from CS or IT department:")
print(df[df["department"].isin(["CS", "IT"])])

# --- Slicing ---
# iloc = select by position (row number / column number)
print("\nFirst 3 rows (iloc):")
print(df.iloc[0:3])

print("\nRows 2 to 5, columns 1 to 3 (iloc):")
print(df.iloc[2:6, 1:4])

# loc = select by label (row label / column name)
print("\nRows 0 to 3, only name and marks (loc):")
print(df.loc[0:3, ["name", "marks"]])

# Sorting
print("\nTop 5 students by marks:")
print(df.sort_values("marks", ascending=False).head(5))
# ---------- Step 4: Save Filtered Results ----------
print("\n===== STEP 4: SAVE RESULTS =====")

# Filter: students with marks above 80
top_students = df[df["marks"] > 80]

# Save to CSV (index=False avoids saving the row numbers as an extra column)
top_students.to_csv("top_students.csv", index=False)
print("Saved top_students.csv")

# Save to Excel
top_students.to_excel("top_students.xlsx", index=False)
print("Saved top_students.xlsx")

# Save only selected columns of Lahore students
lahore = df[df["city"] == "Lahore"][["name", "department", "marks"]]
lahore.to_csv("lahore_students.csv", index=False)
print("Saved lahore_students.csv")

# Save multiple sheets into one Excel file
with pd.ExcelWriter("students_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="All Students", index=False)
    top_students.to_excel(writer, sheet_name="Top Students", index=False)
    lahore.to_excel(writer, sheet_name="Lahore", index=False)
print("Saved students_report.xlsx with 3 sheets")

# Read the saved files back to verify
print("\nReading top_students.csv back:")
print(pd.read_csv("top_students.csv"))

print("\nReading top_students.xlsx back:")
print(pd.read_excel("top_students.xlsx"))