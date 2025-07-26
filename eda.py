import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def main():
    #get filepaths to data
    player_path = "contestant_table.csv"
    season_path = "season_table.csv"
    tribe_path = "tribe_table.csv"

    #load data
    player_data = load_data(player_path)
    season_data = load_data(season_path)
    tribe_data = load_data(tribe_path)

    print(player_data.head())
    print(season_data.head())
    print(tribe_data.head())

if __name__ == "__main__":
    main()


