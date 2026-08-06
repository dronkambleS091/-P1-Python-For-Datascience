import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [2,4,6,8,10]

categories = ["Data Structures", "Scala for DS", "Operating System", "Python for DS"]
scores = [65,70,74,60]

x_scatter = [5,7,8,7,6,9,5]
y_scatter = [99,86,87,88,100,86,103]

data = np.random.normal(0,1,100)

fig, axs = plt.subplots(2,2,figsize=(10,8))

axs[0,0].plot(x,y,marker="o")
axs[0,0].set_title("Line Plot")

axs[0,1].bar(categories,scores,color="orange")
axs[0,1].set_title("Bar Chart")
axs[0,1].tick_params(axis="x",rotation=15)

axs[1,0].scatter(x_scatter,y_scatter,color="green",s=100)
axs[1,0].set_title("Scatter Plot")

axs[1,1].hist(data,bins=20,color="purple",edgecolor="black")
axs[1,1].set_title("Histogram")

plt.tight_layout()

plt.show()
