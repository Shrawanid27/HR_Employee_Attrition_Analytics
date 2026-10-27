# HR Employee Attrition Analytics

An end-to-end data analytics project that explores employee attrition
patterns and presents actionable workforce insights using **Python, SQL,
and Power BI**. The project analyzes a dataset of 5,000 employee records
to understand where attrition is concentrated and how it relates to
department, age group, job satisfaction, overtime, education, marital
status, income level, business travel, and other workforce attributes.

## Project Overview

Employee attrition can affect team stability, recruitment costs,
productivity, and long-term workforce planning. This project turns
employee data into an analytical view that helps HR teams explore
attrition trends, compare employee groups, and identify areas that may
deserve further investigation.

The workflow covers data understanding and exploratory analysis in
Python, SQL-based data querying, and interactive dashboard reporting in
Power BI.

## Objectives

-   Understand the overall employee population and attrition rate.
-   Compare attrition across departments, gender, age groups, and
    job-related categories.
-   Explore relationships between attrition and factors such as
    overtime, job satisfaction, education, marital status, income
    quartile, and business travel.
-   Build interactive Power BI pages with charts, KPI cards, and
    slicers.
-   Communicate findings through clear, business-focused visualizations.

## Tools and Technologies

  -----------------------------------------------------------------------
  Tool                                Purpose
  ----------------------------------- -----------------------------------
  Python                              Data understanding and exploratory
                                      data analysis (EDA)

  Pandas / NumPy                      Data preparation and analysis

  Matplotlib / Seaborn                Exploratory visualizations

  SQL / MySQL                         Querying and analyzing employee
                                      records

  HeidiSQL                            Database access and SQL query
                                      execution

  Microsoft Power BI                  Interactive dashboards, KPI cards,
                                      slicers, and charts

  CSV                                 Dataset and data exchange format
  -----------------------------------------------------------------------

*The exact libraries and SQL scripts used may vary according to the
files in the project repository.*

## Dataset

-   **Records:** 5,000 employees
-   **Primary outcome:** `Attrition` (whether an employee left)
-   **Database table:** `hr_employee_attrition_5000`
-   **Source file:** `hr_employee_attrition.csv` (use the exact filename
    present in your `Dataset` folder)

The dataset includes employee and work-related attributes such as
department, gender, age/age band, business travel, job role, job
satisfaction, education, marital status, overtime, income-related
fields, and years at the company.

> **Privacy note:** Use only a dataset you are permitted to share. Do
> not upload confidential employee information or personally
> identifiable data to a public repository.

## Key Results

The current analysis reports the following summary figures:

  Metric                     Result
  ------------------------ --------
  Total employees             5,000
  Employees who left          1,227
  Active employees            3,773
  Overall attrition rate     24.54%

### Department-wise employees who left

  Department                 Employees who left
  ------------------------ --------------------
  Research & Development                    346
  Sales                                     292
  IT                                        181
  Finance                                   160
  Marketing                                 147
  Human Resources                           101

### Other observations explored

-   **Gender:** 729 male and 498 female employees are recorded in the
    attrition group.
-   **Overtime:** 439 employees in the attrition group had overtime
    marked `Yes`; 788 had overtime marked `No`.
-   **Job satisfaction:** Attrition counts are compared across Low,
    Medium, High, and Very High satisfaction categories.
-   **Business travel:** Employee counts are compared across
    Travel_Rarely, Travel_Frequently, and Non-Travel.
-   **Age and tenure:** The dashboards compare attrition across age
    bands and years at the company.

These figures describe patterns in this dataset. They do not, by
themselves, establish that any factor causes an employee to leave.

## Power BI Dashboard

The Power BI report contains three pages:

### 1. HR Overview

Provides a high-level summary of the workforce and attrition,
including: - KPI cards for Total Employees, Attrition Count, Attrition
Rate, Average Tenure, and Average Income - Attrition by department -
Attrition by age band - Attrition by job satisfaction - Attrition by
gender - Attrition by job role - Attrition by business travel -
Department, age-group, and gender filters

### 2. Employee Attrition Insights

Focuses on comparisons that may help HR teams investigate attrition
patterns: - Attrition by overtime - Attrition by education level -
Attrition by department and overtime - Attrition by marital status -
Attrition by job satisfaction - Attrition by income level - Attrition by
gender - Attrition rate by years at the company - Attrition and
department filters

### 3. Workforce Attrition Analysis

Explores workforce segments and department-level rates: - Attrition by
business travel - Attrition by gender - Attrition by department -
Attrition by job satisfaction - Attrition by age group - Attrition by
overtime - Department attrition rate chart - Department, age-band, and
overtime filters

The report uses a consistent green theme and interactive slicers to help
users explore the data. Dashboard values can change when filters are
applied.

## Project Structure

The project is organized into the following folders. Update this example
if your repository uses different filenames or capitalization.

``` text
HR_Employee_Attrition_Analytics/
├── Dataset/
│   ├── hr_employee_attrition.csv
│   └── customer_or_cleaned_data.csv   # Include only if this file actually exists
├── Python/
│   └── eda_analysis.py
├── SQL/
│   └── SQL analysis scripts (.sql)
├── PowerBI/
│   └── HR_Analytics_Dashboard.pbix
├── Reports/
│   └── screenshots or project documentation
└── README.md
```

**Important:** Replace example filenames with the exact names in your
repository and remove any entries that do not exist. Do not commit
temporary files or unrelated datasets.

## How to Run the Project

### 1. Clone the repository

``` bash
git clone <your-github-repository-url>
cd HR_Employee_Attrition_Analytics
```

Replace `<your-github-repository-url>` with your repository's actual
GitHub URL.

### 2. Prepare the Python environment

Install Python, then install the libraries used by your analysis script:

``` bash
pip install pandas numpy matplotlib seaborn
```

Run the exploratory analysis from the project root, if the script is
stored at `Python/eda_analysis.py`:

``` bash
python Python/eda_analysis.py
```

If your script or dataset uses a different path, update the command or
file path accordingly.

### 3. Load the data into MySQL

1.  Open MySQL through HeidiSQL or another MySQL client.
2.  Create or select your project database.
3.  Import the employee CSV into a table named
    `hr_employee_attrition_5000`, or update the SQL queries to match
    your actual table name.
4.  Confirm the row count and inspect a small sample before running
    analysis queries.

Example validation queries:

``` sql
SELECT COUNT(*) AS total_employees
FROM hr_employee_attrition_5000;

SELECT Attrition, COUNT(*) AS employee_count
FROM hr_employee_attrition_5000
GROUP BY Attrition;
```

If your database uses different column names or casing, adjust the
queries to match your schema.

### 4. Open the Power BI report

1.  Open `HR_Analytics_Dashboard.pbix` in Power BI Desktop, if included
    in the repository.
2.  If prompted, connect to your local CSV or MySQL source.
3.  Verify the table and column names, then refresh the data.
4.  Check the KPI cards, charts, and slicers on all three report pages.

If the `.pbix` file is not in the repository yet, save your Power BI
report into the `PowerBI` folder before publishing the project.

## Key Analytical Questions

This project helps explore questions such as:

-   What percentage of employees left the organization?
-   Which departments have the highest number of employees in the
    attrition group?
-   How does attrition differ across age groups and genders?
-   How does attrition vary by overtime status?
-   How do job satisfaction, education, marital status, and income
    categories compare?
-   How does attrition vary across years at the company?
-   Which workforce segments should HR investigate further?

## Business Value

The analysis can support HR teams by helping them: - Monitor workforce
attrition using a consistent set of KPIs. - Compare attrition patterns
across departments and employee groups. - Identify areas for deeper
investigation and employee-retention analysis. - Communicate workforce
trends through interactive reporting.

The dashboard is intended for **descriptive analysis**. Any retention
action should be supported by additional context, appropriate
validation, and consultation with employees and HR stakeholders.

## Limitations

-   The results depend on the quality, definitions, and
    representativeness of the dataset.
-   Counts and rates may differ from other HR reports if filters or
    definitions differ.
-   Observed associations do not prove causation.
-   The dashboard does not automatically predict which individual
    employee will leave.
-   Average income and tenure depend on the source data's units and
    definitions.

## Future Improvements

-   Add a documented data-cleaning pipeline and data-quality checks.
-   Add more SQL queries for department and employee-segment analysis.
-   Include dashboard screenshots and a data dictionary.
-   Add a reproducible Python requirements file.
-   Explore validated attrition prediction models, with appropriate
    privacy, fairness, and model-evaluation checks.

## Author

**Shrawani Ramdas Dhadwad**

Data Analytics Project \| Python • SQL • MySQL • Power BI

## License

No license has been specified yet. If you want others to reuse this
project, add an appropriate open-source license file and update this
section.
