import pandas as pd

# Reading the CSV file
# Make sure your file is named exactly "basic_reader.csv" and located in the same directory
df = pd.read_csv("basic_reader.csv")

# Display the full DataFrame
print("Complete Data:\n", df)

# Convert to a DataFrame (not necessary here because read_csv already returns a DataFrame)
# But keeping it to match your code style
df = pd.DataFrame(df)

# Accessing and displaying the first row using loc
first_row = df.loc[0]
print("\nFirst Row of the DataFrame:\n", first_row)

# Bonus: Displaying some useful information about the CSV
print("\n--- Data Summary ---")
print("Shape of the DataFrame:", df.shape)
print("Column Names:", df.columns.tolist())
print("Data Types:\n", df.dtypes)
print("First 5 Rows:\n", df.head())
