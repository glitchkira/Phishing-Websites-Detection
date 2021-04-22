Link: https://calm-peak-20355.herokuapp.com/input_url/

For windows Command Prompt:
```shell
# set FLASK_APP=flaskr
set FLASK_APP=main.py  # Current directory: flaskr
```

For Terminal:
```shell
$ # export FLASK_APP=flaskr
$ export FLASK_APP=main.py # Current directory: flaskr
```
Run server:

```shell
$ flask run
```

Run with Gunicorn:

```shell
web: python manage.py runserver 0.0.0.0:5000 # Windows
web: gunicorn main:app # Unix
```



Go to `chrome://extensions`, activate developer mode, click on `Load Unpacked` and select the `Extension` folder of this project.

