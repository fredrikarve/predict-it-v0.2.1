# Data transfer object for movies, use it to send movie objects between different parts of the program.


class Movie():

    def __init__(self, MovieID, Title, Genres):
        self.MovieID = MovieID
        self.Title = Title
        self.Genres = Genres

    def getMovieID(self):
        return self.MovieID

    def getTitle(self):
        return self.Title

    def getGenres(self):
        return self.Genres
