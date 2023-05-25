import pandas as pd
import matplotlib.pyplot as plt


def load_df():
    df = pd.read_csv("census_income_data.csv")
    return df


def plot_hist(arr1, arr2, label1, label2):
    ax = arr1.hist(color="r", alpha=0.5)
    ax = arr2.hist(color="b", alpha=0.5, ax=ax)
    ax.legend([label1, label2])
    plt.savefig("hist.png")


if __name__ == "__main__":
    df = load_df()
    below = df.query('income == " <=50K"')
    above = df.query('income == " >50K"')
    plot_hist(below.age, above.age, "<=50K", ">50K")
