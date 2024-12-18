import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.ticker import FuncFormatter

def static_map(merged_data):
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    merged_data.plot(column='Total Cases', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    cbar = ax.get_figure().get_axes()[1]
    cbar.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x / 1_000_000)}M'))
    ax.set_title('Кількість випадків COVID-19 по країнах', fontsize=15)
    plt.show()

def interactive_map(merged_data):
    fig = px.choropleth(
        merged_data,
        locations="Country",
        locationmode="country names",
        color="Total Cases",
        hover_name="Country",
        hover_data={"Total Cases": ":,.0f", "Total Deaths": ":,.0f"},
        title="Кількість випадків COVID-19 по країнах",
        color_continuous_scale="OrRd",
        labels={'Total Cases': 'Випадки', 'Total Deaths': 'Смерті'}
    )
    fig.show()
