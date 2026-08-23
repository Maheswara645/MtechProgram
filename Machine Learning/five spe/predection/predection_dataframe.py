import pandas as pd

data = pd.DataFrame({
    "Hours":[1,2,3,4,5],
    "Score":[20,35,45,55,70]
})

X = data[["Hours"]]
Y = data["Score"]

intercept, coefficient, prediction, r2 = train_model(X, Y)

print("Intercept:", intercept)
print("Coefficient:", coefficient)
print("Predictions:", prediction)
print("R2:", r2)
