import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(1, 10, 10) # Create an array containing 10 elements.
ypt1 = xpt / xpt # time complexity 0(1)
ypt2 = np.log2(xpt) # time complexity 0(logn)
ypt3 = xpt # time complexity 0(n)
ypt4 = xpt * np.log2(xpt) # time complexity 0(nlogn)
ypt5 = xpt * xpt # time complexity 0(n * n)


plt.plot(xpt, ypt1, '-o', label = "O(1)")
plt.plot(xpt, ypt2, '-o', label = "O(logn)")
plt.plot(xpt, ypt3, '-o', label = "O(n)")
plt.plot(xpt, ypt4, '-o', label = "O(nlogn)")
plt.plot(xpt, ypt5, '-o', label = "O(n * n)")

plt.legend(loc = "best")  #create a legend
plt.show()