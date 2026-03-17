#python
# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading dataset
df = pd.read_csv("netflix_titles.csv")

# ===============================
# Basic Data Operations
# ===============================
print("===== Basic Data Operations =====")
print("Dataset Shape:", df.shape)
print("Columns:", df.columns)

print("\nDataset Description:")
print(df.describe())

print("\nDataset Information:")
df.info()

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

# ===============================
# Data Understanding
# ===============================
print("\n===== Data Understanding =====")
print("Total show_ids:", df["show_id"].nunique())
print("Total titles:", df["title"].nunique())
print("Total countries:", df["country"].nunique())
print("Total directors:", df["director"].nunique())
print("Total cast entries:", df["cast"].nunique())

print("\nNumerical Columns:", df.select_dtypes(include="number").columns)
print("Categorical Columns:", df.select_dtypes(include="object").columns)

# ===============================
# Handling Missing Values
# ===============================
missing_values = [
    "N/A","NAN","ERROR","error",
    "?","unknown","UNKNOWN","na",
    "Null","null","NULL","-",","
]

df.replace(missing_values, np.nan, inplace=True)

print("\nMissing Values:")
print(df.isnull().sum())

# Filling missing values
df["director"] = df["director"].fillna(df["director"].mode()[0])
df["cast"] = df["cast"].fillna(df["cast"].mode()[0])
df["country"] = df["country"].fillna(df["country"].mode()[0])
df["date_added"] = df["date_added"].fillna(df["date_added"].mode()[0])
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])

# ===============================
# Duration Column Cleaning
# ===============================
# Extract numeric value from duration column
df["duration_value"] = df["duration"].str.extract(r"(\d+)")
df["duration_value"] = df["duration_value"].astype(float)

# Create separate columns
df["movies_runtime"] = df["duration_value"].where(df["type"] == "Movie")
df["shows_runtime"] = df["duration_value"].where(df["type"] == "TV Show")

# Fill missing values
df["movies_runtime"] = df["movies_runtime"].fillna(df["movies_runtime"].mean())
df["shows_runtime"] = df["shows_runtime"].fillna(df["shows_runtime"].mean())

# Convert to integer
df["movies_runtime"] = df["movies_runtime"].astype(int)
df["shows_runtime"] = df["shows_runtime"].astype(int)

# Remove unnecessary columns
df.drop(columns=["duration", "duration_value"], inplace=True)

# ===============================
# Remove Duplicates
# ===============================
print("\nShape before removing duplicates:", df.shape)
df.drop_duplicates(inplace=True)
print("Shape after removing duplicates:", df.shape)

# ===============================
# Feature Engineering
# ===============================

# Rating category
def rating_category(rating):
    if rating in ["TV-Y", "TV-Y7"]:
        return "Kids"
    elif rating in ["TV-14", "PG-13"]:
        return "Teens"
    elif rating in ["TV-MA", "R"]:
        return "Adults"
    else:
        return "General"

df["rating_category"] = df["rating"].apply(rating_category)

# Movie length category
def movies_category(runtime):
    if runtime <= 90:
        return "Short Movie"
    elif runtime <= 120:
        return "Medium Movie"
    else:
        return "Long Movie"

df["movies_category"] = df["movies_runtime"].apply(movies_category)

# ===============================
# Visualization
# ===============================

# Content type distribution
plt.figure(figsize=(6,4))
sns.countplot(x="type", data=df)
plt.title("Movies vs TV Shows Distribution")
plt.show()

# Rating category distribution
plt.figure(figsize=(8,5))
sns.countplot(x="rating_category", data=df)
plt.title("Content Rating Category Distribution")
plt.show()

# Movie runtime distribution
plt.figure(figsize=(8,5))
sns.histplot(df["movies_runtime"], bins=30, kde=True)
plt.title("Movie Runtime Distribution")
plt.show()

# Top 10 countries with most Netflix content
top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()

# Movie category distribution
plt.figure(figsize=(8,5))
sns.countplot(x="movies_category", data=df)
plt.title("Movie Length Category Distribution")
plt.show()
