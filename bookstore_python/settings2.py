import os
from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURANÇA: Mantenha a Secret Key em variável de ambiente!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-o&bx13fby9^jkl@8_17(!k2e!-y=)n!t@dl@=+-o4se^s67x38')

# DEBUG: No Docker/Produção, passamos 1 para True ou 0 para False no .env
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# RESOLVE O SEU ERRO: Adicione os hosts permitidos
# O '*' permite qualquer host (ideal para dev com Docker)
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1,0.0.0.0').split(',')

# Configuração das Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions', # Esta é a tabela que estava faltando na primeira imagem!
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_extensions",
    "rest_framework",
    "rest_framework.authtoken",
    "debug_toolbar",
    
    # Suas Apps
    'product', 
    "order"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'bookstore_python.urls' 

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # ou outro número de sua preferência
     'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# Configuração do Banco de Dados (Postgres do seu docker-compose)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'bookstore_dev_db'),
        'USER': os.getenv('POSTGRES_USER', 'bookstore_dev'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'bookstore_dev'),
        'HOST': 'db', # Nome do serviço definido no docker-compose.yml
        'PORT': '5432',
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'