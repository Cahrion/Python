import matplotlib.pyplot as plt
import numpy as np

# x = [1,2,3,4]
# y = [1,4,9,16]

"""
'[market][line][color]' 
Plotun kullanımı .
"""
"""
# renk ve cizgi büyüklügü degiştirilebilir. # İki cizgi ' cizgi cizgi gösterir.
# plt.plot(x,y, color='red',linewidth="5") # bunun gibi.

plt.plot(x,y,'o--r') 




plt.axis([0,6,0,20]) # [0,6|0,20] ilk taraf x' başlangıç ve bitiş , ikinci taraf y' başlangıç bitiş.

plt.title('Grafik Başlığı')
plt.xlabel('x label')
plt.ylabel('y label')
plt.show()

""""""

x = np.linspace(0,2,100)

plt.plot(x, x,'-r' ,label='linear')
plt.plot(x, x**2,'-y', label='quadratic')
plt.plot(x, x**3,'-g', label='cubic')

plt.title('Simple Plot')
plt.xlabel('x label')
plt.ylabel('y label')

plt.legend()

plt.show()
"""

"""

axs[0].plot(x, x, '-r')
axs[0].set_title('linear')

axs[1].plot(x, x**2, '-g')
axs[1].set_title('quadratic')

axs[2].plot(x, x**3, '-y')
axs[2].set_title('cubic')

plt.tight_layout()
"""
"""
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)
fig.suptitle('grafik başlığı')

axs[0,0].plot(x, x, '-r')
axs[0,0].set_title('linear')

axs[0,1].plot(x, x**2, '-b')
axs[0,1].set_title('quadratic')

axs[1,0].plot(x, x**3, '-g')
axs[1,0].set_title('cubic')

axs[1,1].plot(x, x**4, '-y')
axs[1,1].set_title('Küp')

plt.tight_layout()
"""
import pandas as pd

df = pd.read_csv('nba.csv')

df = df.drop(['Number'], axis = 1).groupby('Team').mean()
df.head().plot(subplots=True)
plt.legend()
plt.show()



plt.show()













