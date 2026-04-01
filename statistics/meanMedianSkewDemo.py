import statistics

raw = input("Enter numbers separated by commas: ")
data = [float(x.strip()) for x in raw.split(",")]

mean = statistics.mean(data)
median = statistics.median(data)

print("\n--- Mean vs Median ---")
print("Data:", sorted(data))
print("Mean:", mean)
print("Median:", median)

if mean > median:
    print("Interpretation: likely right-skewed.")
elif mean < median:
    print("Interpretation: likely left-skewed.")
else:
    print("Interpretation: likely symmetric.")