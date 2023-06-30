def throw_darts(num_points):

# Hier werfen wir "Darts" und zählen die Anzahl der Treffer

	points = []
	hits = 0
	
	import random

	for _ in range(num_points):
		x, y = random.random(), random.random()

		if x*x + y*y < 1.0:
			hits += 1
			points.append((x, y, "red"))
		else:
			points.append((x, y, "blue"))

	return hits, points


def visualize(points):

	import matplotlib.pyplot as plt

	# unzip points into 3 lists
	x, y, colors = zip(*points)

	# define figure dimensions
	fig, ax = plt.subplots()
	fig.set_size_inches(6.0, 6.0)

	# plot results
	ax.scatter(x, y, c=colors)