# Data transfer object for User, use it to send user objects between different parts of the program.


class User:

    def __init__(self, UserID, Gender, Age, Occupation, ZipCode):
        self.UserID = UserID
        self.Gender = Gender
        self.Age = Age
        self.Occupation = Occupation
        self.ZipCode = ZipCode

    def getUserID(self):
        return self.UserID

    def getGender(self):
        return self.Gender

    def getAge(self):
        return self.Age

    def getOccupation(self):
        return self.Occupation

    def getZipCode(self):
        return self.ZipCode


def make_user(userID, gender, age, occupation, zipCode):
    user = User(userID, gender, age, occupation, zipCode)
    return user
