import pandas as pd
import matplotlib.pyplot as plt

def analyze_travel_cost():
    file_path = "./data/Tourist_Travel_Europe.csv"
    df = pd.read_csv(file_path)

    total_cost_per_country = df.groupby("Country_Visited")["Total_Travel_Cost"].sum().reset_index()

    # Calculate average travel cost per country
    avg_cost_per_country = df.groupby("Country_Visited")["Total_Travel_Cost"].mean().reset_index()

    # Calculate overall total and average travel cost
    total_travel_cost = df["Total_Travel_Cost"].sum()
    average_travel_cost = df["Total_Travel_Cost"].mean()

    total_cost_per_country = total_cost_per_country.sort_values(by="Total_Travel_Cost", ascending=False)
    plt.figure(figsize=(12, 6))
    bars = plt.bar(total_cost_per_country["Country_Visited"], total_cost_per_country["Total_Travel_Cost"], color='skyblue')

    plt.xlabel("Country")
    plt.ylabel("Total Travel Cost (£)")
    plt.title("Total Travel Cost per Country")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Add labels inside bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval - (yval * 0.1), f"£{yval:,.0f}", ha="center", va="top", fontsize=10, color="black")

    # Show the plot
    plt.show()

    # Sort data for better visualization
    avg_cost_per_country = avg_cost_per_country.sort_values(by="Total_Travel_Cost", ascending=False)

    # Plot average travel cost per country
    plt.figure(figsize=(12, 6))
    bars = plt.bar(avg_cost_per_country["Country_Visited"], avg_cost_per_country["Total_Travel_Cost"], color='lightcoral')

    plt.xlabel("Country")
    plt.ylabel("Average Travel Cost (£)")
    plt.title("Average Travel Cost per Country")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Add labels inside bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval - (yval * 0.1), f"£{yval:,.0f}", ha="center", va="top", fontsize=10, color="black")

    # Show the plot
    plt.show()
