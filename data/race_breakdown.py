
import pandas as pd

link = "https://raw.githubusercontent.com/Casper-Guo/MDST-Covid-Vaccination/main/state_racial_breakdown.csv"
state_racial_breakdown = pd.read_csv(link)

state_racial_breakdown.rename(columns={"State":"STATE"}, inplace=True)
state_racial_breakdown["STATE"] = state_racial_breakdown["STATE"].map(lambda x: x.upper())
