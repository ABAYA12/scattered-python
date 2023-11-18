from datetime import datetime as dt
import matplotlib.pyplot as plt
even_numbers = [2, 4, 6, 8, 10]
squares = [4, 16, 36, 64, 100]
plt.scatter(even_numbers, squares, s=10)
# Set chart title and label axes.
plt.title("Square of Even Numbers", fontsize=24)
plt.xlabel("Even Numbers", fontsize=14)
plt.ylabel("Corresponding Squares", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()


today = dt.now()
print(today)
