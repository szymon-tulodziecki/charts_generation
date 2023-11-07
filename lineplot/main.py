import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('dane.csv')
sns.lineplot(data=data, x="Hz", y="mA")
plt.xlabel("Hz")
plt.ylabel("mA")
plt.title("Wykres Zależności Częstotliwości od Natężenia Prądu")
plt.show()
