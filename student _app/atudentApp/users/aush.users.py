from django.contrib.auth import authenticate

user = authenticate(username="human reader12321", password="")
if user is not None:
    # A backend authenticated the credentials
    ...
else:
    # No backend authenticated the credentials