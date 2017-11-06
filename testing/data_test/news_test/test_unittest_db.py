import unittest
import newspaper
import datetime
import os
from data.news.news_database import models
from data.news.news_database.models import add_news_to_db
from data.news.news_collector import collect_news


class TestStringMethods(unittest.TestCase):

    path = os.path.abspath(os.path.join('data/news', 'model.pkl'))

    # This test case tests if the database are storing the data in correct
    # format 
    def test_string_database(self):
        self.assertTrue(isinstance(models.News.query.first().title, str))
        self.assertTrue(isinstance(models.News.query.first().id, int))
        self.assertTrue(isinstance(models.News.query.first().source, str))
        self.assertTrue(isinstance(models.News.query.first().collected, str))
        self.assertTrue(isinstance(models.News.query.first().url, str))

    # This test case tests if the database are storing the news in correct
    # length
    def test_news_string(self):
        paper = newspaper.build('http://cnn.com', memoize_articles=True)
        for current_article in paper.articles:
            current_article.download()
            current_article.parse()
            current_article.nlp()
            self.assertLessEqual(len(current_article.title), 150)
            self.assertLessEqual(len(paper.brand), 100)
            self.assertLessEqual(len(current_article.url), 250)
            self.assertLessEqual(len(datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S')), 20)
            self.assertLessEqual(len(current_article.keywords), 30)
            print('titel: ' + str(len(current_article.title)))
            print('source: ' + str(len(paper.brand)))
            print('url: ' + str(len(current_article.url)))
            print('collected: ' + str(len(datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'))))
            print('keywords: ' + str(len(current_article.keywords)))

    # This test case tests if the database only saves up to 20 news in the db.
    def test_news_number(self):
        all_news = models.News.query.all()
        self.assertLessEqual(len(all_news), 20)

    # This test case tests when new news are collected and old news are removed
    # the function removes the oldest news first from the db.
    def test_old_removed(self):
        oldest_news_1 = models.News.query.first().collected
        # Extracts articles from different news sources
        news_data = collect_news()
        # Uses the add_to_db method in news_database.models
        # to add the articles in the list to the news database
        add_news_to_db(news_data)
        oldest_news_2 = models.News.query.first().collected
        print('Here is oldest news 1: ' + oldest_news_1)
        print('Here is oldest news 2: ' + oldest_news_2)
        print(
            len(news_data), 'fresh news collected  ', datetime.datetime.now())
        self.assertLessEqual(oldest_news_1, oldest_news_2)

    # This test case tests that the database with news has the same or more
    # amount of articles after we have gathered new news.
    def test_if_stable(self):
        all_news_1 = models.News.query.all()
        length_of_news = len(all_news_1)
        print('The original length: ' + str(length_of_news))
        # Extracts articles from different news sources
        news_data = collect_news()
        # Uses the add_to_db method in news_database.models
        # to add the articles in the list to the news database
        add_news_to_db(news_data)
        print(
            len(news_data), 'fresh news collected  ', datetime.datetime.now())
        all_news_2 = models.News.query.all()
        length_of_news_updated = len(all_news_2)
        print('The updated length: ' + str(length_of_news_updated))
        self.assertLessEqual(length_of_news, length_of_news_updated)

    def test_news_categorization(self):
        self.assertTrue(isinstance(models.News.query.first().category, str))

suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
