import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("students.csv")

X = data[["Hours"]]
y = data["Score"]

model = LinearRegression()
model.fit(X, y)

# Predict using a DataFrame
new_data = pd.DataFrame({"Hours": [6]})
prediction = model.predict(new_data)

print("Coefficient =", model.coef_[0])
print("Intercept =", model.intercept_)
print("Prediction for 6 hours =", prediction[0])
