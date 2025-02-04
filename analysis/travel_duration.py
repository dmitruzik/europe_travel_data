import pandas as pd
import matplotlib.pyplot as plt

def analyze_travel_duration():
    file_path = "./data/Tourist_Travel_Europe.csv"
    df = pd.read_csv(file_path)

    # Calculate average travel duration per country
    avg_duration_per_country = df.groupby("Country_Visited")["Travel_Duration_Days"].mean().reset_index()

    # Calculate the total average travel duration
    total_avg_duration = df["Travel_Duration_Days"].mean()

    # Sort the data for better visualization
    avg_duration_per_country = avg_duration_per_country.sort_values(by="Travel_Duration_Days", ascending=False)

    # Create a bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(avg_duration_per_country["Country_Visited"], avg_duration_per_country["Travel_Duration_Days"])
    plt.xlabel("Country")
    plt.ylabel("Average Travel Duration (Days)")
    plt.title("Average Travel Duration per Country")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Show the plot
    plt.show()

