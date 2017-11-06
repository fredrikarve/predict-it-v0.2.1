import numpy as np
from machine_learning.prediction.new_algorithm.examples import svd
from data.news.news_database.models import get_five_articles, News
model = 0   # The ML-model. If it's value is 0, it means it's not trained yet.


def get_news():
    return


def add_rating(userid, movieid, rating):
    userid_str = str(userid)
    movieid_str = str(movieid)
    rating_str = str(rating)
    with open('ml-1m/ratings.dat', 'a') as f:
        # UserID::MovieID::Rating::Timestamp
        f.write(userid_str + '::' + movieid_str + '::' +
                rating_str + '::' + '987654321\n')
    f.closed
    return


# Trains the model. This function has to be called for before requesting any
# predictions.
def initialize():
    global model
    model = svd.initialize()


# The function needs an array of users and an array of items of equal size to
# return a result[i] of how likely it is that User[i] likes item[i]. If the
# model is not yet trained it will be trained before a result will be returned.
# Show_valid is by default set to false but if set to True, the function will
# return the mean square error of the whole valid dataset.
def get_rating(users, items, show_valid=False):
    global model
    if model == 0:  # This means the model has not been trained/initialized yet
                    # and training has to be done.
        print('Model is not trained yet, training initialized')
        initialize()
    # TODO add a check if users and items are of equal size.
    array_of_users = np.array(users)   # Converts the arrays into nympy arrays.
    array_of_news = np.array(items)
    result = model.tf_counterpart.prediction(array_of_users,
                                             array_of_news, show_valid)
    return result


# This function takes a User as input and get the id of five articles from the
# database. Then it uses the get_rating function to get predictions on each of
# these articles. Predictions are made based on the movie database,
# DO NOT TRUST, yet
# The return type is 'News' as can be found in news->news_database->models.
def get_news(user):
    #print(User)
    #print(User.UserID)
    user_arr = [user.UserID, user.UserID, user.UserID, user.UserID, user.UserID]
    articles_arr = get_five_articles()
    articles_id_arr = []
    for k in articles_arr:
        articles_id_arr.append(k.id)
    result = get_rating(user_arr, articles_id_arr)
    max_index = np.argmax(result)

    return articles_arr[max_index]


# Creates fake ratings to help the machine learning algorithm take the category
# of the news into account. User 1 will always like com.graphics, User 2 will
# always like com.os.ms - windows.misc etc. If a real User behaves like on of
# the fake users below the ML-model will notice this and predict accordingly.
def create_bot_ratings(news_id, category):
    if category == 'comp.graphics':
        add_rating(1, news_id, 5)
    elif category == 'comp.os.ms - windows.misc':
        add_rating(2, news_id, 5)
    elif category == 'comp.sys.ibm.pc.hardware':
        add_rating(3, news_id, 5)
    elif category == 'comp.sys.mac.hardware':
        add_rating(4, news_id, 5)
    elif category == 'comp.windows.x':
        add_rating(5, news_id, 5)
    elif category == 'rec.autos':
        add_rating(6, news_id, 5)
    elif category == 'rec.motorcycles':
        add_rating(7, news_id, 5)
    elif category == 'rec.sport.baseball':
        add_rating(8, news_id, 5)
    elif category == 'rec.sport.hockey':
        add_rating(9, news_id, 5)
    elif category == 'sci.crypt':
        add_rating(10, news_id, 5)
    elif category == 'sci.electronics':
        add_rating(11, news_id, 5)
    elif category == 'sci.med':
        add_rating(12, news_id, 5)
    elif category == 'sci.space':
        add_rating(13, news_id, 5)
    elif category == 'misc.forsale':
        add_rating(14, news_id, 5)
    elif category == 'talk.politics.misc':
        add_rating(15, news_id, 5)
    elif category == 'talk.politics.guns':
        add_rating(16, news_id, 5)
    elif category == 'talk.politics.mideast':
        add_rating(17, news_id, 5)
    elif category == 'talk.religion.misc':
        add_rating(18, news_id, 5)
    elif category == 'alt.atheism':
        add_rating(19, news_id, 5)
    elif category == 'soc.religion.christian':
        add_rating(20, news_id, 5)
