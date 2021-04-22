import joblib
from flaskr.FeatureExtraction import getAttributess

class myModel:
    def __init__(self):
     self.model = joblib.load('./xgb_model.pkl')

    def __getFeature(self, url):
        return getAttributess(url)

    def __useModel(self, features):
        return self.model.predict(features)

    def pipeline(self, url):
        features = self.__getFeature(url)
        return self.__useModel(features)



if __name__ == '__main__':
    model = myModel()
    # print(model.pipeline('https://github.com/masqueraderx'))
    print(model.pipeline('https://www.google.com'))
    