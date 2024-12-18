from data_processing import load_covid_data, load_geodata, process_data
from map_visualization import static_map, interactive_map
from trend_analysis import plot_trend, top_countries_growth

def main():
    
    covid_data = load_covid_data()
    geodata = load_geodata()
    merged_data = process_data(covid_data, geodata)
    
    static_map(merged_data)
    interactive_map(merged_data)
    
    plot_trend(covid_data, 'Ukraine')
    print(top_countries_growth(covid_data))

if __name__ == "__main__":
    main()
