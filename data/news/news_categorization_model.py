from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib
from definitions import root_dir
import os


# Trains a ski-learn machine learning model using the 20 newsgroup dataset
def train_categorization_model():

    twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

    text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                         ('tfidf', TfidfTransformer()),
                         ('clf', MultinomialNB()),
                         ])

    text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

    parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
                  'tfidf__use_idf': (True, False),
                  'clf__alpha': (1e-2, 1e-3),
                  }

    gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
    gs_clf = gs_clf.fit(twenty_train.data, twenty_train.target)

    filepath = os.path.join(root_dir, 'data/news/model.pkl')
    filepath = os.path.abspath(os.path.realpath(filepath))

    joblib.dump(gs_clf, filepath)


if __name__ == '__main__':
    train_categorization_model()
