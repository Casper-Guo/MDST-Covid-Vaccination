import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

link_race_ethnicity = "https://github.com/Casper-Guo/MDST-Covid-Vaccination/blob/main/percent_vaccinated_race_ethnicity.xlsx?raw=true"
df_race_ethnicity = pd.read_excel(link_race_ethnicity)

del df_race_ethnicity["Unnamed: 7"]
del df_race_ethnicity["Unnamed: 8"]
del df_race_ethnicity["Unnamed: 9"]
del df_race_ethnicity["Unnamed: 10"]
del df_race_ethnicity["Link"]
del df_race_ethnicity["Date"]

df_race_ethnicity.rename(columns={"State": "STATE"})

df_race_ethnicity.drop(axis=0, index=range(49,54), inplace=True)
df_race_ethnicity.drop(axis=0, index=25, inplace=True)
df_race_ethnicity["State"] = df_race_ethnicity["State"].map(lambda x: x.upper())

pd.set_option("display.max.columns", None)
df_race_ethnicity["Percent Vaccinated, Hispanic"] = df_race_ethnicity["Percent Vaccinated, Hispanic"].fillna(value = 0)
df_race_ethnicity["Percent Vaccinated, Asian"] = df_race_ethnicity["Percent Vaccinated, Hispanic"].fillna(value = 0)

df_race_ethnicity["Percent Vaccinated, White"] *= 100
df_race_ethnicity["Percent Vaccinated, Black"] *= 100
df_race_ethnicity["Percent Vaccinated, Hispanic"] *= 100
df_race_ethnicity["Percent Vaccinated, Asian"] *= 100

abbreviations = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL*', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY*', 'LA', 'ME*', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC*', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV*', 'WI' ]
df_race_ethnicity['Abb'] = abbreviations

#df_race_ethnicity["State"] = df_race_ethnicity["State"].apply(value = states_abbreviations.get(df_race_ethnicity("State")))


print(df_race_ethnicity)

x = df_race_ethnicity["Abb"]
y1 = df_race_ethnicity["Percent Vaccinated, White"]
y2 = df_race_ethnicity["Percent Vaccinated, Black"]
y3 = df_race_ethnicity["Percent Vaccinated, Hispanic"]
y4 = df_race_ethnicity["Percent Vaccinated, Asian"]

plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.bar(x, y3, bottom=y1+y2, color='y')
plt.bar(x, y4, bottom=y1+y2+y3, color='g')

plt.xlabel("STATE")
plt.ylabel("Percent Vaccinated")
plt.legend(["White", "Black", "Hispanic", "Asian"])
plt.title("Percent Vaccinated by Race/Ethnicity")

plt.rcParams["figure.figsize"] = (15,8)

plt.show()
