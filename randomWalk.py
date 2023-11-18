from plot4 import RandonWalk
import matplotlib.pyplot as plt

rw = RandonWalk(50000)
rw.fill_walks()

plt.plot(rw.x_values, rw.y_values)
plt.figure(figsize=(10, 6))
plt.grid(True)
plt.show()
