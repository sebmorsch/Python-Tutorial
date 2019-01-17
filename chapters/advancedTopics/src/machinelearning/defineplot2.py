# Plot definieren
fig = pyplot.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot mit Daten versorgen
ax.scatter(dataSet[:,0], dataSet[:,1], dataSet[:,2],
	marker ='o', color=classColorVector)
	
# Achsenbeschriftungen festlegen
ax.set_xlabel("X-Label")
ax.set_ylabel("Y-Label")
ax.set_zlabel("Z-Label")

# Achsenskala festlegen
ax.set_xlim(xmin=0)
ax.set_ylim(ymin=0)
ax.set_zlim(zmin=0)

# Plot anzeigen
pyplot.show()