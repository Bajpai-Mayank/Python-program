import pandas as pd
import numpy as np
import random
#Use ai to get csv file to work on it.
# Set seed for reproducibility
np.random.seed(42)
num_records = 5000

# Core categories
techniques = ["Two Pointers", "HashMaps", "Sliding Window", "Dynamic Programming"]
problems = ["Move Zeroes", "Valid Anagram", "Two Sum", "Palindrome Number"]
languages = ["Java", "Python"]

# Initialize basic DataFrame
data = {
    "submission_id": range(1, num_records + 1),
    "problem_name": [random.choice(problems) for _ in range(num_records)],
    "technique": [random.choice(techniques) for _ in range(num_records)],
    "language": [random.choice(languages) for _ in range(num_records)],
}

df = pd.DataFrame(data)

# Generate baseline execution times (simulating language differences)
df["execution_time_ms"] = np.where(
    df["language"] == "Java",
    np.random.normal(15, 5, num_records),   # Java is generally faster here
    np.random.normal(35, 10, num_records)   # Python is relatively slower
)

# Add technique-specific time variations
df.loc[df["technique"] == "HashMaps", "execution_time_ms"] += np.random.normal(5, 2, len(df[df["technique"] == "HashMaps"]))
df.loc[df["technique"] == "Two Pointers", "execution_time_ms"] -= np.random.normal(2, 1, len(df[df["technique"] == "Two Pointers"]))

# Generate baseline memory usage
df["memory_usage_mb"] = np.where(
    df["language"] == "Java",
    np.random.normal(40, 5, num_records),   # Java uses more memory overhead
    np.random.normal(15, 3, num_records)    # Python is lighter in this mock
)

# Inject the extreme outliers for your data cleaning task
outlier_indices = random.sample(range(num_records), 75)
df.loc[outlier_indices, "execution_time_ms"] = np.random.uniform(5000, 15000, 75) # Timeouts
df.loc[outlier_indices, "memory_usage_mb"] = np.random.uniform(500, 1024, 75)     # Memory leaks

# Clean up baseline numbers (no negative time/memory)
df["execution_time_ms"] = df["execution_time_ms"].clip(lower=1.0).round(2)
df["memory_usage_mb"] = df["memory_usage_mb"].clip(lower=1.0).round(2)

# Save to CSV
df.to_csv("algorithm_submissions.csv", index=False)
print("dataset 'algorithm_submissions.csv' generated successfully!")