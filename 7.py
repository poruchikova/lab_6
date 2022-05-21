import matplotlib.pyplot as plt
import numpy
import seaborn
from pandas import DataFrame

planets: DataFrame = seaborn.load_dataset("planets")
print(planets.groupby(["method", "number"], as_index=False).agg({"value": numpy.mean}))
seaborn.countplot(x="method", data=planets)
plt.show()  # график
