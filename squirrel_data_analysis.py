import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('Central_Park_Squirrel_Census_Squirrel_Data.csv')


# Display basic information about the dataset
print(data.info())


# Display the first few rows of the dataset
print(data.head())


# Summary statistics
print(data.describe())


# Visualize the distribution of fur colors
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='Primary Fur Color')
plt.title('Distribution of Squirrel Fur Colors')
plt.xlabel('Primary Fur Color')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# Visualize the distribution of age categories
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='Age')
plt.title('Distribution of Squirrel Age Categories')
plt.xlabel('Age Category')
plt.ylabel('Count')
plt.show()


# Explore behavior patterns
behaviors = [
    'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Kuks',
    'Quaas', 'Moans', 'Tail flags', 'Tail twitches', 'Approaches',
    'Indifferent', 'Runs from'
]


behavior_counts = data[behaviors].sum()
print(behavior_counts)


# Visualize the distribution of behavior
plt.figure(figsize=(10, 6))
behavior_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Squirrel Behaviors')
plt.xlabel('Behavior')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# Geographic visualization (if you have lat/long data)
plt.figure(figsize=(10, 8))
plt.scatter(data['X'], data['Y'], alpha=0.5, color='green')
plt.title('Squirrel Sightings in Central Park')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()


# Age and Color Relationship
age_color_cross = pd.crosstab(data['Age'], data['Primary Fur Color'])
sns.heatmap(age_color_cross, annot=True, cmap='coolwarm', fmt='d')
plt.title('Age and Color Relationship')
plt.xlabel('Primary Fur Color')
plt.ylabel('Age')
plt.show()


# Correlation Analysis
correlation_matrix = data[behaviors].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Squirrel Behaviors')
plt.show()






