import joblib
from flaskr.FeatureExtraction import getAttributess

class myModel:
    def __init__(self):
        # check model path
        self.model = joblib.load('./flaskr/xgb_model.pkl') # hierarchy proj structure
        # self.model = joblib.load('./xgb_model.pkl') # plain proj structure

    def __getFeature(self, url):
        return getAttributess(url)

    def __useModel(self, features):
        return self.model.predict(features)

    def pipeline(self, url):
        features = self.__getFeature(url)
        return self.__useModel(features)
