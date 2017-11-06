# Data transfer object for ratings, use it to send rating objects between different parts of the program.


class Rating():

    def __init__(self, UserID, MovieID, Rating, Timestamp):
        self.UserID = UserID
        self.MovieID = MovieID
        self.Rating = Rating
        self.Timestamp = Timestamp

    def getUserID(self):
        return self.UserID

    def getMovieID(self):
        return self.MovieID

    def getRating(self):
        return self.Rating

    def getTimestamp(self):
        return self.Timestamp
