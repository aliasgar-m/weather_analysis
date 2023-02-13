# Date: MM-DD-YYYY              ;    Average Windspeed: (mph) float ;
# Temperature: (F) float        ;    Average Gustspeed: (mph) float ;
# Average Humidity: (%) float   ;    Average Direction: (deg) float ;
# Average Dewpoint: (F) float   ;    Rainfall for month: (in) float ;
# Average Barometer: (in) float ;    Rainfall for year: (in) float  ;

# Maximum pressure: (bar) float   ;   Diff_pressure: (bar) float     ;
# Maximum temperature: (F) float  ;   Minimum pressure: (bar) float  ;
# Minimum temperature: (F) float  ;   Maximum windspeed: (mph) float ;
# Maximum humidity: (%) float     ;   Maximum gustspeed: (mph) float ;
# Minimum humidity: (%) float     ;   Maximum heat index: (F) float  ;

# Maximum rain per minute:

import pandas as pd


class preprocessData:
    def __init__(self, raw_data: pd.DataFrame) -> None:
        self.initial_raw_data = raw_data

    def run(self) -> None:
        self.remove_null_values()
        self.convert_column_name()
        self.save_cleaned_dataset()
        # self.insight()

    def remove_null_values(self) -> None:
        self.initial_raw_data.dropna(axis=1, how="all", inplace=True)
        self.initial_raw_data.dropna(axis=0, how="all", inplace=True)

    def convert_column_name(self) -> None:
        new_cols_names = ['Date', 'Temperature', 'Avg_humidity', 'Avg_dewpoint',
                          'Avg_barometer', 'Avg_windspeed', 'Avg_gustspeed',
                          'Avg_direction', 'Rainfall_month', 'Rainfall_year',
                          'Max_rain_per_minute', 'Max_temperature', 'Min_temperature',
                          'Max_humidity', 'Min_humidity', 'Max_pressure',
                          'Min_pressure', 'Max_windspeed', 'Max_gustspeed',
                          'Max_heat_index', 'diff_pressure']

        self.initial_raw_data = self.initial_raw_data.set_axis(new_cols_names, axis=1, copy=False)

    def save_cleaned_dataset(self) -> None:
        self.initial_raw_data.to_csv(r"assets/cleaned_weather_dataset.csv", header=True, index=False)

    def insight(self) -> None:
        print(self.initial_raw_data.columns)
        print(self.initial_raw_data.describe())
        print(self.initial_raw_data.info())
        print(self.initial_raw_data.head())
        print(self.initial_raw_data.isnull().sum())


def main():
    raw_dataset = pd.read_csv(r"assets/raw_weather_dataset.csv")
    preprocessor = preprocessData(raw_dataset)
    preprocessor.run()


if __name__ == "__main__":
    main()
