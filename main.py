import os
from src.data_loader import load_data
from src.preprocess import clean_data
from src import plot_generator as pg

def main():
    # Load data
    filepath = os.path.join("data", "Electric_Vehicle_Population_Data.csv")
    df = load_data(filepath)

    # Preprocess
    df = clean_data(df)

    # Visualizations
    pg.plot_vehicle_type_pie(df)
    pg.plot_county_distribution(df)
    pg.plot_ev_type_bar(df)
    pg.plot_model_year_trend(df)
    pg.plot_cafv_eligibility(df)
    pg.plot_electric_range_hist(df)
    pg.plot_utility_bar(df)

if __name__ == "__main__":
    main()
