from data.user_data.user import User
from data.news.news_database.models import News
from machine_learning.prediction.new_algorithm import ml_functions
from data.user_data.user import User
import nltk

#ml_functions.initialize()

#prediction = ml_functions.get_rating([10], [15])
#print('The prediction 1 is:', prediction)

#prediction = ml_functions.get_rating([13, 51, 9], [31, 51, 3], False)
#print('The prediction 2 is:', prediction)

#prediction = ml_functions.get_rating([13, 51, 9], [31, 51, 3], True)
#print('The error for prediction 2 is:', prediction)

#user1 = User(15, 'm', 20, 10, 58328)
#prediction = ml_functions.get_news(user1)
#print('The predicted article is:', prediction)

user1 = User(15, 'F', 18, 4, 58328)
prediction = ml_functions.get_news(user1)
print("The prediction 3 is:", prediction)
print("The prediction 3 is:", prediction.url)
