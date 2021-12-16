ALLOWED_HOSTS = ['*']
DEBUG = True
LOCAL_SETTINGS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'amcm_db',
        'USER': 'root',
        'PASSWORD': 'root031027',
        'HOST': '',
        'PORT': '',
    }
}