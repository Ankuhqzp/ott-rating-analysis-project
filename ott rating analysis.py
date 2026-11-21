# OTT Rating Analysis Project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating dataset
data = {
    'Platform': ['Netflix', 'Prime Video', 'Disney+', 'Netflix',
                 'Prime Video', 'Disney+', 'Netflix', 'Prime Video'],
    'Title': ['Money Heist', 'Mirzapur', 'Loki', 'Dark',
              'The Boys', 'WandaVision', 'Stranger Things', 'Farzi'],
    'Genre': ['Crime', 'Action', 'Sci-Fi', 'Thriller',
              'Action', 'Fantasy', 'Sci-Fi', 'Crime'],
    'Rating': [8.5, 8.4, 8.2, 8.7, 8.7, 7.9, 8.7, 8.4],
    'Views': [100, 85, 90, 75, 95, 80, 120, 70]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Display dataset
print("OTT Rating Dataset:")
print(df)

# Average rating of each platform
print("\nAverage Rating by Platform:")
print(df.groupby('Platform')['Rating'].mean())

# Highest rated show
print("\nHighest Rated Show:")
print(df.loc[df['Rating'].idxmax()])

# Total views by platform
print("\nTotal Views by Platform:")
print(df.groupby('Platform')['Views'].sum())

# Plot average rating
plt.figure(figsize=(8, 5))
sns.barplot(x='Platform', y='Rating', data=df)
plt.title("Average OTT Ratings")
plt.show()

# Plot genre distribution
plt.figure(figsize=(8, 5))
df['Genre'].value_counts().plot(kind='bar', color='skyblue')
plt.title("OTT Genre Distribution")
plt.xlabel("Genre")
plt.ylabel("Number of Shows")
plt.show()

# Rating distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Rating'], bins=5, color='orange', edgecolor='black')
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Shows")
plt.show()

# Views comparison
plt.figure(figsize=(8, 5))
sns.barplot(x='Title', y='Views', data=df)
plt.xticks(rotation=45)
plt.title("Show Views Comparison")
plt.tight_layout()
plt.show()

print("\nAnalysis Completed Successfully!")
