import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta

from constants import KAWASANKU_CENSUS_DISTRICT
from constants_secret import TOKEN_CHANNEL_AKSARA

from helper import download_csv, telegram_msg, telegram_image


# download data
status = download_csv(src=KAWASANKU_CENSUS_DISTRICT, save_as='data/census_district.csv')
telegram_msg(msg=status, conf=TOKEN_CHANNEL_AKSARA)

# manipulate data
df = pd.read_csv('data/census_district.csv', usecols=['state','year','population_total'])
df = df.groupby('year').sum().reset_index()
df.columns = ['year','population']
df.population = df.population.astype(int)



fig, ax = plt.subplots()
ax.set_title(f'Census Population in Malaysia')
df.plot(x ='year', y=['population'], kind="bar", ax=ax)
plt.savefig('charts/census_trend.png')

    # send chart
telegram_image(src='charts/census_trend.png',
               caption='Census Population in Malaysia',
               conf=TOKEN_CHANNEL_AKSARA)
