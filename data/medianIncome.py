
import pandas as pd

link = "https://raw.githubusercontent.com/Casper-Guo/MDST-Covid-Vaccination/main/medianIncomeByState2019.csv"
state_median_income = pd.read_csv(link)

state_median_income["Median Annual Household Income"] = state_median_income["Median Annual Household Income"].map(lambda x: int(x.replace(',', '')[1:]))
