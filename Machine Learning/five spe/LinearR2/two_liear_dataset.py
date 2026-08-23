data2 = pd.DataFrame({
    "X":[1,2,3,4,5],
    "Y":[2,5,4,8,7]
})

model1 = LinearRegression()
model1.fit(data1[["X"]], data1["Y"])

pred1 = model1.predict(data1[["X"]])
r21 = r2_score(data1["Y"], pred1)

model2 = LinearRegression()
model2.fit(data2[["X"]], data2["Y"])

pred2 = model2.predict(data2[["X"]])
r22 = r2_score(data2["Y"], pred2)

print("Dataset 1 R2 =", r21)
print("Dataset 2 R2 =", r22)

if r21 > r22:
    print("Model 1 performs better")
else:
    print("Model 2 performs better")
