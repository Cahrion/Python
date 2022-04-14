import matplotlib.pyplot as plt
import numpy as np


goal_types = 'Yapıldı','Yapılıyor'

goals = [65,35]
colors= ['b','g']

plt.pie(goals,labels=goal_types,colors=colors, shadow=True, explode=(0.05,0.05), autopct='%1.1f%%')

plt.title('Python (İLERİ SEVİYE)')
plt.show()


