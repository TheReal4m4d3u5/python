import statistics

raw = input("Enter numbers separated by commas: ")
data = [float(x.strip()) for x in raw.split(",")]

add_value = float(input("Enter a value to add to each data point: "))
mult_value = float(input("Enter a value to multiply each data point by: "))

added_data = [x + add_value for x in data]
multiplied_data = [x * mult_value for x in data]

print("\n--- Original Data ---")
print(sorted(data))
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))

print("\n--- After Adding ---")
print(sorted(added_data))
print("Mean:", statistics.mean(added_data))
print("Median:", statistics.median(added_data))

print("\n--- After Multiplying ---")
print(sorted(multiplied_data))
print("Mean:", statistics.mean(multiplied_data))
print("Median:", statistics.median(multiplied_data))