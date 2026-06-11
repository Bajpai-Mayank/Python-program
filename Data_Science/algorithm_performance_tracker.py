import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load the data
df = pd.read_csv('algorithm_submissions.csv')

# 2. Clean Outliers (The Pandas Way)
# Instead of a loop, we create a "mask". This keeps all rows where time is <= 100.
df_clean = df[df["execution_time_ms"] <= 100.0]

# 3. Calculate Mean and Median
# 'groupby' automatically does the heavy lifting of grouping the algorithms together
print("--- Mean and Median Execution Times ---")
stats = df_clean.groupby('technique')[
    'execution_time_ms'].agg(['mean', 'median'])
print(stats)

# 4. Graphing with Seaborn
print("\nGenerating Boxplot...")
# We pass the whole cleaned dataframe directly to Seaborn
sns.boxplot(
    data=df_clean,
    x='technique',          # X-axis will be the algorithm names
    y='execution_time_ms',  # Y-axis will be the times
    hue='language'  # 'hue' automatically splits the data by Java and Python!
)

# Add a title and show the plot
plt.title("Execution Time: Java vs Python by Algorithm")
plt.show()
# mine approach :(

org_df = pd.read_csv('algorithm_submissions.csv')
df = org_df.copy()
techniques = ["Two Pointers", "HashMaps",
              "Sliding Window", "Dynamic Programming"]
languages = ["Java", "Python"]

for index in df.index:
    if df.loc[index, "execution_time_ms"] > 100.0:
        df.drop(index, inplace=True)

for _, items in enumerate(techniques):
    print(f"Mean Execution Time for {items} : ",
          "\033[33m", df.loc[df['technique'] == items, "execution_time_ms"].mean(), "\033[0m")
    print(f"Median Execution Time for {items} : ",
          "\033[33m", df.loc[df['technique'] == items, "execution_time_ms"].median(), "\033[0m")
print("\nGenerating Boxplot...")
sns.boxplot(
    data=df,
    x='technique',
    y='execution_time_ms',
    hue='language'
)
plt.title("Algorithm Performance: Java vs Python")
plt.show()
sns.barplot(
    data=df,
    x='technique',
    y='memory_usage_mb',
    hue='language'
)
plt.title("Memory Usage : Java vs Python")
plt.show()
sns.displot(
    data=df,
    x='execution_time_ms',
    y='memory_usage_mb',
    hue='language',
    kind='kde'
)

plt.title(" Algorithm Performance vs Memory Usage : Java vs Python")
plt.show()
