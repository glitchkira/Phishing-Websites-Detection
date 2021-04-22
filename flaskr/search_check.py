 
from flask import flash, get_flashed_messages
from flaskr.myPredModel import myModel
from flaskr.phishTankApiRequest import PhishTank

import time

def checkWithSql(url):
    """ Check the user input url with sql
    """
    urlInSql = 0
    time_start= time.time()
    # return 0 # overlook this func
    phishTank = PhishTank()
    result = phishTank.check(url)
    if result.in_database:
        # url exists in SQL
        urlInSql = 1
        if result.valid:
            print("{url} is a phish!".format(url=result.url))
            flash("Phishing Website: \n" + url, 'danger')
        else:
            print("{url} is not a phish!".format(url=result.url))
            flash("Legitimate Website: \n" + url, 'success')
    else:
        # url Not exists in SQL
        urlInSql = 0
        print("{url} is not in the PhishTank database".format(url=result.url))
    time_end = time.time()
    time_c = time_end - time_start 
    print('time cost for sql', time_c, 's')

    return urlInSql

def checkWithML(url):
    """ Check the user input url with machine learning model
    """

    model = myModel()
    ans = model.pipeline(url)[0]
    # return ans
    if ans == 1:
        flash("Phishing Website: \n" + url, 'danger')
        print("ML result: PHISHING")

    elif ans == 0:
        flash("Legitimate Website: \n" + url, 'success')
        print("ML result: SAFE")
