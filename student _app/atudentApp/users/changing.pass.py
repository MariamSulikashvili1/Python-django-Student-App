 from django.contrib.auth.models import User
 u = User.objects.get(username="human reader12321")
 u.set_password("new password")
 u.save()

