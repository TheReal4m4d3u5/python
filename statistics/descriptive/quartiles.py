def median(values):
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    return values[mid]

def quartiles(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2

    q2 = median(data)

    if n % 2 == 0:
        lower = data[:mid]
        upper = data[mid:]
    else:
        lower = data[:mid]
        upper = data[mid + 1:]

    q1 = median(lower)
    q3 = median(upper)

    return q1, q2, q3

def iqr(data):
    q1, _, q3 = quartiles(data)
    return q3 - q1