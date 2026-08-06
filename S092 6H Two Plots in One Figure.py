import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

categories = ["Data Structures", "Scala for DS", "Operating System", "Python for DS"]
scores = [65, 70, 74, 60]

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(x, y, marker="o")
plt.title("Line Plot")

plt.subplot(1,2,2)
plt.bar(categories, scores, color="green")
plt.title("Bar Chart")

plt.xticks(rotation=15)

plt.tight_layout()

plt.show()
