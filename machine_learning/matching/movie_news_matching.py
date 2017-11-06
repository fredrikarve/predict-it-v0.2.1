from os import path
from data.content.movie import Movie
import codecs
parent_path = path.abspath('..')


# function that takes in a news category and returns movie categories relating
# to that set of news
def news_to_movie(key):
    dict = {}

    dict.setdefault('comp.graphics', []).append('Animation')
    dict.setdefault('comp.graphics', []).append('Sci-Fi')
    dict.setdefault('comp.os.ms-windows.misc', []).append('Sci-Fi')
    dict.setdefault('comp.os.ms-windows.misc', []).append('Animation')
    dict.setdefault('comp.sys.ibm.pc.hardware', []).append('Animation')
    dict.setdefault('comp.sys.mac.hardware', []).append('Animation')
    dict.setdefault('comp.windows.x', []).append('Animation')
    dict.setdefault('misc.forsale', []).append('Drama')
    dict.setdefault('misc.forsale', []).append('Thriller')
    dict.setdefault('rec.autos', []).append('Action')
    dict.setdefault('rec.autos', []).append('Crime')
    dict.setdefault('rec.motorcycles', []).append('Crime')
    dict.setdefault('rec.motorcycles', []).append('Action')
    dict.setdefault('rec.sport.baseball', []).append('Comedy')
    dict.setdefault('rec.sport.baseball', []).append('Fantasy')
    dict.setdefault('rec.sport.hockey', []).append('Action')
    dict.setdefault('rec.sport.hockey', []).append('Fantasy')
    dict.setdefault('sci.crypt', []).append('Crime')
    dict.setdefault('sci.crypt', []).append('Sci-Fi')
    dict.setdefault('sci.electronics', []).append('Sci-Fi')
    dict.setdefault('sci.electronics', []).append('Thriller')
    dict.setdefault('sci.med', []).append('Crime')
    dict.setdefault('sci.med', []).append('Thriller')
    dict.setdefault('sci.space', []).append('Sci-Fi')
    dict.setdefault('sci.space', []).append('Horror')
    dict.setdefault('talk.politics.misc', []).append('Documentary')
    dict.setdefault('talk.politics.misc', []).append('War')
    dict.setdefault('talk.politics.guns', []).append('War')
    dict.setdefault('talk.politics.guns', []).append('Western')
    dict.setdefault('talk.politics.mideast', []).append('War')
    dict.setdefault('talk.politics.mideast', []).append('Action')
    dict.setdefault('talk.religion.misc', []).append('Drama')
    dict.setdefault('talk.religion.misc', []).append('Fantasy')
    dict.setdefault('alt.atheism', []).append('Documentary')
    dict.setdefault('alt.atheism', []).append('Drama')
    dict.setdefault('soc.religion.christian', []).append('Mystery')
    dict.setdefault('soc.religion.christian', []).append('Fantasy')
    return dict.get(key)


# Function that matches news categories to movie genres and return a list of
# up to 10 movie class objects.
# Parameter: The news category that will be matched with the movie genres.
def get_movie_from_news(newscategory):

    path1 = parent_path + '/predict-it/machine_learning/prediction/new_algorithm/ml-1m/movies.dat'
    movieList = []
    for line in codecs.open(path1, 'r', encoding="utf-8", errors='ignore'):
        for genre in news_to_movie(newscategory):
            if genre in line:
                tempMovie = line.split('::')
                movieList.append(Movie(tempMovie[0], tempMovie[1],
                                       tempMovie[2]))
                if len(movieList) == 10:
                    #for temp in movieList:
                         # print(temp.getMovieID() + temp.getTitle() +
                         #     temp.getGenres() + '\n')
                    return movieList

    # Returns the movieList if less than 10 matches are found (very unlikely)
    return movieList
