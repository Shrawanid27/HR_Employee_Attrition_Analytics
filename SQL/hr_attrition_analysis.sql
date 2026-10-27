
-- HR EMPLOYEE ATTRITION ANALYSIS
-- Dataset: 5000 employees

-- 1. Total Employees
SELECT COUNT(*) AS total_employees
FROM hr_employee_attrition;

-- 2. Attrition Overview
SELECT
    Attrition,
    COUNT(*) AS employee_count
FROM hr_employee_attrition
GROUP BY Attrition;

-- 3. Department-wise Attrition
SELECT
    Department,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left,
    ROUND(
        100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    ) AS attrition_rate_pct
FROM hr_employee_attrition
GROUP BY Department
ORDER BY attrition_rate_pct DESC;

-- 4. Gender-wise Attrition
SELECT
    Gender,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left
FROM hr_employee_attrition
GROUP BY Gender;

-- 5. Overtime vs Attrition
SELECT
    Overtime,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left
FROM hr_employee_attrition
GROUP BY Overtime;

-- 6. Job Satisfaction vs Attrition
SELECT
    Job_Satisfaction,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left
FROM hr_employee_attrition
GROUP BY Job_Satisfaction
ORDER BY employees_left DESC;

-- 7. Business Travel vs Attrition
SELECT
    Business_Travel,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left
FROM hr_employee_attrition
GROUP BY Business_Travel;

-- 8. Average Monthly Income by Attrition
SELECT
    Attrition,
    ROUND(AVG(Monthly_Income), 2) AS average_monthly_income
FROM hr_employee_attrition
GROUP BY Attrition;

-- 9. Average Age by Attrition
SELECT
    Attrition,
    ROUND(AVG(Age), 2) AS average_age
FROM hr_employee_attrition
GROUP BY Attrition;

-- 10. Average Years at Company by Attrition
SELECT
    Attrition,
    ROUND(AVG(Years_At_Company), 2) AS average_years_at_company
FROM hr_employee_attrition
GROUP BY Attrition;
