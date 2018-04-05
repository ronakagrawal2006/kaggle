from .sample_feature import SampleFeature


class Features:
    def __init__(self):
        pass

    def load(self):
        print("I am loading sample feautre")
        sample = SampleFeature()
        print(sample)
