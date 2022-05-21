import pandas
import seaborn
from numpy import split
from pandas import DataFrame


# Данные
taxis: DataFrame = seaborn.load_dataset('taxis')


# ищем улицу с самым большим количество людей
street_to_passengers_amount = {}
for t in taxis.values:
    pickup_zone = t[-4]  # from street
    dropoff_zone = t[-3]  # to street
    if pickup_zone in street_to_passengers_amount:
        street_to_passengers_amount[pickup_zone] += 1
    else:
        street_to_passengers_amount[pickup_zone] = 0
    if dropoff_zone in street_to_passengers_amount:
        street_to_passengers_amount[dropoff_zone] += 1
    else:
        street_to_passengers_amount[dropoff_zone] = 0
big_street: str = sorted(
    [(street, passengers_amount) for street, passengers_amount in street_to_passengers_amount.items()],
    key=lambda d: d[1],
    reverse=True
)[0][0]


# фильтруем
taxis = taxis.query(f"pickup_zone == '{big_street}' or dropoff_zone == '{big_street}'")


# создание таблицы
table = taxis.pivot_table(
    index='passengers',
    columns='passengers'
)
table.to_excel('./table.xlsx')
