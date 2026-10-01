# Prodigy InfoTech — Data Science Internship
## Task 02: Data Cleaning and Exploratory Data Analysis

### Project Overview
This project performs data cleaning and exploratory data analysis (EDA) on the Titanic passenger dataset using Python.

### Objective
To clean the dataset, handle missing values, perform basic statistical analysis, and identify patterns and relationships using visualizations.

### Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Git and GitHub

### Data Cleaning
The following preprocessing steps were performed:
- Handled missing values in the Age column using the median.
- Handled missing values in the Embarked column using the mode.
- Removed the Cabin column because it contained a large number of missing values.

### Exploratory Data Analysis
The project includes visualizations for:
- Overall survival count
- Survival by gender
- Passenger age distribution
- Survival by passenger class

### Project Structure
PRODIGY_DS_TASK_02/
+-- dataset/
¦   +-- titanic.csv
+-- output/
¦   +-- age_distribution.png
¦   +-- survival_by_class.png
¦   +-- survival_by_gender.png
¦   +-- survival_count.png
+-- src/
¦   +-- analysis.py
+-- .gitignore
+-- README.md
+-- requirements.txt

### How to Run

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.\.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the analysis:

python .\src\analysis.py

### Conclusion
This project demonstrates a basic data analysis workflow including data cleaning, statistical analysis, and visualization using Python.
