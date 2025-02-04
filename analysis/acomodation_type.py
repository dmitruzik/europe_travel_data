import pandas as pd
import matplotlib.pyplot as plt

def analyze_accomodation_type():
    file_path = "./data/Tourist_Travel_Europe.csv"
    df = pd.read_csv(file_path)

    accomodation_counts = df['Accommodation_Type'].value_counts()

    most_popular_accomodation= accomodation_counts.idxmax()

    plt.figure(figsize=(8, 8))  
    plt.pie(
        accomodation_counts, 
        labels=accomodation_counts.index,  
        autopct='%1.1f%%',  
        startangle=140,  
        colors=['green', 'purple', 'red', 'yellow']  
    )
    plt.title("Most Popular accomodation types")  
    plt.show()  
    