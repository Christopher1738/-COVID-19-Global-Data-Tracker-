COVID-19 GLOBAL DATA TRACKER
============================

A Python-based data analysis project tracking pandemic metrics across countries.

REQUIREMENTS
------------
- Python 3.8+
- Required packages:
  pandas, numpy, matplotlib, seaborn, plotly

INSTALLATION
------------
1. Clone this repository
2. Install dependencies:
   pip install -r requirements.txt

USAGE
-----
Run the analysis script:
   python covid19_tracker.py

This will generate:
1. cases_by_country.png - Case trends visualization
2. vaccinations.png - Vaccination progress charts
3. vaccine_map.html - Interactive world map

DATA SOURCE
-----------
Our World in Data COVID-19 Dataset:
https://covid.ourworldindata.org/data/owid-covid-data.csv

PROJECT STRUCTURE
-----------------
covid19_tracker.py - Main analysis script
requirements.txt - Dependency list
/output/ - Generated reports and visualizations

KEY METRICS ANALYZED
--------------------
- Total cases/deaths over time
- Vaccination rates
- Country comparisons
- Death rate calculations

CONTACT
-------
For questions or contributions, please open an Issue.

NOTE
----
This is an educational project. Refer to official health authorities for medical guidance.
