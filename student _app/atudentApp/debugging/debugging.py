# settings.py

INSTALLED_APPS = [
    'student_app',
    ...
    'debug_toolbar'
]


MIDDLEWARE_CLASSES = [
    'django.auth.users. middleware.SessionAuthenticationMiddleware',
    ...
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]
