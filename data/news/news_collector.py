import newspaper
import datetime
import itertools
import os
from data.news.news_categorization_predictor import news_predictor
from sklearn.datasets import fetch_20newsgroups
from sklearn.externals import joblib
from newspaper import news_pool


# Function that gathers news from a news site and
# returns a list of news and relating data
def collect_news():

    papers = []
    papers.append(newspaper.build('http://cnn.com', memoize_articles=True))
    papers.append(newspaper.build('http://www.bbc.com/news', memoize_articles=True))
    papers.append(newspaper.build('http://news.sky.com/world', memoize_articles=True))
    papers.append(newspaper.build('https://nytimes.com/section/world', memoize_articles=True))
    papers.append(newspaper.build('https://washingtonpost.com/world', memoize_articles=True))
    papers.append(newspaper.build('http://reuters.com/news/world', memoize_articles=True))

    news_pool.set(papers, threads_per_source=1)
    news_pool.join()
    news_list = []

    categories = fetch_20newsgroups(subset='train', shuffle=True)
    clf = joblib.load(os.path.join(os.path.dirname(__file__), 'model.pkl'))

    for paper in papers:
        for current_article in itertools.islice(paper.articles, 0, 5):
            current_article.download()
            current_article.parse()
            current_article.nlp()

            news_to_add = {'title': current_article.title,
                           'keywords': current_article.keywords,
                           'url': current_article.url,
                           'category': news_predictor([current_article.text], categories, clf),
                           'source': paper.brand,
                           'collected': datetime.datetime.now().strftime(
                               '%Y-%m-%d %H:%M:%S')
                           }
            news_list.append(news_to_add)

    return news_list
