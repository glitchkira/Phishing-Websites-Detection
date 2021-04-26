from .myPredModel import myModel
from flaskr.phishTankApiRequest import PhishTank
# import os

# import sys
import time

# currentDir = os.path.dirname(__file__)
def checkWithSql(url):
    """ Check the user input url with sql
    """
    urlInSql = 0
    judge = 0
    time_start= time.time()
    # return 0 # overlook this func
    phishTank = PhishTank()
    result = phishTank.check(url)
    if result.in_database:
        # url exists in SQL
        urlInSql = 1
        if result.valid:
            print("{url} is a phish!".format(url=result.url))
            # flash("Phishing Website: \n" + url, 'danger')
            judge = 1
        else:
            print("{url} is not a phish!".format(url=result.url))
            # flash("Legitimate Website: \n" + url, 'success')
            judge = 0
    else:
        # url Not exists in SQL
        urlInSql = 0
        print("{url} is not in the PhishTank database".format(url=result.url))
    time_end = time.time()
    time_c = time_end - time_start 
    print('time cost for sql', time_c, 's')

    return urlInSql, judge

def check(url):
    ''' Make prediction with trained model
    '''
    judge = 0
    url = url.lower()

    if 'http' not in url:
        url = 'https://www.' + url
    print("url to predict is:" + url)
    # Check with sql first
    try:
        urlInSql, judge = checkWithSql(url)
    except Exception as error:
        print("Sql failed: %s" % error)

    try:
        if not urlInSql:
            # if url not exist in sql, then check with machine learning model
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

