#!/usr/bin/env python3
import unittest
from machine_learning.prediction.new_algorithm import ml_functions
from numpy import ndarray, float32
from data.user_data.user import User
from machine_learning. flask_REST_API import api
# Run the tests with run_pred_test.py.


def run_test(test_class, header):
    """
    Function to run all the tests from a class of tests.

    :type testClass: unittest.TesCase
    :type header: str
    """
    print(header)
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    unittest.TextTestRunner(verbosity=2).run(suite)


class TestPred(unittest.TestCase):
    """
    Class that test if a prediction is returned from the model
    """

    @classmethod
    def setUpClass(self):
        print("Start training model...")
        ml_functions.initialize()

    def test_single_prediction(self):
        """
        Test if a single prediction can be made
        and if return data is of correct type and size.
        """

        prediction = ml_functions.get_rating([3], [4])
        self.assertTrue(isinstance(prediction, ndarray))
        self.assertEqual(prediction.size, 1)

    def test_multiple_predictions(self):
        """
        Test if a multiple predictions can be made
        and if return data is of correct type and size.
        """
        prediction = ml_functions.get_rating([13, 51, 9], [31, 51, 3], False)
        self.assertTrue(isinstance(prediction, ndarray))
        self.assertEqual(prediction.size, 3)

    def test_prediction_error(self):
        """
        Test if the model can give information about prediction error.
        """
        prediction_error = ml_functions.get_rating([3], [4], True)
        self.assertTrue(isinstance(prediction_error, float32))

        prediction_error = ml_functions.get_rating([13, 51, 9], [31, 51, 3], True)
        self.assertTrue(isinstance(prediction_error, float32))


class TestNews(unittest.TestCase):
    """
    Class that test the content of the news used in the prediction.
    """

    def test_news_data(self):
        """
        Test if the system can generate real news when making a prediction for a User.
        The news shall be presented in a link that starts with 'http://' to verify that it is in fact a link.
        """
        user1 = User(15, 'm', 25, 10, 58328)
        prediction = ml_functions.get_news(user1)
        print("The prediction URL is:", prediction.url)
        self.assertTrue(prediction.url[:7] == 'http://')


class TestAPI(unittest.TestCase):
    """
    Class that test functionality from the api.
    """

    def test_five_articles(self):
        """
        Test if the api can return five articles and if these are the same as the ones that
        is returned from "from data.news.news_database.models import get_five_articles"
        used in ml_functions.py
        """

        five_articles_api = api.News.get(self)
        self.assertTrue(isinstance(five_articles_api, list))
        self.assertEqual(len(five_articles_api), 5)

        from data.news.news_database.models import get_five_articles
        five_articles_db = get_five_articles()
        self.assertTrue(isinstance(five_articles_db, list))
        self.assertEqual(len(five_articles_db), 5)

        for i in range(0, 5):
            art_api = str(five_articles_api[i])
            art_db = str(five_articles_db[i])
            # Strip the first string in db articles
            art_db = art_db[1:-1]
            self.assertTrue(art_api == art_db)

# class testUpdate(unittest.TestCase):
#        def test_update_userdata(self):
#         """
#         Test if the data stored from users can be modified if wanted.
#         Test if new items can be added, if ecisting items can be removed and altered.
#         """
#         user2 = User(15, 'f', 18, 5, 58328)
#         ml_functions.add_rating(15,1383,5)
#         # 1387::Jaws (1975)::Action|Horror
#
#         if '15::1383::5' in open('ml-1m/ratings.dat') == True:
#             print("The item has been added to the list")
#
#
#         #Enter ratings.dat and see if the new rating is stated in the list
