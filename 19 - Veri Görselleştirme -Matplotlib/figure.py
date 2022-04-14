import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2



"""
figure = plt.figure()

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8]) # Soldan,|,alttan,|,genişlik,|,Uzunluk| Unutma düzlem 1'e 1'lik

axes_cube.plot(x,y,'b')
axes_cube.set_xlabel('X axis')
axes_cube.set_ylabel('Y axis')
axes_cube.set_title('Cube')

axes_square = figure.add([0.15,0.6,0.25,0.25])
axes_square.plot(x,z,'r')
axes_square.set_xlabel('X axis')
axes_square.set_ylabel('Z axis')
axes_square.set_title('Seuare')
"""

"""
figure = plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x,z, label='Square')
axes.plot(x,y, label='Cube')

axes.legend(loc=4)

plt.show()
"""

fig,axes = plt.subplots(2,1,figsize=(4,4))

axes[0].plot(x,y)
axes[0].set_title('Cube')
axes[1].plot(x,z)
axes[1].set_title('Square')

plt.tight_layout()
fig.savefig('figure1.pdf')


plt.show()
