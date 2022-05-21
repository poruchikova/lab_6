import pandas as pd
import requests as requests


DOWNLOAD_PATH = './gspc.csv'
API_KEY = 'hgg2bwdphgwdhnnxsdchsgjyxqjjh3'
EXCEL_PATH = './res.xlsx'


# используем для скачивания requests, потому что pandas это делает неправильно
response = requests.get(f'https://query.data.world/s/{API_KEY}')
print(f'{DOWNLOAD_PATH} downloaded')
open(DOWNLOAD_PATH, mode='wb').write(response.content)

# работа с данными
gspc = pd.read_csv(DOWNLOAD_PATH)
gspc.set_index("Date")
gspc = gspc.assign(Number=gspc.Open / gspc.Close)
gspc = gspc.assign(Coeff=gspc.Volume / gspc.Number)
gspc.to_excel(EXCEL_PATH)
