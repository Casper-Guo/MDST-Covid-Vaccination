import pandas as pd

df_raw = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/rolling-averages/us-states.csv')
state_cases = df_raw.rename(columns={'state': 'STATE'})
state_cases['STATE'] = state_cases.STATE.map(str.upper)