from transformations.transformations import add_constant, multiply_constant
from descriptive.descriptive_stats import mean
from descriptive.quartiles import iqr

def explore(data):
    add_val = float(input("Add value: "))
    mult_val = float(input("Multiply value: "))

    added = add_constant(data, add_val)
    multiplied = multiply_constant(data, mult_val)

    print("\n--- Original ---")
    print("Mean:", mean(data), "IQR:", iqr(data))

    print("\n--- After Adding ---")
    print("Mean:", mean(added), "IQR:", iqr(added))

    print("\n--- After Multiplying ---")
    print("Mean:", mean(multiplied), "IQR:", iqr(multiplied))

if __name__ == "__main__":
    raw = input("Enter numbers: ")
    data = [float(x.strip()) for x in raw.split(",")]
    explore(data)