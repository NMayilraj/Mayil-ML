# import numpy as np
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# c = a*b
# d = np.dot(a,b)
# print(d)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv('C:\\Users\\Mayilraj\\Downloads\\Test ML\\Date,Temperature,Day of the week,Se.csv')
# Create a dictionary to map day of the week to numeric values
day_of_week_mapping = {
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6,
    'sunday': 7
}

# Convert the 'Day of the week' column to numeric values
data['Day of the week'] = data['Day of the week'].map(day_of_week_mapping)

# Split the data into training and testing sets
X = data[['Temperature', 'Day of the week', 'Season']]
y = data['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# print(X_test)
# print(X_train)
# print(y_test)
# print(y_train)

model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test data
predictions = model.predict(X_test)

# Evaluate the model's performance
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, predictions)
print('Mean Squared Error:', mse)