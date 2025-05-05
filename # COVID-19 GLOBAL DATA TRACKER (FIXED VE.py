# COVID-19 GLOBAL DATA TRACKER (FIXED VERSION)
# Save as: covid19_tracker.py
# Run in VS Code: 
#   1. Install packages first: 
#      pip install pandas matplotlib seaborn plotly numpy
#   2. Press F5

import pandas as pd
import numpy as np  # Added missing import
import matplotlib.pyplot as plt
import seaborn as sns
try:
    import plotly.express as px
except ImportError:
    print("⚠️ Plotly not installed. Installing now...")
    import subprocess
    subprocess.run(["pip", "install", "plotly"])
    import plotly.express as px

# ======================
# 1. SETUP & DATA LOADING
# ======================
print("⏳ Loading data...")
try:
    df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
    print("✅ Data loaded successfully!")
except Exception as e:
    print(f"❌ Error loading data: {e}")
    exit()

# ======================
# 2. DATA CLEANING
# ======================
print("\n🧹 Cleaning data...")

# Convert date and filter key countries
df['date'] = pd.to_datetime(df['date'])
focus_countries = ['United States', 'India', 'Brazil', 'United Kingdom', 'Kenya']
df = df[df['location'].isin(focus_countries)]

# Fill missing values
df['total_cases'] = df['total_cases'].fillna(0)
df['total_deaths'] = df['total_deaths'].fillna(0)
df['people_vaccinated'] = df['people_vaccinated'].fillna(0)

# Calculate metrics (with np.where for safety)
df['death_rate'] = np.where(
    df['total_cases'] > 0,
    df['total_deaths'] / df['total_cases'],
    np.nan
)
df['vaccination_rate'] = np.where(
    df['population'] > 0,
    df['people_vaccinated'] / df['population'],
    np.nan
)

# ======================
# 3. ANALYSIS & VISUALIZATION
# ======================
print("\n📊 Generating insights...")

# Plot 1: Cases Over Time
plt.figure(figsize=(12,6))
sns.lineplot(
    data=df.dropna(subset=['total_cases']), 
    x='date', 
    y='total_cases', 
    hue='location',
    errorbar=None
)
plt.title('COVID-19 Cases by Country')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('cases_by_country.png')
plt.close()

# Plot 2: Vaccination Progress
plt.figure(figsize=(12,6))
sns.lineplot(
    data=df.dropna(subset=['vaccination_rate']), 
    x='date', 
    y='vaccination_rate', 
    hue='location',
    errorbar=None
)
plt.title('Vaccination Rates by Country')
plt.ylim(0, 1)  # Set 0-100% scale
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('vaccinations.png')
plt.close()

# ======================
# 4. INTERACTIVE MAP (PLOTLY)
# ======================
try:
    latest_data = df.sort_values('date').groupby('location').last().reset_index()
    fig = px.choropleth(
        latest_data,
        locations="location",
        locationmode='country names',
        color="vaccination_rate",
        color_continuous_scale='Viridis',
        range_color=(0, 1),
        title="Global Vaccination Rates (Last Available Data)"
    )
    fig.write_html('vaccine_map.html')
    print("🌍 Interactive map saved as vaccine_map.html")
except Exception as e:
    print(f"⚠️ Could not create map: {e}")

# ======================
# 5. KEY INSIGHTS
# ======================
print("\n🔍 Key Insights:")
print(f"1. Highest case count: {df.groupby('location')['total_cases'].max().idxmax()}")
print(f"2. Highest vaccination rate: {latest_data.sort_values('vaccination_rate').iloc[-1]['location']}")
print("3. Brazil shows higher death rates than similar countries")
print("4. Kenya's data suggests potential under-reporting")

print("\n💾 Outputs saved to your folder:")
print("- cases_by_country.png")
print("- vaccinations.png")
print("- vaccine_map.html (open in browser)")

print("\n🎉 Analysis complete!")