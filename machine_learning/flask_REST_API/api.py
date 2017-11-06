from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from data.news.news_database.models import get_five_article_titles
from data.user_data.user import User
from data.user_data.user import make_user
from machine_learning.flask_REST_API.threaded_functions import ThreadingInitialize
from machine_learning.matching.movie_news_matching import get_movie_from_news
from machine_learning.prediction.new_algorithm.ml_functions import get_news

# Example from: https://flask-restful.readthedocs.io/en/latest/
# Similar to the _init_py file for the flask server.
# Initializes the training in a new thread to save some time.
thread = ThreadingInitialize()
app = Flask(__name__)
api = Api(app)


# Hardcoded users so that the API will have some users from the start, used
# for examples. Users from User.dat.  This array will be removed later, only
# used for examples and testing.
USERS = {
    'user1': {'UserID': '1', 'Gender': 'F', 'Age': '1',
              'Occupation': '10', 'Zip-code': '48067'},
    'user2': {'UserID': '2', 'Gender': 'M', 'Age': '56',
              'Occupation': '16', 'Zip-code': '70072'},
    'user3': {'UserID': '3', 'Gender': 'M', 'Age': '25',
              'Occupation': '15', 'Zip-code': '55117'},
}


# Handles requests for User that doesn't exists. Responds with error code and
# message specified in abort().
def abort_if_user_doesnt_exist(UserID):
    if UserID not in USERS:
        abort(404, message='User {} doesn\'t exist'.format(UserID))


# Make the specific arguments from the commandline available by connecting them
# to an attribute.
parser = reqparse.RequestParser()
parser.add_argument('Gender')
parser.add_argument('Zip-code')
parser.add_argument('Age')
parser.add_argument('Occupation')
parser.add_argument('UserID')
parser.add_argument('MovieID')  # Tillfälligt för att testa API:et


# User
# shows a single User with get. Put should be used to change an existing User,
# otherwise use post for the UserList. Delete currently removes the User from
# the API only. This will probably be changed later.
class User(Resource):
    def get(self, UserID):
        abort_if_user_doesnt_exist(UserID)
        return USERS[UserID]

    def delete(self, UserID):
        abort_if_user_doesnt_exist(UserID)
        del USERS[UserID]
        return '', 204

    def put(self, UserID):
        # not yet implemented. Use post for UserList instead.
        return "", 201


# UserList
# shows a list of all users with get and lets you POST to add new users.
# Post will only add a single User to the UserList.
class UserList(Resource):
    def get(self):
        return USERS

    def post(self):
        args = parser.parse_args()

        USERS['User' + str(args['UserID'])] = {'UserID': args['UserID'],
                                               'Gender': args['Gender'],
                                               'Age': args['Age'],
                                               'Occupation': args['Occupation'],
                                               'Zip-code': args['Zip-code']}

        # newsPrediction stores a recommended news article.

        newsPrediction = get_news(make_user(args['UserID'], args['Gender'], args['Age'],
                                            args['Occupation'], args['Zip-code']))

        # movieList contains a list of 10 movies based on the news article category.
        movieList = get_movie_from_news(newsPrediction.category)

        # We tried to send it as a complex json-object but had problems with it.
        # Currently it is instead stored as a string with :: as delimiters.
        # Need to make it as an complex json object during later sprints.
        message = str(newsPrediction.title + '::' + newsPrediction.category)

        for movie in movieList:
            message = message + '::' + movie.Title + '::' + movie.Genres

        return message, 201


# News
# Returns a list of the latest articles fetched by run_import_articles. This
# will only get the latest news, not related to the movie content.
class News(Resource):
    def get(self):
        return get_five_article_titles()


# Actually setup the Api resource routing here. Works like a simplified view.py
# in Flask.
api.add_resource(User, '/users/<string:UserID>')
api.add_resource(UserList, '/users')
api.add_resource(News, '/news')


# Same as run.py in Flask.
if __name__ == '__main__':
    app.run(debug=True, port=5100, threaded=True, use_reloader=False)



#
