import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_city_visits():
    file_path = "../data/Tourist_travel_Europe.csv"
    df = pd.read_csv(file_path)

    # Count visits per city
    city_counts = df["City_Visited"].value_counts()

    # Find the most visited city
    most_visited_city = city_counts.idxmax()

    # Create the bar plot
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(
        x=city_counts.index[:10], 
        y=city_counts.values[:10], 
        hue=None,  # Explicitly set hue to None
        palette="magma", 
        legend=False  # Disable legend
    )

    # Add labels inside each bar
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2, p.get_height() / 2),  # Centered inside
                    ha='center', va='center', 
                    fontsize=12, color='blue', fontweight='bold')

    # Label the chart
    plt.xticks(rotation=45)
    plt.xlabel("City")
    plt.ylabel("Number of Visits")
    plt.title("Top 10 Most Visited Cities in Europe")

    # Show the plot
    plt.show()

