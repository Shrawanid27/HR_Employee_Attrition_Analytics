import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"C:\Users\ADIMN\OneDrive\Desktop\HR_Employee_Attrition_Analytics\Dataset\hr_employee_attrition_5000.csv"
)

# -----------------------------
# 1. BASIC INFORMATION
# -----------------------------

print("===== HR EMPLOYEE ATTRITION ANALYSIS =====")

total_employees = len(df)
attrition_count = (df["Attrition"] == "Yes").sum()
active_employees = (df["Attrition"] == "No").sum()
attrition_rate = (attrition_count / total_employees) * 100

print("\n----- EMPLOYEE OVERVIEW -----")
print("Total Employees:", total_employees)
print("Employees Left:", attrition_count)
print("Active Employees:", active_employees)
print("Attrition Rate:", round(attrition_rate, 2), "%")


# -----------------------------
# 2. ATTRITION COUNT
# -----------------------------

print("\n----- ATTRITION COUNT -----")
print(df["Attrition"].value_counts())


# -----------------------------
# 3. DEPARTMENT-WISE ATTRITION
# -----------------------------

print("\n----- DEPARTMENT-WISE ATTRITION -----")

department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

print(department_attrition)


# -----------------------------
# 4. GENDER-WISE ATTRITION
# -----------------------------

print("\n----- GENDER-WISE ATTRITION -----")

gender_attrition = pd.crosstab(
    df["Gender"],
    df["Attrition"]
)

print(gender_attrition)


# -----------------------------
# 5. OVERTIME VS ATTRITION
# -----------------------------

print("\n----- OVERTIME VS ATTRITION -----")

overtime_attrition = pd.crosstab(
    df["Overtime"],
    df["Attrition"]
)

print(overtime_attrition)


# -----------------------------
# 6. JOB SATISFACTION VS ATTRITION
# -----------------------------

print("\n----- JOB SATISFACTION VS ATTRITION -----")

satisfaction_attrition = pd.crosstab(
    df["Job_Satisfaction"],
    df["Attrition"]
)

print(satisfaction_attrition)


# -----------------------------
# 7. BUSINESS TRAVEL VS ATTRITION
# -----------------------------

print("\n----- BUSINESS TRAVEL VS ATTRITION -----")

travel_attrition = pd.crosstab(
    df["Business_Travel"],
    df["Attrition"]
)

print(travel_attrition)


# -----------------------------
# 8. AVERAGE SALARY
# -----------------------------

print("\n----- SALARY ANALYSIS -----")

salary_analysis = df.groupby("Attrition")["Monthly_Income"].mean()

print(salary_analysis)


# -----------------------------
# 9. AVERAGE AGE
# -----------------------------

print("\n----- AGE ANALYSIS -----")

age_analysis = df.groupby("Attrition")["Age"].mean()

print(age_analysis)


# -----------------------------
# 10. YEARS AT COMPANY
# -----------------------------

print("\n----- YEARS AT COMPANY -----")

experience_analysis = df.groupby("Attrition")["Years_At_Company"].mean()

print(experience_analysis)


# -----------------------------
# 11. CHART - ATTRITION
# -----------------------------

plt.figure(figsize=(6, 5))

df["Attrition"].value_counts().plot(kind="bar")

plt.title("Employee Attrition")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()


# -----------------------------
# 12. CHART - DEPARTMENT
# -----------------------------

department_attrition["Yes"].sort_values().plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Department-wise Employee Attrition")
plt.xlabel("Department")
plt.ylabel("Employees Who Left")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# -----------------------------
# 13. CHART - OVERTIME
# -----------------------------

overtime_attrition["Yes"].plot(
    kind="bar",
    figsize=(6, 5)
)

plt.title("Overtime vs Employee Attrition")
plt.xlabel("Overtime")
plt.ylabel("Employees Who Left")

plt.tight_layout()
plt.show()


print("\n===== EDA COMPLETED SUCCESSFULLY =====")