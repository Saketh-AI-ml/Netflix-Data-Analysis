# Netflix-Data-Analysis
Exploratory Data Analysis of Netflix dataset using Python, Pandas, Matplotlib and Seaborn.
# Netflix Data Analysis Project

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on a Netflix dataset to understand the distribution of movies and TV shows available on the platform. The analysis focuses on cleaning the dataset, handling missing values, creating useful features, and visualizing patterns related to countries, ratings, and content duration.

The goal of this project is to extract meaningful insights from the dataset and provide recommendations that could help improve content strategy.

---

## 📊 Dataset

The dataset used in this project contains information about Netflix titles including:

* Show ID
* Title
* Director
* Cast
* Country
* Date Added
* Release Year
* Rating
* Duration
* Type (Movie / TV Show)

Dataset file: **netflix_titles.csv**

---

## 🛠 Tools and Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## 🔄 Project Workflow

### 1. Data Loading

The dataset is loaded using the Pandas library.

### 2. Data Understanding

Basic dataset exploration was performed including:

* Dataset shape
* Column names
* Data types
* Unique values
* Summary statistics

### 3. Data Cleaning

Data preprocessing steps included:

* Handling missing values
* Replacing invalid values with NaN
* Filling missing values using mode and mean
* Removing duplicate records

### 4. Feature Engineering

New features were created to improve analysis:

**Runtime Features**

* Extracted numeric values from the duration column
* Created separate columns for:

  * Movie runtime
  * TV show seasons

**Categorical Features**

* Rating category
* Movie runtime category (Short / Medium / Long)

### 5. Data Visualization

Visualizations were created using Matplotlib and Seaborn to understand content distribution across countries and other attributes.

---

## 📈 Key Insights

1. Movies make up the majority of Netflix content compared to TV shows.

2. The United States contributes the largest number of titles in the dataset.

3. Most movies have a runtime between **90 and 120 minutes**, which is considered optimal for streaming audiences.

4. TV shows usually have fewer seasons, indicating that many series are short-form.

5. Adult and teenage rating categories dominate the platform's content.

---

## 💡 Recommendations

* Increase the number of TV shows to encourage longer user engagement.
* Expand children and family-friendly content.
* Invest more in international and regional productions.
* Focus on producing movies with medium runtime (around 90–120 minutes).
* Encourage development of multi-season TV shows to improve viewer retention.

---

## 📊 Example Visualization

The project includes visualizations such as:

* Content distribution by country
* Movie runtime categories
* Rating distribution

---

## 🚀 How to Run the Project

1. Clone the repository
2. Install required libraries

pip install pandas numpy matplotlib seaborn

3. Run the Jupyter Notebook

## 📌 Project Objective

The main objective of this project is to demonstrate **data cleaning, feature engineering, exploratory data analysis, and visualization skills using Python**.

This project can be used as part of a **data analyst portfolio** to showcase practical data analysis skills.
## 👨‍💻 Author
Data Analysis Project using Python
Exploratory Data Analysis on Netflix Dataset
