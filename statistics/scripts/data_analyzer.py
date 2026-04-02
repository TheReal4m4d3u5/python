from descriptive.descriptive_stats import describe
from descriptive.quartiles import quartiles, iqr
from outliers.outlier_detection import find_outliers

def analyze(data):
    stats = describe(data)
    q1, q2, q3 = quartiles(data)
    spread = iqr(data)
    outliers = find_outliers(data)

    print("\n--- Data Analysis ---")
    print("Data:", sorted(data))
    print("Mean:", stats["mean"])
    print("Median:", stats["median"])
    print("Std Dev:", stats["std_dev"])

    print("\nQuartiles:")
    print("Q1:", q1)
    print("Q2:", q2)
    print("Q3:", q3)
    print("IQR:", spread)

    print("\nOutliers:", outliers if outliers else "None")

    if stats["mean"] > stats["median"]:
        print("Skew: Right")
    elif stats["mean"] < stats["median"]:
        print("Skew: Left")
    else:
        print("Skew: Symmetric")

if __name__ == "__main__":
    raw = input("Enter numbers separated by commas: ")
    data = [float(x.strip()) for x in raw.split(",")]
    analyze(data)