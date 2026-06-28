import pandas as pd
import matplotlib.pyplot as plt

# Load transformed dataset
df = pd.read_csv("titanic_transformed.csv")

# Basic information
print("Dataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Survival Count
plt.figure(figsize=(6,4))
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Number of Passengers")
plt.savefig("survival_count.png")
plt.show()

# Age Distribution
plt.figure(figsize=(6,4))
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("age_distribution.png")
plt.show()

# Fare Distribution
plt.figure(figsize=(6,4))
plt.hist(df["Fare"], bins=20)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.savefig("fare_distribution.png")
plt.show()

print("\nTask 4 Completed Successfully!")