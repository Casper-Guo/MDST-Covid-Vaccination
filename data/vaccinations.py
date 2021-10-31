import pandas as pd

raw_df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv")
state_vacc = raw_df.dropna().rename(columns={'location': 'STATE'})