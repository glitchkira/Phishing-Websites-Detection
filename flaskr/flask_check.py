from .myPredModel import myModel
# import os

# import sys
import time

# currentDir = os.path.dirname(__file__)

def check(url):
    ''' Make prediction with trained model
    '''
    judge = 0
    url = url.lower()

    if 'http' not in url:
        url = 'https://www.' + url
    print("url to predict is:" + url)

    try:
        model = myModel()
        judge = model.pipeline(url)[0]
    except FileNotFoundError:
        judge = 2
        print('Exception: model Not Found')
    except UnicodeEncodeError:
        judge = 3
        print('Exception: Encoding incompatible, please try other links')
    except Exception:
        # messages.error(request, "There was Some Error in Prediction... Please Try Again")
        judge = 4
        print('Exception: not predicted')
    return judge



def check_url(url):
    ''' Explain the prediction result
    '''
    
    time_start= time.time() 
    prediction = check(url)
    result = ""
    if prediction == 0:
        # print "The website is safe to browse"
        result = "SAFE"
        print(result)
       
    elif prediction == 1:
        # print "The website has phishing features. DO NOT VISIT!"
        result = "PHISHING"
        print(result)
    else:
        result = "There was Some Error in Prediction: " + str(prediction)
        print(result)
    time_end = time.time()
    time_c = time_end - time_start   
    print('time cost', time_c, 's')
    return result
        # print 'Error -', features_test

