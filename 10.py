import seaborn
from pandas import DataFrame
import matplotlib.pyplot as plt


penguins: DataFrame = seaborn.load_dataset("penguins")
seaborn.countplot(x="species", data=penguins)
plt.show()  # график

