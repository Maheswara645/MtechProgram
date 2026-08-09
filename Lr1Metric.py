from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import math
y=[3,-0.5,2,7];p=[2.5,0.0,2,8]
print(mean_absolute_error(y,p))
mse=mean_squared_error(y,p)
print(mse)
print(math.sqrt(mse))
print(r2_score(y,p))
