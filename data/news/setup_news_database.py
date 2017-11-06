import os
from sys import platform


# Runs download_nltk which downloads program for getting news, if nessesary
exec(open(os.path.abspath('data/news/download_nltk.py')).read())

# Saves the paths for db_create
create_path = os.path.abspath('data/news/news_database/db_create.py')

# If it runs on a Mac, some configuration of SSL is nessesary
if platform == 'darwin':
    exec(open(os.path.abspath('data/news/ssl_update.py')).read())

# Creates the database
exec(open(create_path).read())
