ALLOWED_HOSTS = ['*']
DEBUG = True
LOCAL_SETTINGS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'amcm_db',
        'USER': 'root',
        'PASSWORD': 'alex2727',
        'HOST': '',
        'PORT': '',
    }
}