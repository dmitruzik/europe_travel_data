import pandas as pd
import matplotlib.pyplot as plt

def analyze_season():
  file_path = "./data/Tourist_Travel_Europe.csv"
  df = pd.read_csv(file_path)

  season_counts = df['Season_of_Visit'].value_counts()

  most_popular_season = season_counts.idxmax()

  plt.figure(figsize=(8, 8))  
  plt.pie(
      season_counts, 
      labels=season_counts.index,  
      autopct='%1.1f%%',  
      startangle=140,  
      colors=['blue', 'green', 'red', 'orange']  
  )
  plt.title("Most Popular Travel Seasons")  
  plt.show()  


