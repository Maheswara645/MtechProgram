import numpy as np

X = np.array([1,2,3,4,5])
Y = np.array([2,4,5,4,5])

mean_x = np.mean(X)
mean_y = np.mean(Y)

numerator = np.sum((X - mean_x) * (Y - mean_y))
denominator = np.sum((X - mean_x) ** 2)

m = numerator / denominator
c = mean_y - m * mean_x

print("Slope =", m)
print("Intercept =", c)
