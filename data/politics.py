import pandas as pd

raw_df = pd.read_csv('https://raw.githubusercontent.com/Casper-Guo/MDST-Covid-Vaccination/main/state-political-identification.csv')

state_parties = raw_df \
    .rename({'Unnamed: 0': 'STATE'}, axis=1) \
    .drop(['Unnamed: 3', 'Unnamed: 4'], axis=1) \
    .dropna()

state_parties["STATE"] = state_parties["STATE"].map(lambda x: x.upper())
