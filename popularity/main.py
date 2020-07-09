import pandas as pd
import numpy as np

frame = pd.read_csv('ratings.csv')
cuisine = pd.read_csv('cuisine.csv')

# get summary of the column, how many, how many uniques, most frequent
print(cuisine['Rcuisine'].describe())

rating_count = pd.DataFrame(frame.groupby('placeID')['rating'].count())

sorted_ratings = rating_count.sort_values('rating', ascending=False).head()

top_rated = pd.DataFrame([135085, 132825, 135032, 135052, 132834], index=np.arange(5), columns=['placeID'])

summary = pd.merge(top_rated, cuisine, on='placeID')

print(summary)