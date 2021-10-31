
import pandas as pd

link = "https://raw.githubusercontent.com/Casper-Guo/MDST-Covid-Vaccination/main/education_clean.csv"
state_education = pd.read_csv(link)

print(state_education.head())