import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn

API_KEY = 'hgg2bwdphgwdhnnxsdchsgjyxqjjh3'
DOWNLOAD_PATH = './gspc.csv'


# используем для скачивания requests, потому что pandas это делает неправильно
response = requests.get(f'https://query.data.world/s/{API_KEY}')
print(f'{DOWNLOAD_PATH} downloaded')
open(DOWNLOAD_PATH, mode='wb').write(response.content)

# работа с данными
gspc = pd.read_csv(DOWNLOAD_PATH)
gspc.set_index("Date")
gspc_to_graph = gspc.assign(HighG=gspc.High + (.05 * gspc.Close))
gspc_to_graph = gspc_to_graph.assign(LowG=gspc.Low - (.05 * gspc.Close))
seaborn.set_style("darkgrid")
plot1 = seaborn.barplot(x="Date", y="HighG", data=gspc_to_graph)
plot2 = seaborn.barplot(x="Date", y="LowG", data=gspc_to_graph)
plot1.savefig("plot2", bbox_inches="tight")
plot2.savefig("plot1", bbox_inches="tight")
plt.show()
