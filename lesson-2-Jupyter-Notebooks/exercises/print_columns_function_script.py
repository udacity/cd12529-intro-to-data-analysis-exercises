import pandas as pd


def load_df():
    df = pd.read_csv("census_income_data.csv")
    return df


def print_columns(df):
    for column in df.columns:
        print(column)


if __name__ == "__main__":
    df = load_df()
    print_columns(df)
