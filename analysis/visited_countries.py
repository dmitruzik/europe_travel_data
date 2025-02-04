import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def  analyze_country_visits():
    file_path = "../data/Tourist_travel_Europe.csv"
    df = pd.read_csv(file_path)

    # Count number of visits per country
    country_counts = df["Country_Visited"].value_counts()
    country_counts

    # Find the most visited country
    most_visited_country = country_counts.idxmax()
    most_visited_country

    # Create the bar plot
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x=country_counts.index, y=country_counts.values, palette="viridis")

    # Add labels inside each bar
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2, p.get_height() / 2),  # Centered inside
                    ha='center', va='center', 
                    fontsize=12, color='white', fontweight='bold')

    # Label the chart
    plt.xticks(rotation=45)
    plt.xlabel("Country")
    plt.ylabel("Number of Visits")
    plt.title("Most Visited Countries in Europe (milions)")

    # Show the plot
    plt.show()

