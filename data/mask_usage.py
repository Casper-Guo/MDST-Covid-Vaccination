import pandas as pd

raw_df = pd.read_csv('https://raw.githubusercontent.com/Casper-Guo/MDST-Covid-Vaccination/main/covid_mask_usage_by_state.csv')
state_masks = raw_df.rename(columns={'State': 'STATE'})
state_masks['STATE'] = state_masks['STATE'].map(str.upper)