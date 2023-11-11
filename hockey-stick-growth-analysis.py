import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import ruptures as rpt
import statsmodels.api as sm
import os
from pytrends.request import TrendReq

topics = ["Groupon", "Uber", "Airbnb", "WeWork"]


def get_interest_over_time(topics, timeframe='2007-01-01 2023-01-01'):
    """Fetches Google Trends data for the given topics over the specified timeframe."""
    pytrend = TrendReq()
    interest_over_time_df = pd.DataFrame()

    for topic in topics:
        pytrend.build_payload(kw_list=[topic], timeframe=timeframe)
        topic_df = pytrend.interest_over_time()
        if not topic_df.empty:
            interest_over_time_df[topic] = topic_df[topic]

    return interest_over_time_df


def fit_piecewise_regression(data, x_values, change_points):
    """Fits piecewise regression models to the data at the given change points."""
    models = []
    for start, end in zip([0] + change_points, change_points + [None]):
        segment = data.iloc[start:end]
        x_segment = x_values[start:end]

        if not segment.empty:
            X = sm.add_constant(x_segment)
            model = sm.OLS(segment, X).fit()
            models.append(model)

    return models


def determine_optimal_change_points(data, max_bkps=5, stddev_weight=0.5, length_factor=0.2, constant_factor=1.0):
    """Determines the optimal number of change points for the data."""
    signal = data.dropna().values
    penalty = (data.std() * stddev_weight) * (len(data) ** length_factor) * constant_factor
    algo = rpt.Binseg(model="l2").fit(signal)
    aic_values = [sum(model.aic for model in fit_piecewise_regression(data, np.arange(len(data)),
                                                                      algo.predict(n_bkps=n_bkps))) + penalty * n_bkps
                  for n_bkps in range(1, max_bkps + 1)]

    optimal_n_bkps = aic_values.index(min(aic_values)) + 1
    return algo.predict(n_bkps=optimal_n_bkps)


def plot_interest_change_point(interest_over_time, max_bkps=5, save_dir="graphs"):
    """Plots the interest over time with change points for each topic."""
    os.makedirs(save_dir, exist_ok=True)
    for topic in topics:
        fig, ax = plt.subplots(figsize=(15, 5))
        data = interest_over_time[topic].dropna()
        result = determine_optimal_change_points(data, max_bkps)
        x_values = np.arange(len(data))

        ax.plot(data.index, data.values, label=topic)
        for cp in result[:-1]:
            ax.axvline(x=data.index[cp - 1], color='r', linestyle='--')

        models = fit_piecewise_regression(data, x_values, result)
        for model, cp in zip(models, result):
            start = 0 if models.index(model) == 0 else result[models.index(model) - 1]
            end = cp if models.index(model) != len(models) - 1 else None
            ax.plot(data.index[start:end], model.predict(sm.add_constant(x_values[start:end])), label=f'Reg {models.index(model) + 1}')

        ax.set_title(topic)
        ax.legend()
        fig.savefig(os.path.join(save_dir, f"{topic}_change_point_analysis.png"))
        plt.close(fig)


def plot_composite_interest(interest_over_time, save_dir="graphs"):
    """Plots a composite graph of interest over time for all topics."""
    os.makedirs(save_dir, exist_ok=True)
    plt.figure(figsize=(15, 8))
    for topic in topics:
        plt.plot(interest_over_time[topic].dropna().index, interest_over_time[topic].dropna().values, label=topic)

    plt.title("Composite Google Trends Analysis")
    plt.xlabel("Year")
    plt.ylabel("Interest Over Time")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(save_dir, "composite_interest_analysis.png"))
    plt.close()


def main():
    """Main function to execute the script."""
    interest_over_time = get_interest_over_time(topics)
    plot_interest_change_point(interest_over_time, 5)
    plot_composite_interest(interest_over_time)


if __name__ == "__main__":
    main()
