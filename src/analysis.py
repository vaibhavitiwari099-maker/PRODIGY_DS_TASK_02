import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "dataset/titanic.csv"
df = pd.read_csv(file_path)

# Display basic information
print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Data cleaning
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove unnecessary column
df = df.drop(columns=["Cabin"])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# Visualization 1: Survival Count
# -----------------------------
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Survived")
plt.title("Titanic Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("output/survival_count.png", dpi=300)
plt.show()

# -----------------------------
# Visualization 2: Survival by Gender
# -----------------------------
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("output/survival_by_gender.png", dpi=300)
plt.show()

# -----------------------------
# Visualization 3: Age Distribution
# -----------------------------
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", bins=30, kde=True)
plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("output/age_distribution.png", dpi=300)
plt.show()

# -----------------------------
# Visualization 4: Survival by Passenger Class
# -----------------------------
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Pclass", hue="Survived")
plt.title("Survival by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("output/survival_by_class.png", dpi=300)
plt.show()

print("\nEDA completed successfully!")