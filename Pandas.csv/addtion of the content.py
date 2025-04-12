import pandas as pd

# Read the CSV file (make sure the file is named exactly like this and is in the same folder)
df = pd.read_csv("basicreader.csv")

# Display the full DataFrame
print("Complete Data:\n", df)

# Accessing and displaying the first row using loc
first_row = df.loc[0]
print("\nFirst Row of the DataFrame:\n", first_row)

# Summary Info
print("\n--- Data Summary ---")
print("Shape of the DataFrame:", df.shape)
print("Column Names:", df.columns.tolist())
print("Data Types:\n", df.dtypes)
print("First 5 Rows:\n", df.head())

# Calculate and print total marks for the first 10 students (or less if DataFrame has fewer rows)
print("\n--- Total Marks for First 10 Students ---")
for x in range(min(10, len(df))):  # prevents going out of bounds
    student = df.loc[x]
    total = student["English"] + student["Science"] + student["Maths"]
    print(f"{student['Name']} (ID: {student['StudentID']}) - Total Marks: {total}")
