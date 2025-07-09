import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

# Number of records
n = 500

# Generate balanced target
feels_lonely = ['Yes'] * (n // 2) + ['No'] * (n // 2)
random.shuffle(feels_lonely)

# Create dataset
data = {
    "StudentID": [f"S{i+1:04d}" for i in range(n)],
    "Age": np.random.randint(18, 25, size=n),
    "CityType": np.random.choice(["Urban", "Semi-Urban"], size=n),
    "ScreenTimeHours": np.random.normal(6, 2, size=n).round(1),
    "TimeSpentAlone": np.random.normal(4, 2, size=n).round(1),
    "SleepQualityScore": np.random.randint(1, 10, size=n),
    "MoodStability": np.random.randint(1, 10, size=n),
    "SocialActivityScore": np.random.randint(1, 10, size=n),
    "FeelsLonely": feels_lonely
}

df = pd.DataFrame(data)

# Save as CSV
df.to_csv("loneliness_dataset.csv", index=False)
print("✅ New balanced dataset created!")
