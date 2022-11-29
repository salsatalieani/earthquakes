# Importing auxiliary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Extracting earthquakes data

df = pd.read_csv('C:/Users/salsa/Documents/IEB_export.csv')

lat = df['Lat']
lon = df['Lon']
depth = df['Depth']
magnitude = df['Mag']

# Drawing the map background

fig = plt.figure(figsize=(10, 10))
m = Basemap(projection='lcc', resolution='h', 
            lat_0=-6, lon_0=105,
            width=10E6, height=5E6)
m.bluemarble()
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')
m.drawstates(color='gray')

# Scattering data, with color reflecting depth and size reflecting magnitude

m.scatter(lon, lat, latlon=True,
          c=depth, s=magnitude**3,
          cmap='autumn', alpha=0.5)

# Creating colorbar and legend

plt.colorbar(label=r'$\rm Depth (meter)$')
plt.clim(10, 550)

# Making legend with dummy points

for a in [3, 4, 5, 6]:
    plt.scatter([], [], c='y', alpha=0.5, s=a**3,
                label=str(a))
leg = plt.legend(scatterpoints=1, frameon=False,
           labelspacing=1, loc='lower left')
for text in leg.get_texts():
    text.set_color("white")

# Setting up the graph

plt.title('Earthquakes in Indonesia on October-November 2022', fontsize=16, pad=20)
plt.xlabel('Longitude', fontsize=14)
plt.ylabel('Latitude', fontsize=14)

# Showing map result

plt.show()

