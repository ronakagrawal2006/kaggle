from .sample_preprocessor import Helper


class Execute:
    def __init__(self):
        pass

    def process(self):
        help = Helper()
        help.helper_method()
        print('I am preprocessing')
