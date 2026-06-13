# ==========================================
# 1. IMPORTING REQUIRED LIBRARIES
# ==========================================
import datetime                      # Used to manipulate standard dates and times
import matplotlib.pyplot as plt      # The base library used to draw the actual graphs/charts
import numpy as np                   # Used for numerical operations (imported just in case)
from numpy import random as rd       # Used to generate our random dummy data
import pandas as pd                  # The powerhouse library for data manipulation (DataFrames)
import seaborn as sns                # Built on top of matplotlib; makes statistical graphs (like heatmaps) look beautiful


# ==========================================
# 2. HELPER FUNCTION: GENERATE RANDOM DATES
# ==========================================
def _timestamp_data() -> datetime.datetime:
    """Generates a random timestamp at some point during the current year."""
    # Set the start boundary to January 1st of the current year at 00:00:00
    _start_range = datetime.datetime(datetime.datetime.now().year, 1, 1, 0, 0, 0)
    
    # Set the end boundary to December 31st of the current year at 23:59:59
    _end_range = datetime.datetime(datetime.datetime.now().year, 12, 31, 23, 59, 59)
    
    # Calculate the total difference in seconds between the start and end dates
    delta = _end_range - _start_range
    total_seconds = int(delta.total_seconds())
    
    # Pick a random number of seconds within that total range
    random_seconds = rd.randint(0, total_seconds)
    
    # Add those random seconds to January 1st to get a random date and time
    return _start_range + datetime.timedelta(seconds=random_seconds)


# ==========================================
# 3. CREATING THE DATASET
# ==========================================
# Building a dictionary of lists. Each key becomes a column, and the list becomes the rows.
media_data = {
    "video_duration": rd.randint(30, 100, size=(10)),   # 10 random lengths between 30-100s
    "likes": rd.randint(100, 5000, size=(10)),          # 10 random like counts between 100-5000
    "comments": rd.randint(10, 500, size=(10)),         # 10 random comment counts
    "shares": rd.randint(10, 500, size=(10)),           # 10 random share counts
    "avg_watch_time": rd.randint(10, 90, size=(10)) + rd.random(size=10).round(2), # Watch time with decimals
    "timestamp": [_timestamp_data() for _ in range(10)], # 10 random dates using our helper function
}

# Convert the raw dictionary into a Pandas DataFrame (a 2D table)
df = pd.DataFrame(media_data)
print("--- Original DataFrame ---")
print(df)
print("\n" + "=" * 50 + "\n")
# ==========================================
#      The Single Best Performing Video 
# ==========================================
highest_yield = df[df['avg_watch_time'] == max(df['avg_watch_time'])]
peak_day = pd.to_datetime(highest_yield['timestamp']).dt.day_name().to_string(index=False)
peak_watch = highest_yield['avg_watch_time'].to_string(index=False)

print(f"The single most-watched Reel was posted on a {peak_day} with {peak_watch} seconds.")
# ==========================================
# 4. EXTRACTING DAY OF THE WEEK (THE NEW CONCEPT)
# ==========================================
# pd.to_datetime() ensures the column is strictly recognized as time-series data.
# The .dt accessor lets us access special date properties.
# .day_name() magically converts the timestamp into "Monday", "Tuesday", etc.
df["day_of_week"] = pd.to_datetime(df["timestamp"]).dt.day_name()


# ==========================================
# 5. FINDING THE TRUE HIGHEST AVERAGE WATCH TIME
# ==========================================
# .groupby() groups all identical days together (e.g., all the Mondays together).
# ["avg_watch_time"] isolates the specific column we want to calculate.
# .mean() finds the true average of those grouped days.
day_performance = df.groupby("day_of_week")["avg_watch_time"].mean()

# .idxmax() finds the INDEX (the name of the day) that holds the maximum value.
best_day = day_performance.idxmax()

# .max() grabs the actual highest NUMBER (the highest average watch time).
highest_avg = day_performance.max()

# The :.2f inside the f-string forces the decimal to round strictly to 2 places for a cleaner print.
print(f"Highest Average Watch Time Day: {best_day} ({highest_avg:.2f} seconds)\n")
print("--- Average Watch Time per Day ---")
print(day_performance)
print("\n" + "=" * 50 + "\n")


# ==========================================
# 6. CALCULATING THE CORRELATION MATRIX
# ==========================================
# We only want to find relationships between numeric engagement metrics.
# If we included dates or strings, the math would break!
metrics_df = df[["likes", "comments", "shares", "avg_watch_time"]]

# .corr() runs complex statistics instantly to compare every column against every other column.
# It outputs a square grid mapping values from -1.0 to 1.0.
correlation_matrix = metrics_df.corr()

print("--- Correlation Matrix ---")
print(correlation_matrix, "\n")


# ==========================================
# 7. VISUALIZING WITH SEABORN HEATMAP
# ==========================================
# Set the physical size of the pop-up window (8 inches wide, 6 inches tall)
plt.figure(figsize=(8, 6))

# sns.heatmap breaks down like this:
# data: Requires a 2D grid of numbers (which is exactly what our correlation_matrix is!)
# annot=True: Automatically writes the numeric correlation score inside each colored square.
# cmap="coolwarm": Maps negative numbers to cool blues, and positive numbers to warm reds.
# vmin/vmax: Locks our color legend rigidly between -1 and 1 so the colors are accurate.
# fmt=".2f": Formats the text annotations inside the squares to exactly two decimal places.
sns.heatmap(
    data=correlation_matrix, 
    annot=True, 
    cmap="coolwarm", 
    vmin=-1, 
    vmax=1, 
    fmt=".2f"
)

# Add a clean title to the top of the chart
plt.title("Correlation Matrix of Reel Engagement Metrics", fontsize=14, pad=15)

# .tight_layout() ensures none of the labels or titles get cut off the edges of the window
plt.tight_layout()

# Actually render and display the visualization on the screen
plt.show()