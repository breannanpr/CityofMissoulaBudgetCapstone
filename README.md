# 🏛️ City of Missoula Budget Capstone Project 🏛️


## Overview
This repository supports the City of Missoula’s public budgeting efforts by connecting raw financial data with narrative program information through an interactive Power BI dashboard and internal training tool. This project was developed in partnership with the City of Missoula Finance Department and is being used to support long-term transparency, strategic alignment, and informed decision-making across City government.

This project serves as the hub for a final Capstone Project for the MSBA program at the University of Montana.


## Project Structure

While the image files were removed from the below summary list, they can be found in the assets/ folder. 

The repository is organized as follows for brevity: 

```
CityofMissoulaBudgetCapstone/
│
├── assets/                                             # Relevant files + images for project
│   ├── budget_data_cleaning_procedure_20250502.pdf     # Procedural Document for Annual Process
│   ├── FY2025_chart_of_acct_structure.pdf              # Supporting Document of Budget Hierarchy
│   ├── program_inventory_internal_data_collection.pdf  # FY24 Internal Data Collection Survey
│   ├── written_product_niekamp_20250502_v4.pdf         # Written Product
│   └── three_ps_niekamp.txt                            # Weekly Project Updates Log
│
├── cleaned_outputs/                                    # Final clean data for app + dashboard
│   ├── cleaned_expenditure_status.csv
│   └── cleaned_program_inventory.csv
│
├── streamlit_app                                       # Digital product files; internal tool
│   ├── assets/
│   ├── digital_product_internal_tool.py
│   ├── pages.py
│   ├── requirements.txt
│   ├── style.py
│   └── utils.py
|
├── data/                                               # Raw City of Missoula data (ignored)
│   └── *.xlsx
│
│── citydata_01_cleaning.ipynb                          # Narrated data cleaning process by step
│── citydata_02_exploratory.ipynb                       # Narrated data analysis process by step
├── README.md                                           # You’re reading it!
└── .gitignore                                          # Clean Git tracking
```


## Data Sources Overview
- **FY24_Expenditure_Status.xlsx**: Budget account-level data with activity, department and objective codes. Export from Tyler Edens.
- **Program_Inventory_Internal_Data_Collection.xlsx**: Survey-based program intake / inventory that includes attributes about specific programming (mandates, trends, risks, etc.) Export from Workiva. 

## Final Deliverables Overview
- Final [**Program Inventory and Expenditure Dashboard**](https://app.powerbigov.us/view?r=eyJrIjoiMTYxNmYxYTgtYjhjZC00YjdhLTliOTItMDY3YmEzODY0ZTczIiwidCI6Ijc4MGM5OGZhLTc3ZDYtNGMwZi05NzJhLTM5YjQ5MGE0ZjY0MSJ9)
- Final Digital Product and [**Internal Training Tool for Expenditure Status**](https://expendituretrainingmt2025.streamlit.app/)
- Final [**Written Product**](https://github.com/breannanpr/CityofMissoulaBudgetCapstone/blob/main/assets/written_product_niekamp_20250502_v4.pdf), Elevating Decision-Making in Missoula's Budget Adoption Process
- [**Budget Data Cleaning Procedure Documentation**](https://github.com/breannanpr/CityofMissoulaBudgetCapstone/blob/main/assets/budget_data_cleaning_procedure_20250502.pdf)
- [**Google Colab Environment**](https://colab.research.google.com/drive/1d5DcpU9pPE3S6YncbMMwBcjf7saI8NgW?usp=sharing) that contains the Data Cleaning Pipeline
- [**Exploratory Analysis Jupyter Notebook**](https://github.com/breannanpr/CityofMissoulaBudgetCapstone/blob/main/citydata_02_exploratory.ipynb) for FY24 Data 


## Methodology

The City of Missoula focuses on priority based budgeting practices. This is essential given that many programs are required by various factors. Because this topic is easily misconstrued, here is a summary of frequent terminology used in this project (More detailed definitions available in Appendicies). 


### Key Definitions
- **Program**: City-funded service or function with a 6-digit code, representing a specific output or public-facing activity. 
- **Mandate**: Legally required (federal, state or court-appointed). Does not include contract-based or optional services. 
- **Service Level Requirements (External)**: Rules imposed by external entities (ex., regulatory agencies), even if the program itself isn't mandated.
- **Reliance**: Community dependence or risk of disruption if removed from the community. High reliance = wide usage, few alternatives, or critical outcomes. 
- **Trend**: Indicates whether the program's demand is growing, stable, declining or evolving due to external factors. 
- **Risk**: Assesses potential challenges in the next 1-3 years (ex., funding cuts, staffing issues, legal changes).
- **Cost Recovery**: Indicates whether or not a program experiences any form of cost recovery meaning, a portion of program costs are offset by revenue sources.


### Annual Cleaning and Transformation Process

While the process below is detailed for this repository, ultimately Google Colab was used to perform and carry out the final cleaning pipeline. 

In order to begin a refreshed cycle of visualizing the City of Missoula's Program Inventory data, a City of Missoula employee follow the guidelines and tasks outlined in the supporting **[budget data cleaning documentation](https://github.com/breannanpr/CityofMissoulaBudgetCapstone/blob/main/assets/budget_data_cleaning_procedure_20250502.pdf)**, provided to the city. 

Once the steps are carried out, two cleaned files are uploaded into the the appropriate Sharepoint Site folder: **[Missoula PBI - City Program Inventory Budget Breakdown](https://cityofmissoulagcc.sharepoint.com/sites/MissoulaPBI/CPIBB/Forms/AllItems.aspx)**. After the process is completed in full, the user will have a fully updated interactive dashboard. 

All cleaning is conducted in Python using modular, documented functions that support automation and integration with the Power BI Platform. For a more comprehensive breakdown of each of the steps, please review the ```citydata_01_cleaning.ipynb``` in this repository. 


#### Steps Summary
**Step 1:** Import Libraries Used

```
pandas, numpy                   ## Data wrangling
openpyxl                        ## Excel file I/O
janitor                         ## Header normalization and chaining helpers
tqdm, re, os, chardet           ## Cleaning utilities
missingno, matplotlib.pyplot    ## EDA visual tools
```


**Step 2:** Define Cleaning Functions
- Creating a set of helper functions reduced repetition and provides greater clarity, below are some notable functions used and an explanation of what they do. 

```
drop_unnamed_columns()          ## Removes Excel filler columns

clean_numeric_column()          ## Fixes trailing .0 artifacts

clean_identifiers()             ## standardizes key indentifiers and applies formatting

expand_multicolumn_headers()    ## Converts original clumped "Mandate" column into multiple structured column headers

apply_department_and_fund_mappings() ## easilty identified mappings for city codes

clean_program_inventory()       ## full cleaning pipeline for program inventory data

strip_whitespace_and_standardize() ## Cleans casing and trailing spaces

remove_trailing_underscores()   ## Final polish on column names
```


**Step 3:** Load Raw Files
- Reads in both Excel exports using ```openyxl```


**Step 4:** Expenditure Status Filtering
- Creates six individual filtering conditions on the Expenditure Status file; 
    - Removes subtotal/blank rows
    - Confirms numeric validity
    - Retains specific row and column combinations


**Step 5:** Account Code Decomposition
- Breaks out ```account_number``` within the Expenditure status data into:

```
fund_no,                ## related to four digit fund code

dept_no,                ## related to three digit department code

activity_code,          ## related to six digit unique activity codes

object_code,            ## related to three digit budget object code

sub_object_code         ## related to three digit sub budget object code
```


**Step 6:** Program Inventory Header Expansion
- Converts wide format survey headers (e.g. "Mandate (E41, H41, E43)") into proper named fields


**Step 7:** Clean Program Inventory
- Calls in our ```clean_program_inventory()``` function
- Standardizes IDs (```fund, dept_no, activity```)
- Fills empty responses with "blank" for BI compatibility


**Step 8:** Normalize Column Names
- Converts all columns to ```snake_case``` using ```janitor.clean_names()```
- Removes trailing _ characters
- Applies across both program and revenue workbooks


**Step 9:** Validate Structure

```
missingno.matrix()           ## confirms data completeness

.describe() and .info()      ## checks used on each dataset
```

Spot checks confirm no corrupted rows or null-heavy fields


**Step 10:** Apply Final Mappings
- Merges ```dept_map``` and ```fund_map``` for readability
- Unmapped entries are labeled "unmapped" for visibility


**Step 11:** Export Cleaned Files
- Final files are saved to cleaned_outputs/ for use in:
    - Streamlit Hosted Internal Expenditure Status Training Tool
    - Power BI Dashboard


## Streamlit Digital Product: Internal Training Tool
The Streamlit app allows the user to experience what it is like to be included in the budget planning process in the City of Missoula. Whether you are planning to run for a position on the City Council, aspire to be the Mayor or will be filling a supporting staff role - This tool educates understanding of budget tradeoffs by allocating funds across the four strategic goals; Community Design and Livability, Community Saftety Health and Well-Being, Organizational Excellence and Resilience, and Economic Health using priority-based budgeting practices.

Explore:
- Understanding how program risks, requirements and mandates reduce available budget
- Understanding how strategic goals align with priority-based budgeting
- Understanding the breakdown of what is included in all of the budgeted costs for a program. 

**[Launch App (Streamlit Cloud)](https://expendituretrainingmt2025.streamlit.app/)** | [View the Full Code: **Streamlit_app**](https://github.com/breannanpr/CityofMissoulaBudgetCapstone/tree/main/streamlit_app)

**[Leave a comment about your experience](https://docs.google.com/forms/d/e/1FAIpQLSdOltLVM-Sb7vrwDpKbwmf82047GzrqpWmDYE8fHGUFD-22lw/viewform?usp=header)** with the training tool. 


## Raw Data to Power BI Pipeline
This partially manual and automatic data cleaning pipeline utilizes Google Colab as a data cleaning processor to host python code in an interactive environment for the employee carrying out the task. 

**1. Beginning Extracting the Raw Data Files**
- Raw .xlsx files (Expenditure Status, Program Inventory) are extracted and saved within the employees desktop. 
    - File format "Expenditure_Status.xlsx" for Expenditure Status. 
    - File Format: "Program_Inventory_Internal_Data_Collection.xlsx" for Program Inventory. 

**NOTE: It is essential that these file names are accurate for the integrity of the data cleaning process. Overwrite existing file when dropping them into the SharePoint Library.**


**2. Navigate to Google Colab for Cleaning and Transformation**
- **[Program Inventory and Expenditure Data Cleaning Notebook](https://colab.research.google.com/drive/1d5DcpU9pPE3S6YncbMMwBcjf7saI8NgW?usp=sharing)** in Google Colab. 
- Google Colab will prompt the user to upload the required Excel files, then clean the files accordingly to the methodology used in this Repository. 
- Once the cleaning process is complete, the user may download the cleaned .csv files


**3. Upload Clean Data to SharePoint**
- Upload the cleaned files to the correct SharePoint folder **clean_data__outputs**, overwriting any pre-existing data and retaining the correct file names. 

![Screenshot of SharePoint Library View](/assets/sharepoint_library_view.png)


**3. Refresh the Dashboard (Optional)**

Once the files are uploaded properly the Dashboard should reflect the update, however if it does not users may refresh the data sources to showcase the new data visualization.


### Dashboard Features

The **[Program Inventory and Expenditure Power BI Dashboard](https://app.powerbigov.us/view?r=eyJrIjoiMTYxNmYxYTgtYjhjZC00YjdhLTliOTItMDY3YmEzODY0ZTczIiwidCI6Ijc4MGM5OGZhLTc3ZDYtNGMwZi05NzJhLTM5YjQ5MGE0ZjY0MSJ9)** will support: 
- Maximum filtering by fiscal year, fund, trend (demand), mandate, service level, risk type, cost recovery, and reliance. 
- Visual Summaries for understanding: 
    - Strategic Goal Alignment
    - Budget by Program and Department
    - Mandated and Service Level Requirements 
    - Cost Breakdown by Capital, O&M, Personnel, Grant, Total Expenditures and Cost Recovery (%)

![Placeholder for Dashboard Embedded View #1](assets/dashboard_view_01.png)

![Placeholder for Dashboard Embedded View #2](assets/dashboard_view_02.png)


## Exploratory Analysis and Key Findings
The notebook **[citydata_02_exploratory.ipynb](https://github.com/breannanpr/CityofMissoulaBudgetCapstone/blob/main/citydata_02_exploratory.ipynb)** dives into the cleaned data to identify patterns, ensure data integrity, and inform both the app and dashboard. The respository notebook contains well docummented narrative and breaks this process into a more detailed step-by-step process. 

Exploratory analysis in general is an essential for validating the success of the cleaning process and surfacing analytical insights before building visualizations. The referenced notebook is summarized as follows:

**Step 1: Load Data**
- Both cleaned CSVs are loaded from our ```cleaned_outputs``` file:
- cleaned_expenditure_status.csv
- cleaned_program_inventory.csv
    - ✅ Column names and data types are verified
    - ✅ Expected shapes: ~2,185 expenditure rows, ~378 program rows
    - ✅ Structure aligns with expectations, no null or corrupted columns


**Steps 2 and 3: Data Structure, Health Checks and Summary Statistics**
- Used ```info()``` and ```.describe()``` to assess completeness and distributions.
- Confirmed all key fields (like ```dept_no, adjusted_appropriation, strategic_goal```) are usable.
- Found most columns to be consistent and free of missing data.
- Visual null-check: ```import missingno as msno``` and ```msno.matrix(df_programs)```
    - Quickly confirms that most columns are complete and suitable for grouping and visualization.


**Step 4: Department Budget Trends**
- Aggregated ```adjusted_appropriation``` by ```department``` to highlight areas of high-spend.
    - 🟢 Findings: Several departments (e.g. Fire, Police, Public Works) dominate the budget allocation.


**Step 5: Program Review**
- Explored how resources are spread across programs
- Grouped by ```strategic_goal_e66_name``` and ```risk_e93_type``` to understand complexity
- 🟡 Insight: Programs tied to housing and infrastructure were most common among strategic alignments.

Example:
```
df_programs['strategic_goal_e66_name'].value_counts().head(10)
```


**Steps 6 through 13: Deeper Dive into Data**
- Budget Allocation Breakdown 
- Mandate, Risk and Trend Distributions
- FTE vs Total Spending 
- Department-level Cost Recovery Overview
- Combined Risk + Mandate Matrix
- Heatmap of Risk and Trend (Demand) 
- Flagging High-Investment and High-Risk Programs


**Summary of Exploratory Insights**
- The cleaning pipeline was validated: no structural errors or major nulls.
- Expenditure is concentrated among a few departments and object types.
- Strategic goals align closely with staffing patterns.
- Risk analysis is a critical lens — high-cost programs often carry operational risks.


## Requirements

To Run locally, Python 3.9+ and the following libraries: 

```
pandas
openpyxl
pyjanitor
matplotlib
missingno
streamlit
```


## Feedback Welcome!
If you'd like to adapt this work to your city or department, feel free to fork the repo or reach out. 
*This work is open for public use under civic good licensing.*


## Appendicies 

### Appendix 1A: Cleaned City Program Inventory Internal Data Collection Data Columns

1. fund: Identifies the financial fund supporting the program.
2. dept_no: formerly "Org" in the pre-cleaned data, Department responsible for the program’s delivery or oversight. 
3. activity: Code linked to a specific function or financial activity in the City's system.
4. program_title_h8: The name of the city-funded service or function, representing a specific output or public-facing activity.
5. requested_title_change_i9: Suggested updates to program titles, submitted by departments.
6. department_h6: Label for the department managing the program.
7. ftes_h36: Full-Time Equivalent employees assigned to the program.
8. personnel_g27: Budget for salaries, benefits, and direct staff compensation.
9. o&m_g28: Operational costs and maintenance-related expenses.
10. debt_g29: Costs related to debt service obligations.
11. grant_g30: Costs related to Grant paid to other organizations.
12. transfers_g31: Transfers between funds or departments.
13. capital_g32: Capital expenditures for infrastructure or equipment.
14. total_expenditures_g33: Sum of all budgeted costs for the program.
15. cost_recovery_e58_yn: Count of program that are or are not offset by revenue sources.
16. cost_recovery_p24_percent: Percent of program costs offset by revenue sources. 
17. description_e12: Written explanation of the program’s purpose and activities, why it exists and how it benefits the community.
18. additional_activities_e20: Notes extra roles, services, or responsibilities.
19. mandate_e41_yn: Indicates whether or not a program is a legal requirement, defined by the entity. Does not include contract-based or optional services. 
20. mandate_h41_entity: Federal, state or court-appointed authority distinguishing value.
21: mandate_e43_descript: Further written description of the mandated rationale
22. service_requirement_e47_yn: Describes whether or not a program has a service requirements or rules imposed by external entities, even if program is not mandated and provies justification.
23. service_requirement_h47_entity: Regulatory agency as defined.
24. service_requirement_e49_descript: Justification for service requirements. 
25. reliance_e53_level: Captures both community dependence and risk of disruption if removed from the community. 
26. reliance_e55_high_descript: High reliance = wide usage, few alternatives, or critical outcomes.
27. strategic_goal_e64_yn: Indicates whether or not a program supports any of the City strategic goals.
28. strategic_goal_e66_name: Name of city goal as they apply. 
29. strategic_goal_e68_action_descript: Description of activites relating to strategic goals. 
30. strategic_goal_e74_additional_activities: Additional field for description informaton about strategic goals. 
31. strategic_goal_e80_2nd_additional_activities: Second additional field for strategic goal descriptions.
32. trend_demand_e87_level: Describes changes in demand or usage over time, indicates whether a programs demand is growing, stable, declining or evolving due to external factors.
33. trend_demand_e89_descript: Provides explanation to pair with the current demand and trend levels. 
34. risk_e93_type: Identifies short-term risks and supporting notes; assesses potential challenges in the next 1-3 years (ex., funding cuts, staffing issues, legal changes).
35. risk_e95_descript: Describes the risk type indicated in greater detail. 


### Appendix 1B: Cleaned Expenditure Status Data Columns 

1. adjusted_appropriation: Final amended budget for each line item. 
2. fund_no: Four digit code for the funding source (General Fund).
3. dept_no: Three digit code for the responsible department.
4. activity_code: Unique six digit code for linking specific programs or services. 
5. object_code: Three digit code categorizing the type of expense. 
6. sub_object_code: Subcategory for further detail within the object code.
7. account_description: Label describing the nature of the expense. 
8. department: full name of the department tied to ```dept_no```. 