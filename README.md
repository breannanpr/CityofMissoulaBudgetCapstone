# City of Missoula Budget Capstone Project


## Project Overview
This repository contains the capstone project for the City of Missoula Finance Department, supported by Mayor Andrea Davis. The goal is to enhance the City's priority-based budgeting and program transparency through structured data cleaning and the creation of a centralized Power BI dashboard.

By combining budget data and program-level survey responses, this tool enables better strategic planning and decision-making by elected officials and city leadership.

## Project Structure

The repository is organized as follows: 

CITYOFMISSOULABUDGETCAPSTONE/
│
├── assets/                             # Supporting documents and visuals
│   ├── *.png                           # Screenshots and data previews
│   └── three_ps_niekamp.txt           # Running dev notes
│
├── cleaned_outputs/                    # Final outputs used by Power BI
│   ├── cleaned_expenditure_status.csv
│   └── cleaned_program_inventory.csv
│
├── code/                               # Jupyter notebooks and Python scripts
│   ├── citydata_01_cleaning.ipynb      # Full cleaning pipeline (this project)
│   └── citydata_02_exploratory.ipynb   # Exploratory visuals and analysis
│
├── data/                               # Raw source data from internal systems
│   ├── FY24_Expenditure_Status.xlsx
│   ├── FY24_Revenue_Expense_Data.xlsx
│   └── Program_Inventory_Internal_Data_Collection.xlsx
│
├── .gitignore                          # Ignore untracked files
├── README.md                           # This file


## Data Sources and Overview
- FY24_Expenditure_Status.xlsx - Budget account-level data with activity, dpeartment and objective codes. Export from Tyler Edens.
- FY24_Revenue_Expense_Data.xlsx - Multi-sheet revenue, expense, and status exports. Export from Tyler Edens. 
- Program_Inventory_Internal_Data_Collection.xlsx - Survey-based program intake / inventory that includes attributes about specific programming (mandates, trends, risks, etc.) Export from City of Missoula Workiva Instance. 

These files are exported from the City of Missoula's Workiva (Wdesk) instance and financial software accordingly. 

## Methodology

### Key Definitions
**Program**: City-funded service or function with a 6-digit code, representing a specific output or public-facing activity. 

**Program Description**: Short summary explaining what the program does, why it exists and how it benefits the community. 

**Mandate**: Legally required (federal, state or court-appointed). Does not include contract-based or optional services. 

**Service Requirements (External)**: Rules imposed by external entities (ex., regulatory agencies), even if the program itself isn't mandated.

**Reliance**: Community dependence or risk of disruption if removed from the community. High reliance = wide usage, few alternatives, or critical outcomes. 

**Trend**: Indicates whether the program's demand is growing, stable, declining or evolving due to external factors. 

**Risk**: Assesses potential challenges in the next 1-3 years (ex., funding cuts, staffing issues, legal changes).

**Internal Use**: Data used internally for planning and analysis, but not necessarily shared publicly. 


### Extraction Process
**[Currently in progress of implementation]**
City of Missoula employee will download data beginning January 1, 2024 through current year to ensure and maintain accuracy for year over year comparison of both program inventory data and financial data. In all there will be three files; Expenditure Status, Revenue Expense and Program Inventory Internal Data Collection. 

These three files will be uploaded into the Sharepoint Site: ***"Missoula PBI - City Program Inventory Budget Breakdown - All Documents"***. 

From this, the files will undergo a cleaning and transformation process, as elaborated in the next section. 


### Cleaning & Transformation Process
All Cleaning is conducted in Python, designed to support automation and repeatability. The core script has been designed to integrate into both PowerBI and a standalone environment for testing/debugging. 

#### Libraries Used
- pandas, numpy: data wrangling
- openpyxl: Exel IO
- janitor, .clean_names(): header normalization
- tqdm, re, os, chardet: helpful cleaning utilities
- missingno, matplotlib.pyplot: EDA tools


#### Steps Summary

##### Step 1: Import Libraries
Clean separation of standard libraries, text parsing, data wrangling, and Excel handling.

##### Step 2: Define Cleaning Functions
All transformation logic is modularized with custom functions:
- drop_unnamed_columns(), clean_identifiers(), strip_whitespace_and_standardize(), etc.

##### Step 3: Load Raw Files
Uses openpyxl for compatibility with complex Excel sheets. Only relevant sheets are loaded for efficiency.

##### Step 4: Filter Raw Expenditure Status
Applies logic filters to keep only valid transactional rows:
- Excludes empty, subtotal, and non-financial rows.
- Ensures each row has a valid department and numeric content.

##### Step 5: Restructure Expenditure Data
Parses the composite account_number into its individual fields:
- fund_no, dept_no, activity_code, object_code, and sub_object_code
- Handles missing or malformed subcodes (like 0, 00X, or empty) gracefully.
- Extracts the account_description and ensures numerical consistency.

##### Step 6: Expand Headers in Program Inventory
Expands multi-part headers from Workiva survey (ex: Mandate, Trend, Risk) into structured columns.

##### Step 7: Clean Program Inventory
Standardizes IDs (fund, dept_no, activity) and fills missing values with "blank" for Power BI clarity.

##### Step 8: Normalize Column Headers
All columns are converted to snake_case using pyjanitor, and trailing underscores are removed. Multi-sheet normalization is also applied to the revenue workbook.

##### Step 9: Validations
Includes null checks, data type summaries, and duplicate checks to verify integrity across both datasets.

##### Step 10: Apply Department Mapping
Department names are pulled from the program_inventory, then mapped onto the cleaned expenditure data using dept_no as a shared key.

##### Step 11: Export Cleaned Files
The cleaned datasets are saved to cleaned_outputs/:
- cleaned_expenditure_status.csv
- cleaned_program_inventory.csv


### Power BI Integration
**[Currently in progress, will be adding more information to this section. Currently the process is as below]**
This pipeline is automated directly within Power BI. 
1. Beginning with the SharePoint File Drop 

Raw .xlsx files (Expenditure, Revenue/Expense, Program Inventory) are uploaded to a desginated SharePoint folder: 
- Missoula PBI - City Program Inventory Budget Breakdown - All Documents

2. Power BI Python Script

Power BI will: 
- Pull the raw files directly from SharePoint
- Execute the same cleaning pipeline using the Python Script inside (citydata_01_cleaning.py)
- Generate cleaned, in-memory dataframes used for dashboard visualizations

3. No Pre-Clean Required

Users only need to upload raw files. The cleaning script takes care of the rest - cleaning, mapping, and shaping all the data in real-time. 

#### Dashboard Features

***[Currently in progress, this is how the process will be laid out in the future]***
Power BI will support: 
- Filtering by Fund, Department, Program and Activity
- Visual Summaries for: 
    - Mandates
    - Strategic Goal Alignment
    - Program Risk & Demand
    - Operational vs Personnel Costs
- Investment-to-impact visualizations
- Future year-over-year comparisons (planning for multi-year tracking and comparison)

### Exploratory Analysis
**[In progress]**
An additional notebook (citydata_02_exploratory.ipynb) is used to analyze trends, detect anomolies, and explore departmental allocation breakdowns outside the dashboard environment. 
This helps: 
- Validate that cleaning logic is producing correct aggregates
- Spot patterns or outliers ahead of time
- Offer advanced visual insights not necessariliy included in Power BI (Currently)


## Appendicies 

### Appendix 1A: City Program Inventory Internal Data Collection Data Columns (Subject to Confirmation)

1. Fund: Identifies the financial fund supporting the program.
2. Org: Department responsible for the program’s delivery or oversight. 
3. Activity: Code linked to a specific function or financial activity in the City's system.
4. Program Title (H8): The name of the city-funded service or function.
5. Requested Title Change (I9): Suggested updates to program titles, submitted by departments.
6. Department (H6): Label for the department managing the program.
7. FTEs (H36): Full-Time Equivalent employees assigned to the program.
8. Personnel (G27): Budget for salaries, benefits, and direct staff compensation.
9. O&M (G28): Operational costs and maintenance-related expenses.
10. Debt (G29): Costs related to debt service obligations.
11. Grant (G30): Costs related to Grant paid to other organizations.
12. Transfers (G31): Transfers between funds or departments.
13. Captial (G32): Capital expenditures for infrastructure or equipment.
14. Total Expenditures (G33): Sum of all budgeted costs for the program.
15. Cost Recovery (E58, P24): Portion of program costs offset by revenue sources.
16. Description (E12): Written explanation of the program’s purpose and activities.
17. Additional Activities (E20): Notes extra roles, services, or responsibilities.
18. Mandate (E41, H41, E43): Indicates legal requirement, authority, and rationale.
19. Service Level (E47, H47, E49): Describes level of service offered and justification.
20. Reliance & Interdependencies (E53, E55): Captures both community dependence and internal links to other programs.
21. Strategic Goal (E64, E66, E68, E74, E80): Tags which City strategic goals the program supports.
22. Trend (Demand) (E87, E89): Describes changes in demand or usage over time.
23. Risk (E93, E95): Identifies short-term risks and supporting notes.