from app import app
from flask import render_template, redirect, url_for, request
from requests import post, get

from data.news.news_database.models import get_five_article_titles
from data.user_data.user import User
from data.content.movie import Movie


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/operatorView')
def operator_view():
    # myMovie = Movie(1, 'Toy Story (1995)', 'Animation|Childrens|Comedy')
    userPrediction = str(post('http://localhost:5100/users', data={'UserID': '4', 'Gender': 'M', 'Age': '45',
                                                                   'Occupation': '7', 'Zip-code': '02460'}).json())
    userPrediction = userPrediction.split('::')

    return render_template('operatorView.html', userPrediction=userPrediction)


@app.route('/userView')
def user_view():

    myUser = User(1, 'F', 1, 10, 48067)
    userPrediction = str(post('http://localhost:5100/users', data={'UserID': '4', 'Gender': 'M', 'Age': '45',
                                                                   'Occupation': '7', 'Zip-code': '02460'}).json())
    userPrediction = userPrediction.split('::')

    return render_template('userView.html', myUser=myUser,
                           userPrediction=userPrediction, news=get('http://127.0.0.1:5100/news').json())


# route for handling the login page logic
@app.route('/loginView', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                        request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('operator_view'))
    return render_template('/loginView.html', error=error)
