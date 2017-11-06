import subprocess
import threading
import os
from definitions import root_dir

class APIThreadInitialize(object):
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()                                  # Start the execution
    def run(self):
        subprocess.check_call(
            [pythonname, directory + '/machine_learning/flask_REST_API/api.py'])


class ArticleThreadInitialize(object):
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()                                  # Start the execution
    def run(self):
        subprocess.check_call(
            [pythonname, directory + '/data/news/run_import_articles.py'])


directory = os.path.dirname(os.path.abspath(__file__))

pythonname = 'python3.6'
try:
    subprocess.check_call([pythonname, directory + '/data/news/setup_news_database.py'])
except FileNotFoundError as e:
    pythonname = 'python'
    subprocess.check_call([pythonname, directory + '/data/news/setup_news_database.py'])

print('\n Set up database. Next step is to categorize news for model. Might take a few minutes if it is the first time you run this file. \n')

if not os.path.exists(directory + '/data/news/model.pkl'):
    subprocess.check_call([pythonname, directory + '/data/news/news_categorization_model.py'])

print('\n'
      'Finished categorizing news. Next we start threads to run news gathering, API and Flask server.'
      '\n')

article_thread = ArticleThreadInitialize()
print('\n'
      'Article thread started. \n')

API_thread = APIThreadInitialize()
print('\n'
      'API thread started. Flask server is started next. \n'
      'Please wait until the ML-model is trained before logging in. \n'
      'You will see data from the ML-model as prints in the console. \n')

subprocess.check_call([pythonname, directory + '/flask/run.py'])
