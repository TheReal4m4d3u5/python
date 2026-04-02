import math

def mean(data):
    return sum(data) / len(data)

def median(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    return data[mid]

def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)

def std_dev(data):
    return math.sqrt(variance(data))

def describe(data):
    return {
        "mean": mean(data),
        "median": median(data),
        "variance": variance(data),
        "std_dev": std_dev(data)
    }