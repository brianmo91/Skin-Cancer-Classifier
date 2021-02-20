# Skin Cancer Classifier

<img src="index.png" height=350 border="1px">
<img src="results.png" height=350 border="1px">

Installation & Use
------------

This project runs on the Flask framework. It is recommended to run this project in a virtual environment. You can do this with the following instructions:

After forking, open CLI path to ```/src/flask_app/```

##### Installing and Activating Virtual Environment (Recommended)

```
pip install virtualenv
```

For Mac/Linux users:
```
python3 -m venv env
.env/bin/activate
 ```


For Windows users: 
```
python -m venv env
env\Scripts\activate
 ```

##### Install Required Packages

```
pip install -r requirements.txt
```
##### Running the Project
Start the project by running:
```
flask run
```
If flask runs into errors, you may also run the 'app.py' file directly through python:  ```python app.py```

The project may take a few minutes to load (~1-5 minutes).
After successfully loading, it should read something like:
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Simply copy and paste the URL into your browser.

Datasets
--------

<br>https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000

Training Models
---------------
