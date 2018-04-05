from .linear_regression import LinearRegression


class Model:
    def __init__(self):
        pass

    def load(self):
        print("I am loading model")
        lr = LinearRegression()
        print(lr.get_model())
