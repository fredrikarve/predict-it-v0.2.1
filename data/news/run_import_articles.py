from data.news.news_collector import collect_news
from data.news.news_database.models import add_news_to_db
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def import_news():
    # Extracts articles from cnn
    news_data = collect_news()

    # Uses the add_to_db method in news_database.models
    # to add the articles in the list to the news database
    add_news_to_db(news_data)

    print(len(news_data), 'fresh news collected  ', datetime.datetime.now())


import_news()
scheduler = BlockingScheduler()
scheduler.add_job(import_news, 'interval', minutes=1)
scheduler.start()
