import matplotlib.pyplot as plt
import seaborn as sns

def plot_vehicle_type_pie(df):
    df['Electric Vehicle Type'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.xlabel('')
    plt.ylabel('')
    plt.title('Electric Vehicle Type Distribution')
    plt.tight_layout()
    plt.show()

def plot_county_distribution(df):
    county_counts = df.groupby('County').size().reset_index(name='Electric Vehicle Count')
    county_counts = county_counts.sort_values(by='Electric Vehicle Count', ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    plt.bar(county_counts['County'], county_counts['Electric Vehicle Count'], color='skyblue')
    plt.xlabel('County')
    plt.ylabel('Electric Vehicle Count')
    plt.title('Top 10 Counties by EV Count')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_ev_type_bar(df):
    df['Electric Vehicle Type'].value_counts().plot(kind='bar')
    plt.title('Electric Vehicle Type Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_model_year_trend(df):
    yearly_counts = df.groupby('Model Year').size().reset_index(name='Electric Vehicle Count')
    plt.figure(figsize=(10, 6))
    plt.plot(yearly_counts['Model Year'], yearly_counts['Electric Vehicle Count'], marker='o', color='red')
    plt.xlabel('Model Year')
    plt.ylabel('Electric Vehicle Count')
    plt.title('EV Trend Over Time')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_cafv_eligibility(df):
    eligibility_counts = df.groupby('Clean Alternative Fuel Vehicle (CAFV) Eligibility').size()
    plt.figure(figsize=(8, 6))
    eligibility_counts.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'orange', 'lightcoral'])
    plt.title('CAFV Eligibility Distribution')
    plt.ylabel('')
    plt.show()

def plot_electric_range_hist(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Electric Range'], bins=20, kde=True, color='red')
    plt.xlabel('Electric Range (miles)')
    plt.ylabel('Frequency')
    plt.title('Electric Range Distribution')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_utility_bar(df):
    utility_counts = df['Electric Utility'].value_counts().head(7)
    plt.figure(figsize=(10, 6))
    utility_counts.plot(kind='bar', color='skyblue')
    plt.xlabel('Electric Utility Provider')
    plt.ylabel('Number of Electric Vehicles')
    plt.title('EV Count by Utility Provider')
    plt.xticks(rotation=45, ha='right')
    plt.show()
