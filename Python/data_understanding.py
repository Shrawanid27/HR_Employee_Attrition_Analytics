import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\ADIMN\OneDrive\Desktop\HR_Employee_Attrition_Analytics\Dataset\hr_employee_attrition_5000.csv")

# Display first 5 rows
print("----- FIRST 5 ROWS -----")
print(df.head())

# Number of rows and columns
print("\n----- DATASET SHAPE -----")
print(df.shape)

# Column names
print("\n----- COLUMN NAMES -----")
print(df.columns.tolist())

# Data types
print("\n----- DATA TYPES -----")
print(df.dtypes)

# Missing values
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

# Duplicate rows
print("\n----- DUPLICATE ROWS -----")
print(df.duplicated().sum())

# Basic statistics
print("\n----- BASIC STATISTICS -----")
print(df.describe())