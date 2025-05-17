import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# Example training data: [rooms, square footage, age of house, location score]
X_train = np.array([
    [3, 1500, 10, 8],
    [4, 2000, 15, 7],
    [2, 1200, 5, 9],
    [5, 2500, 20, 6]
])

# Target values: House prices
y_train = np.array([450000, 600000, 350000, 700000])

# Initialize the regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Save the trained model to a .pkl file
joblib.dump(model, 'data/house_price_model.pkl')

print("Model saved as house_price_model.pkl")
