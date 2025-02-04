import pandas as pd
import matplotlib.pyplot as plt


file_path = "./data/Tourist_Travel_Europe.csv"
df = pd.read_csv(file_path)

purpose_per_country = df.groupby(["Country_Visited", "Main_Purpose"]).size().unstack().fillna(0)

# Create a stacked bar chart
fig, ax = plt.subplots(figsize=(12, 6))
purpose_per_country.plot(kind="bar", stacked=True, colormap="tab10", ax=ax)

plt.xlabel("Country")
plt.ylabel("Number of Travelers")
plt.title("Travel Purposes per Country")
plt.xticks(rotation=45)
plt.legend(title="Main Purpose")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Add labels inside the bars
for container in ax.containers:
    for bar in container:
        height = bar.get_height()
        if height > 0: 
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_y() + height / 2, 
                f"{int(height)}",
                ha="center",
                va="center",
                fontsize=10,
                color="white",
                fontweight="bold"
            )
plt.show()
