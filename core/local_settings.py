ALLOWED_HOSTS = ['*']
DEBUG = True
LOCAL_SETTINGS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fusionti_amcm_db',
        'USER': 'fusionti_amcm_user',
        'PASSWORD': 'UZLs{R4s{Yr~',
        'HOST': '',
        'PORT': '',
    }
}