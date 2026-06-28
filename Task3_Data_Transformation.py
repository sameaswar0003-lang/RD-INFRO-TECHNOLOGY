import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("titanic_cleaned.csv")

# Display data types
print("Data Types Before Transformation:")
print(df.dtypes)

# Create a new column: FamilySize
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Create a new column: IsAlone
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

# Convert Sex column to numeric values
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

# Convert Embarked column to numeric values
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

# Display first 5 rows
print("\nTransformed Dataset:")
print(df.head())

# Save transformed dataset
df.to_csv("titanic_transformed.csv", index=False)

print("\nTask 3 Completed Successfully!")