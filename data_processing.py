import pandas as pd
import geopandas as gpd

def load_covid_data():
    covid_data_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    return pd.read_csv(covid_data_url)

def load_geodata():
    path_to_geodata = "ne_110m_admin_0_countries.shp"
    return gpd.read_file(path_to_geodata)

def process_data(covid_data, geodata):
    latest_data = covid_data.groupby('location').apply(lambda x: x.loc[x['date'].idxmax()])
    latest_data = latest_data[['location', 'total_cases', 'total_deaths', 'date']]
    latest_data.columns = ['Country', 'Total Cases', 'Total Deaths', 'Date'] 
    merged_data = geodata.merge(latest_data, left_on='ADMIN', right_on='Country', how='left')
    merged_data['Total Cases'] = merged_data['Total Cases'].fillna(0)
    merged_data['Total Deaths'] = merged_data['Total Deaths'].fillna(0)
    return merged_data
