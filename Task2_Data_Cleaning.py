import pandas as pd

# Load the dataset
df = pd.read_csv("titanic.csv")

# Display missing values
print("Missing Values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin column
df = df.drop(columns=["Cabin"])

# Check if cleaning was successful
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save the cleaned dataset
df.to_csv("titanic_cleaned.csv", index=False)

print("\nTask 2 Completed Successfully!")