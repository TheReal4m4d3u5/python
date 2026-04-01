import matplotlib.pyplot as plt

raw = input("Enter numbers separated by commas: ")
data = [float(x.strip()) for x in raw.split(",")]

plt.figure(figsize=(10, 5))
plt.hist(data, bins=10, edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.boxplot(data, vert=False)
plt.title("Box Plot")
plt.xlabel("Value")
plt.tight_layout()
plt.show()