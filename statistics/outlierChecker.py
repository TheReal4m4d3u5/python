def median_of_list(values):
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    return values[mid]

def quartiles(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        lower_half = data[:mid]
        upper_half = data[mid:]
    else:
        lower_half = data[:mid]
        upper_half = data[mid + 1:]

    q1 = median_of_list(lower_half)
    q3 = median_of_list(upper_half)
    return q1, q3

raw = input("Enter numbers separated by commas: ")
data = sorted([float(x.strip()) for x in raw.split(",")])

q1, q3 = quartiles(data)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = [x for x in data if x < lower_bound or x > upper_bound]

print("\n--- Outlier Check ---")
print("Sorted data:", data)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)
print("Outliers:", outliers if outliers else "None")