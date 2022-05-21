import matplotlib.pyplot as plt
import seaborn
from pandas import DataFrame

penguins: DataFrame = seaborn.load_dataset("penguins")
seaborn.countplot(x="species", data=penguins)
plt.show()  # график

