import pandas as pd

# Load transformed dataset
df = pd.read_csv("titanic_transformed.csv")

print("===== Statistical Analysis =====")

# Mean
print("\nMean:")
print(df[["Age", "Fare", "FamilySize"]].mean())

# Median
print("\nMedian:")
print(df[["Age", "Fare", "FamilySize"]].median())

# Mode
print("\nMode:")
print(df[["Age", "Fare", "FamilySize"]].mode())

# Standard Deviation
print("\nStandard Deviation:")
print(df[["Age", "Fare", "FamilySize"]].std())

# Variance
print("\nVariance:")
print(df[["Age", "Fare", "FamilySize"]].var())

# Correlation Matrix
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

print("\nTask 5 Completed Successfully!")