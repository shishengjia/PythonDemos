import matplotlib.pyplot as plt
import numpy as np
"""
In 2004-2005, Geniant assisted JHA with the development of a pilot project to construct the 
frame- work for its SOA implementation.
"""
fig, ax = plt.subplots()

x = []
y = []

with open('temp.txt') as f:
    reader = f.readlines()
    for item in reader:
        data = item.split()
        x.append(int(data[0]))
        y.append(float(data[1]))


plt.plot(x, y, marker='o', linestyle='solid')
plt.yticks([i for i in range(0, 21)])
plt.xticks([i for i in range(1, 25)])
plt.ylabel('Stock Price($)')
plt.xlabel('Year')
plt.grid()
# plt.axis([1990, 2016, 0.0000, 1.2000])
plt.title('Year End Stock Prices Since 1990')
# c = np.cos(2 * np.pi * t)
# plt.rcParams['lines.linewidth'] = '3'
# plt.plot(t, c)

plt.show()

