import math

def confidence_interval(data, confidence=0.95):
    n = len(data)
    
    # Mean
    mean = sum(data) / n
    
    # Standard deviation (sample)
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    std_dev = math.sqrt(variance)
    
    # Standard error
    standard_error = std_dev / math.sqrt(n)
    
    # Z-score lookup (for common confidence levels)
    z_scores = {
        0.90: 1.645,
        0.95: 1.96,
        0.99: 2.576
    }
    
    z = z_scores.get(confidence)
    if not z:
        raise ValueError("Unsupported confidence level")
    
    margin_of_error = z * standard_error
    
    lower = mean - margin_of_error
    upper = mean + margin_of_error
    
    return {
        "mean": mean,
        "std_dev": std_dev,
        "standard_error": standard_error,
        "confidence_interval": (lower, upper)
    }


# Example usage
data = [10, 12, 14, 16, 18]

result = confidence_interval(data)

print("Mean:", result["mean"])
print("Standard Deviation:", result["std_dev"])
print("Standard Error:", result["standard_error"])
print("95% Confidence Interval:", result["confidence_interval"])