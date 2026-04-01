import numpy as np
import matplotlib.pyplot as plt


def summarize_data(data):
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data, ddof=1)
    minimum = np.min(data)
    maximum = np.max(data)

    print("\nSummary Statistics")
    print("------------------")
    print(f"Count:   {len(data)}")
    print(f"Mean:    {mean:.4f}")
    print(f"Median:  {median:.4f}")
    print(f"Std Dev: {std_dev:.4f}")
    print(f"Min:     {minimum:.4f}")
    print(f"Max:     {maximum:.4f}")


def plot_histogram(data, title, bins=30):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, edgecolor="black")
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


def simulate_normal():
    mean = float(input("Enter mean: "))
    std_dev = float(input("Enter standard deviation: "))
    n = int(input("Enter sample size: "))

    data = np.random.normal(loc=mean, scale=std_dev, size=n)
    summarize_data(data)
    plot_histogram(data, f"Normal Distribution (mean={mean}, std={std_dev}, n={n})")


def simulate_binomial():
    trials = int(input("Enter number of trials (n): "))
    prob = float(input("Enter probability of success (p): "))
    sample_size = int(input("Enter number of samples to generate: "))

    data = np.random.binomial(n=trials, p=prob, size=sample_size)
    summarize_data(data)

    bins = np.arange(np.min(data), np.max(data) + 2) - 0.5
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, edgecolor="black")
    plt.title(f"Binomial Distribution (trials={trials}, p={prob}, samples={sample_size})")
    plt.xlabel("Number of Successes")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


def simulate_uniform():
    low = float(input("Enter lower bound: "))
    high = float(input("Enter upper bound: "))
    n = int(input("Enter sample size: "))

    data = np.random.uniform(low=low, high=high, size=n)
    summarize_data(data)
    plot_histogram(data, f"Uniform Distribution (low={low}, high={high}, n={n})")


def simulate_exponential():
    scale = float(input("Enter scale (mean waiting time): "))
    n = int(input("Enter sample size: "))

    data = np.random.exponential(scale=scale, size=n)
    summarize_data(data)
    plot_histogram(data, f"Exponential Distribution (scale={scale}, n={n})")


def simulate_t_distribution():
    df = float(input("Enter degrees of freedom: "))
    n = int(input("Enter sample size: "))

    data = np.random.standard_t(df=df, size=n)
    summarize_data(data)
    plot_histogram(data, f"t-Distribution (df={df}, n={n})")


def main():
    while True:
        print("\nDistribution Simulator")
        print("----------------------")
        print("1. Normal")
        print("2. Binomial")
        print("3. Uniform")
        print("4. Exponential")
        print("5. t-Distribution")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            simulate_normal()
        elif choice == "2":
            simulate_binomial()
        elif choice == "3":
            simulate_uniform()
        elif choice == "4":
            simulate_exponential()
        elif choice == "5":
            simulate_t_distribution()
        elif choice == "6":
            print("Exiting simulator.")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()