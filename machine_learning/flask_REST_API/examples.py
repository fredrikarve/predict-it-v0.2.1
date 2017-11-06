from requests import get, post, delete
# Some example calls to the API. The get requests can be pasted into your web
# browser (only use the url), try it!

# Every time the API-restarts (api.py) the added and changed users are lost.
# The pre-added ones gets added every time the server restarts
# (user1 and user2).

print('\nTrying to get the existing users (user1 and user2). '
      'See the pre-added users in api.py')
print(get('http://localhost:5100/users/user1').json())
print(get('http://localhost:5100/users/user2').json())

# Printing the changed User, shall now show the updated User info.
print(get('http://localhost:5100/users/user2').json())

# Adding a new object by using a post request to the '/users' (UserList).
# The post for the UserList doesn't require an ID. This makes it easier for
# us since it just gives the new object an ID automatically. Post and put also
# have a callback function. The callback is currently set to return the User
# put/posted to the API. Put and Post request can therefore be printed
# directly.
print('\n Post: Adding a new User by calling post for the UserList.')
print(post('http://localhost:5100/users', data={'UserID': 5, 'Gender': 'F',
                                                'Age': 35,
                                                'Occupation': 8,
                                                'Zip-code': 12345,
                                                }).json())


# The whole list can be printed with the get for the UserList.
# This get returns all the users that currently exist.
print('\n Get: Printing the whole UserList by using get for the UserList.')
print(get('http://localhost:5100/users').json())

# A User can be deleted by calling delete.
print('\n Delete: Deleting user2 from the users stored in the API and '
      'printing the list again.')
delete('http://localhost:5100/users/user2')
print(get('http://localhost:5100/users').json())

# Print the latest news (currently 5)
print('\n Calling get for /news: \n')
print(get('http://localhost:5100/news').json())
