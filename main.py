import csv
import numpy as np

with open("tips.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  data_numpy = np.array(data_list)

size = data_numpy[:,6]
tips = np.array(data_numpy[:,1], dtype = float)
bills = np.array(data_numpy[:,0], dtype = float)
tip_percentages = tips/bills

print(f"The average bill amount is: ${round(np.mean(bills), 2)}")

print(f"The median bill amount is: ${round(np.median(bills), 2)}")

print(f"The minimum bill amount is: ${round(np.min(bills), 2)}")

print(f"The largest bill amount is: ${round(np.max(bills), 2)}")

import matplotlib.pyplot as plt
plt.scatter(size, tip_percentages, color ="#4B0082")
plt.xlabel("Dinner Party Size")
plt.ylabel("Tip Percentage")
plt.title("Tips and Group Size")
plt.savefig("tipsandgroupsize.png")