from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def train_model(X, Y):

    model = LinearRegression()

    model.fit(X, Y)

    prediction = model.predict(X)

    return (
        model.intercept_,
        model.coef_,
        prediction,
        r2_score(Y, prediction)
    )
