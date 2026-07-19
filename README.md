# COVID-19 Global Trend Analysis – Data Analytics Project

## Overview
This project analyzes the global spread of COVID-19 using daily country-level case data spanning January 22, 2020 to July 27, 2020. The goal is to track infection trends, compare regional impact, and uncover patterns in confirmed cases, deaths, recoveries, and active cases to support public health monitoring and reporting. The workflow covers the full analytics lifecycle: data cleaning in Python, storage and querying in MySQL, visualization in Power BI, and a summary report and presentation for stakeholders.

## Dataset
- **Rows:** 49,068
- **Columns:** 10
- **Coverage:** 187 countries across 6 WHO regions (Africa, Americas, Eastern Mediterranean, Europe, South-East Asia, Western Pacific)
- **Key features:**
  - Location details — Province/State, Country/Region, Lat, Long, WHO Region
  - Time series — Date (daily records, Jan 22 – Jul 27, 2020)
  - Case metrics — Confirmed, Deaths, Recovered, Active
- **Missing data:** 34,404 values in Province/State (structural — most countries don't report at province level, not an error)

## Tools Used
| Category         | Tool                     |
|-------------------|---------------------------|
| Data Cleaning     | Python (pandas)           |
| Database          | MySQL / MySQL Workbench (via SQLAlchemy) |
| Querying          | SQL                       |
| Visualization     | Power BI                  |
| Reporting         | Word / PDF                |
| Presentation      | Gamma (AI-generated PPT)  |

## Steps

### 1. Data Loading & EDA (Python)
- Imported the dataset using pandas
- Used `df.head()`, `df.info()`, and `df.describe()` to check structure and summary statistics

### 2. Data Cleaning (Python)
- **Missing data handling** — checked nulls with `df.isnull().sum()`; filled missing Province/State values with the corresponding Country/Region
- **Column standardization** — renamed columns to snake_case (spaces/slashes replaced, lowercased)
- **Duplicate check** — verified no duplicate rows existed
- **Date formatting** — converted the date column to datetime, then reformatted to dd/mm/yyyy
- **Data consistency check** — identified negative values in the `active` column caused by inconsistent source reporting; recalculated `active = confirmed - deaths - recovered` and clipped remaining negatives to 0
- **Category validation** — confirmed 187 unique countries and reviewed the 6 WHO region categories for consistency
- Loaded the cleaned DataFrame into a `covid_19` MySQL database via SQLAlchemy

### 3. SQL Analysis (MySQL)
Ran 10 analytical queries covering:
1. Top 10 countries by confirmed cases
2. Top 10 countries by deaths
3. Global case summary (latest date) — confirmed, recovered, active, deaths
4. WHO region with highest confirmed cases
5. Countries with over 100,000 confirmed cases
6. Mortality rate by country (Deaths ÷ Confirmed × 100)
7. Recovery rate by country (Recovered ÷ Confirmed × 100)
8. Countries with highest active case load
9. Country count by WHO region
10. Daily trend of confirmed cases worldwide

## Dashboard (Power BI)
Built an interactive Power BI dashboard to visualize global case trends, regional comparisons, and country-level breakdowns.
(https://github.com/arindam-09/Covid-19-Analysis/blob/main/Dashboard.PNG)

## Results & Recommendations
- **Focus resources on high-burden regions** — direct medical support to WHO regions/countries with the highest confirmed and active cases
- **Track mortality rate closely** — countries with high death rates need stronger healthcare response and faster treatment
- **Monitor active case trends daily** — watch countries with rising active cases to catch new outbreaks early
- **Learn from high recovery countries** — study and replicate strategies from countries with strong recovery rates
- **Prepare for regional spikes** — use WHO region breakdowns to plan ahead for likely surge areas
- **Keep data updated regularly** — refresh the dashboard often since case numbers change daily

## How to Run
1. Clone this repository
   ```bash
   git clone <repo-url>
   ```
2. Install Python dependencies
   ```bash
   pip install pandas sqlalchemy mysql-connector-python
   ```
3. Run the cleaning script
   ```bash
   python clean_data.py
   ```
4. Load the cleaned data into MySQL (via the SQLAlchemy connection in the script, or manually import the CSV)
5. Run SQL queries from `queries.sql` in MySQL Workbench
6. Open `dashboard.pbix` in Power BI Desktop to view/interact with the dashboard
7. Refer to `report.pdf` for the written summary and `presentation.pdf`/Gamma link for the PPT

## Project Structure
```
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
├── clean_data.py
├── queries.sql
├── dashboard.pbix
├── report.pdf
└── README.md
```

## Author
Arindam Talukdar
(https://github.com/arindam-09)
linkedin.com/in/arindam-talukdar
