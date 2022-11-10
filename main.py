import numpy as np
import matplotlib.pyplot as plt

# Parameters
size = 25
state_limit = 3
neighbor = [
	(+1, 0),
	(-1, 0),
	(0, +1),
	(0, -1),
]

plt.figure()
field = 0 * np.random.randint(0, state_limit+1, (size, size))
while True:

	i, j = np.random.randint(0, size, 2)

	field[i, j] += 1

	i_us, j_us = np.where(field > state_limit)

	while len(i_us) > 0:

		index = np.random.randint(len(i_us))

		field[i_us[index], j_us[index]] = field[i_us[index], j_us[index]] - (state_limit + 1)

		for ij_ in neighbor:
			i_ = i_us[index] + ij_[0]
			j_ = j_us[index] + ij_[1]

			if 0 <= i_ < size and 0 <= j_ < size:
				field[i_, j_] += 1

		i_us, j_us = np.where(field > state_limit)

		plt.cla()
		plt.imshow(field, interpolation="nearest", cmap="gray")
		plt.clim(0, state_limit+1)
		plt.pause(0.00001)
