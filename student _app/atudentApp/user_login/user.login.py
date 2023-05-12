import django.student_app
user = user.object. create_user("Human", "human reader@123.local", "humanpassword")

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
user.last_name = "Reader"
user.save()

user = authenticate(username="Human", password="new password")
if user is not None:
    # A backend authenticated the credentials
    ...
else:
    # No backend authenticated the credentials
    ...