import pandas as pd

df = pd.read_csv("student_scores.csv")

# Calculate total and percentage
df["Total"] = df[["Maths", "Science", "English", "History"]].sum(axis=1)
df["Percentage"] = df["Total"] / 4

# Display and save new file
print(df)
df.to_csv("student_scores_with_percentage.csv", index=False)
