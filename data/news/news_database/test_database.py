from data.news.news_database import models
from data.news.news_database.models import get_keywords,\
    get_five_articles

# Prints the titles of all articles currently in the news database
for a in models.News.query.all():
    print(a)
    print(a.url)

# Prints the keywords for the given article title
print(get_keywords(models.News.query.first()))

for a in get_five_articles():
    print(a)
