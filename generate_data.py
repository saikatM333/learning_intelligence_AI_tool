import pandas as pd
import numpy as np

np.random.seed(42)

N = 1000

data = {
    "student_id": np.arange(1, N + 1),
    "course_id": np.random.choice([101, 102, 103], size=N),
    "chapter_order": np.random.randint(1, 11, size=N),  # 10 chapters
    "time_spent": np.random.normal(loc=40, scale=20, size=N),  # minutes
    "score": np.random.normal(loc=65, scale=20, size=N),       # marks
}

df = pd.DataFrame(data)

# Introduce missing values (realistic)
for col in ["time_spent", "score"]:
    df.loc[df.sample(frac=0.05).index, col] = np.nan

# Clip logical bounds
df["time_spent"] = df["time_spent"].clip(1, 180)
df["score"] = df["score"].clip(0, 100)

# Completion logic (realistic dependency)
completion_probability = (
    0.4 * (df["score"].fillna(60) / 100) +
    0.4 * (df["time_spent"].fillna(30) / 100) +
    0.2 * np.random.rand(N)
)

df["completion_status"] = (completion_probability > 0.5).astype(int)

# Save dataset
df.to_csv("data/sample_students.csv", index=False)

print("Generated 1000 data points and saved to data/sample_students.csv")
