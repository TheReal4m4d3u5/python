import statistics
import math

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

    median = median_of_list(data)

    if n % 2 == 0:
        lower_half = data[:mid]
        upper_half = data[mid:]
    else:
        lower_half = data[:mid]
        upper_half = data[mid + 1:]

    q1 = median_of_list(lower_half)
    q3 = median_of_list(upper_half)

    return q1, median, q3

def analyze_data(data):
    data = sorted(data)

    mean = statistics.mean(data)
    median = statistics.median(data)
    minimum = min(data)
    maximum = max(data)

    q1, med, q3 = quartiles(data)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [x for x in data if x < lower_bound or x > upper_bound]

    if mean > median:
        skew = "Right-skewed (positive skew)"
    elif mean < median:
        skew = "Left-skewed (negative skew)"
    else:
        skew = "Approximately symmetric"

    print("\n--- Day 2 Data Analysis ---")
    print("Sorted data:", data)
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Minimum: {minimum}")
    print(f"Q1: {q1}")
    print(f"Q3: {q3}")
    print(f"Maximum: {maximum}")
    print(f"IQR: {iqr}")
    print(f"Lower outlier bound: {lower_bound}")
    print(f"Upper outlier bound: {upper_bound}")
    print(f"Outliers: {outliers if outliers else 'None'}")
    print(f"Skew hint: {skew}")

raw = input("Enter numbers separated by commas: ")
data = [float(x.strip()) for x in raw.split(",")]
analyze_data(data)