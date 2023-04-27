import onelogin
# specify client_id, client_secret, and shard (us or eu)
creds = {'client_id':'',
     'client_secret':'',
     'shard':'US'}

token = onelogin.Token(**creds)

# Create the user object with the token created
user = onelogin.User(token)

# define the user, or build the user object from a csv file,
# To create a user you must include the firstname, lastname, email, and username
# attribute.
new_user = {
    'firstname':'Human',
    'lastname':'Reader',
    'email':'human reader@123.local',
    'username':'human reader12321'
}

# Search to see if the user exists based on email, if not, create a new user

if user.user_exists(new_user['email']):
    found_user = user.get_user_by_id(
        user.search_users(
            'email',new_user['email'])[0]['data'][0]['id']
    )
    print "Can not create user, already exists \r\n {0}".format(found_user)
else:
    Foo = user.create_user(**new_user)
    user_id = Foo['data'][0]['id']
    print 'Created User: {0}'.format(new_user)

    urlpatterns = [
        path('', views.Calendar, name='user'),
        path('user/', views.EventListView.as_view(), name='user'),
    ]
     return new_user
