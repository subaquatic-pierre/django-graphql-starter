from pathlib import Path
from .config import Config

config = Config()

BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = config.SECRET_KEY
DEBUG = config.DEBUG
APPEND_SLASH = False

WSGI_APPLICATION = "app.wsgi.application"
ROOT_URLCONF = "app.urls"


GRAPHENE = {
    "SCHEMA": "app.graphql.schema.schema",
    "SCHEMA_OUTPUT": "graphql/schema.graphql",  # defaults to schema.json,
    "SCHEMA_INDENT": 2,  # Defaults to None (displays all data on a single line)
}

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "graphene_django",
    "corsheaders",
    "app.core",
    "app.graphql",
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsPostCsrfMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Check if production or development environment
if DEBUG:
    # CORS settings
    ALLOWED_HOSTS = ["*"]
    CSRF_TRUSTED_ORIGINS = ["*"]
    CORS_ALLOW_ALL_ORIGINS = True

    # Databse settings
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

else:
    # CORS settings
    CORS_ALLOW_ALL_ORIGINS = True
    CSRF_TRUSTED_ORIGINS = config.CSRF_TRUSTED_ORIGINS
    ALLOWED_HOSTS = config.ALLOWED_HOSTS

    # Database settings
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config.DB_NAME,
            "USER": config.DB_USER,
            "PASSWORD": config.DB_PASSWORD,
            "HOST": config.DB_HOST,
            "PORT": config.DB_PORT,
        }
    }

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
    ]

