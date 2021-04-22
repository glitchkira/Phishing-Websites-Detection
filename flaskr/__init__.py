import os

from flask import Flask
from flask import request, make_response, redirect
from markupsafe import escape
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_wtf import FlaskForm

from flaskr.flask_check import check_url

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = '6612'
csrf=CSRFProtect(app)
csrf.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@csrf.exempt
@app.route('/get_url/', methods=['POST'])
def checkWebsite():
    message = 'Something wrong, please try again'
    if request.method == 'POST':
        pageUrl = request.form['url']
        # pageHtml = request.form['html']
        print(pageUrl) 
        message = check_url(pageUrl)
        resp = make_response(message)
        return resp
    else:
        print('Something wrong, please try again')
        resp = make_response('Error')
        return resp

from flask import request, redirect
from flask import flash, get_flashed_messages

from flask import render_template
from flaskr.search_check import checkWithSql, checkWithML
 
# Create your views here.
# def index(request):
#     return render(request, 'index.html')

# Web

@app.route("/input_url/", methods=("GET", "POST"))
def inputWebsite():
    """ open a website, input the url and check
    """
    urlInSql = 0
    form = FlaskForm()
    
    # request.form.

    # return redirect('/')
    # return render_template('index.html', post=post)
    return render_template('index.html', form=form)


@app.route('/nonce/', methods=['POST'])
def check_repeat_submission():
    """ stop posting form twice by redirect
    """
    if request.method == 'POST':    
        url = request.form['url']
        url = url.lower()
        if 'http' not in url:
            url = 'https://' + url
        print("url to predict is:" + url)

        # Check with sql first
        try:
            urlInSql = checkWithSql(url)
        except Exception as error:
            print("Sql failed: %s" % error)
        try:
            if not urlInSql:
                # if url not exist in sql, then check with machine learning model
                checkWithML(url)
        except Exception as error:
            print("ML failed %s" % error)
            flash("There was Some Error in Prediction... \nPlease Try Again", 'warning')
    return redirect('/input_url/')

from flask import send_file, send_from_directory

@app.route('/download/', methods=['GET'])
def download_extension():
    """ Webpage for chrome extension manual
    """
    return render_template('downpage.html')

@app.errorhandler(CSRFError)
# @app.route("/download/<filename>", methods=['GET'])
@app.route("/download/<filename>")
def download_file(filename):
    """ Function to download file
    """
    # NNeed to know path and filename
    # directory = os.getcwd() + "\\flaskr\\downloadFile"  # current directory
    directory = os.getcwd() + "/flaskr/downloadFile"  # heroku linux
    # directory = ('./flaskr/downloadFile')
    print(directory)
    download_extension()
    resp = make_response(
		send_from_directory(directory, filename, as_attachment=True))
    resp.headers["Content-Disposition"] = "attachment; filename={}".format(filename)
    
    return resp

"""
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
@csrf.exempt
"""

@app.errorhandler(CSRFError)
@app.route('/error400')
def csrf_error(reason):
    return "csrf not pass"

# if __name__ == '__init__':
#     app.run(debug=True)
def main():
    app.run(debug=True)
    
if __name__ == '__main__':
    main()