from django.auth.student_app. import User
from django.student_app. import authenticate
 u = User.objects.get(username="Human")
 u.set_password("new password")
 u.save()

user = authenticate(username="Human", password="new password")
if user is not None:
    # A backend authenticated the credentials
    ...
else:
    # No backend authenticated the credentials
    ...