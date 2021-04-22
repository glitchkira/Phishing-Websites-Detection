# from django.shortcuts import render, redirect
from flask import request, redirect
# from django.contrib import messages
from flask import flash, get_flashed_messages
# from PhishingWebsiteDefenseApp.useModel import MachineLearningModel
from flaskr.myPredModel import myModel
# from PhishingWebsiteDefenseApp.phnishTankApiRequest import PhishTank
from flaskr.phnishTankApiRequest import PhishTank

# other pkg
from flask import render_template

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

# helper Function
# def check(request):
@app.route("/input_url", methods=("GET", "POST"))
def inputWebsite():
    """
    """
    # if request.method == 'POST':
    if request.method == 'POST':    
        # url = request.POST.get('url')
        url = request.form['url']

        try:
            url = url.lower()

            if 'http' not in url:
                url = 'https://www.' + url

            phishTank = PhishTank()
            result = phishTank.check(url)
            if result.in_database:
                if result.valid:
                    print("{url} is a phish!".format(url=result.url))
                    # messages.error(request, "Phishing Website: " + url)
                    flash("Phishing Website: " + url, 'danger')
                else:
                    print("{url} is not a phish!".format(url=result.url))
                    # messages.success(request, "Legitimate Website: " + url)
                    flash("Legitimate Website: " + url, 'success')
            else:
                print("{url} is not in the PhishTank database".format(url=result.url))
                # model = MachineLearningModel()
                model = myModel()
                ans = model.pipeline(url)[0]
                if ans == 1:
                    # messages.error(request, "Phishing Website: " + url)
                    flash("Phishing Website: " + url, 'danger')

                elif ans == 0:
                    # messages.success(request, "Legitimate Website: " + url)
                    flash("Legitimate Website: " + url, 'success')

        except Exception as ex:
            print(ex)
            # messages.error(request, "There was Some Error in Prediction... Please Try Again")
            flash("There was Some Error in Prediction... Please Try Again", 'warning')

    # return redirect('/')
    return render_template('index.html')