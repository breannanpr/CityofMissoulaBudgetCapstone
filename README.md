# City of Missoula Budget Capstone Project


## Project Overview
This repository contains the capstone project for the City of Missoula Finance Department, supported by Mayor Andrea Davis. The goal is to enhance the City's priority-based budgeting and program transparency through structured data cleaning and the creation of a centralized Power BI dashboard.

By combining budget data and program-level survey responses, this tool enables better strategic planning and decision-making by elected officials and city leadership.

## Project Structure

The repository is organized as follows: 
CITYOFMISSOULABUDGETCAPSTONE/

│

├── assets/                              # Supporting documents

│   └── three_ps_niekamp.txt             # Regular progress updates

│

├── code/                                # Project notebooks and scripts

│   └── citydata_exploratory.ipynb       # Data cleaning and transformation pipeline

│

├── data/                                # Raw and processed datasets

│   ├── FY24_Expenditure_Status.xlsx

│   ├── FY24_Revenue_Expense_Data.xlsx

│   ├── Program_Inventory_Internal_Data_Collection.xlsx

│   ├── cleaned_expenditure_status.csv

│   ├── cleaned_program_inventory.csv

│   ├── cleaned_missoula_budget_data.xlsx

│   └── testing_expend_status.csv        # (dev/test file)

│

├── .gitignore                           # Git tracking rules

├── README.md                            # Project overview and documentation


## Data Sources and Overview
- FY24_Expenditure_Status.xlsx - Budget account-level data with activity, dpeartment and objective codes. Export from Eden.
- FY24_Revenue_Expense_Data.xlsx - Multi-sheet revenue, expense, and status exports. Export from Eden. 
- Program_Inventory_Internal_Data_Collection.xlsx - Survey-based program intake / inventory that includes attributes about specific programming (mandates, trends, risks, etc.) Export from City of Missoula Workiva Instance. 

These files are exported from the City of Missoula's Workiva (Wdesk) instance and financial software accordingly. 


### Key Definitions
**Program**: City-funded service or function with a 6-digit code, representing a specific output or public-facing activity. 

**Program Description**: Short summary explaining what the program does, why it exists and how it benefits the community. 

**Mandate**: Legally required (federal, state or court-appointed). Does not include contract-based or optional services. 

**Service Requirements (External)**: Rules imposed by external entities (ex., regulatory agencies), even if the program itself isn't mandated.

**Reliance**: Community dependence or risk of disruption if removed from the community. High reliance = wide usage, few alternatives, or critical outcomes. 

**Trend**: Indicates whether the program's demand is growing, stable, declining or evolving due to external factors. 

**Risk**: Assesses potential challenges in the next 1-3 years (ex., funding cuts, staffing issues, legal changes).

**Internal Use**: Data used internally for planning and analysis, but not necessarily shared publicly. 


## Methodology

### Extraction Process
**[Currently in progress of implementation]**
City of Missoula employee will download data beginning January 1, 2024 through current year to ensure and maintain accuracy for year over year comparison of both program inventory data and financial data. In all there will be three files; Expenditure Status, Revenue Expense and Program Inventory Internal Data Collection. 

These three files will be uploaded into the Sharepoint Site: ***"Missoula PBI - City Program Inventory Budget Breakdown - All Documents"***. 

From this, the files will undergo a cleaning and transformation process, as elaborated in the next section. 


### Cleaning & Transformation Process
Data cleaning and transformation were conducted in Python using pandas, janitor, and other helpful libraries. 


#### Libraries Used
- pandas, numpy: data wrangling
- openpyxl: Exel IO
- janitor, .clean_names(): header normalization
- tqdm, re, os, chardet: helpful cleaning utilities
- missingno, matplotlib.pyplot: EDA tools


#### Steps Summary
**[Currently being revised due to different approach that will follow the below laid out steps.]**
1. File Loading: Using library openpyxl
2. Logic Process: Removes unnecessary information from data before cleaning, pre-processing raw data for cleaning.
3. Column Cleaning: Removing unnamed columns and fixing numeric formatting.
4. Account Parsing: Splitting account numbers into fund, department, activity and more. 
4. Mapping: Automatically sourcing, and Attaching readable department and fund names, redacting account information that is not included in the program inventory. 
5. Header Expansion: Expanding multi-column headers (ex., Mandate in Program Inventory)
6. Whitespace & Case: Stripping extra spaces and applying title case to key labels. 
7. Normalization: All columns are converted to snake_case with clean_names().


### Power BI Integration
**[Currently in progress, will be adding more information to this section. Currently the process is as below]**
The cleaned files are loaded into Power BI to enable: 
- Slicers and filters by Program, Fund, Department
- Strategic attribute visualisations (Risk, Mandate, Goals)
- Investment vs. Impact Insights
- Future year over year comparisons (planned)

***[Currently in progress, this is how the process will be laid out in the future]***
Once the files are placed in the Sharepoint Site location, a bat file will set off a chain of events where Power BI will automatically look at the files, and clean them in Power BI through implementation of a functional python script within the Power BI Dashboard. 
The cleaned data will be visualized in Power BI to enable: 
- Slices and filters by Program, Fund, Department and Activity
- Strategic attribute visualisations (Risk, Mandate, Strategic Goals, Reliance, Trend and additional attributes)
- Investment vs. Impact Insights
- Future Year over Year Comparisons

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
11. Grant (G30): Grant funding received to support the program.
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