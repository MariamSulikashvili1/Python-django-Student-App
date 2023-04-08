import student_app
from student_app. import AppConfig


class lmsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lmsApp'
