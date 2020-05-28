from .base import *

SECRET_KEY = get_env_variable("SECRET_KEY")

ALLOWED_HOSTS = ("ponycheckup.amanzi.nz",)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_env_variable("NAME"),
        "USER": get_env_variable("USER"),
        "PASSWORD": get_env_variable("PASSWORD"),
        "HOST": get_env_variable("HOST"),
        "PORT": get_env_variable("PORT"),
    }
}
