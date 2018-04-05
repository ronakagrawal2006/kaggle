from sklearn import linear_model


class LinearRegression:
    def __init__(self):
        pass

    def get_model(self, train, y):
        # logreg = linear_model.LogisticRegression(C=1)  # e5
        # logreg.fit(train, y)
        return "I am a sample model"  # logreg

    def model_predict(self, model, data):
        return model.predict(data)
