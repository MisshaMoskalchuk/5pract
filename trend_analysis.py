import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

def plot_trend(covid_data, country):
    country_data = covid_data[covid_data['location'] == country]
    
    country_data['date'] = pd.to_datetime(country_data['date'])

    def millions(x, pos):
        return f'{int(x / 1_000_000)}M'

    plt.figure(figsize=(12, 7))
    plt.plot(country_data['date'], country_data['total_cases'], label='Випадки', linewidth=2, color='blue')
    plt.plot(country_data['date'], country_data['total_deaths'], label='Смерті', linewidth=2, color='red')

    plt.title(f'Динаміка захворюваності COVID-19 в {country}', fontsize=16)
    plt.xlabel('Дата', fontsize=12)
    plt.ylabel('Кількість випадків', fontsize=12)
    
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions))
    
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=8))
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))

    plt.xticks(rotation=45, fontsize=10)
    
    plt.legend(fontsize=12)

    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.show()


def top_countries_growth(covid_data):
    covid_data['new_cases'] = covid_data.groupby('location')['total_cases'].diff().fillna(0)
    top_countries = covid_data.groupby('location')['new_cases'].sum().nlargest(100)
    return top_countries
