from .base import *

SECRET_KEY = get_env_variable("SECRET_KEY")

ALLOWED_HOSTS = ("ponycheckup.amanzi.nz",)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_env_variable("DBNAME"),
        "USER": get_env_variable("DBUSER"),
        "PASSWORD": get_env_variable("DBPASSWORD"),
        "HOST": get_env_variable("DBHOST"),
        "PORT": get_env_variable("DBPORT"),
    }
}

