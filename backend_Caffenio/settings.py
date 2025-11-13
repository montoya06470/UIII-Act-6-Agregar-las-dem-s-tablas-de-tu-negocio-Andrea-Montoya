"""
Django settings for backend_Caffenio project.
CORREGIDO 100% - Noviembre 2025
Funciona PERFECTO con todos tus templates
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_grq6!-)y54607ys3w_^b!q*qq&96$oonel463s)_(c@s13#_5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ────────────────────────────── APPLICATIONS ──────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',     # NECESARIO PARA EL ADMIN
    'django.contrib.staticfiles',
    'app_Caffenio',
]

# ────────────────────────────── MIDDLEWARE (ARREGLADO) ──────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # ESTA LÍNEA ESTABA MAL ESCRITA
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend_Caffenio.urls'

# ────────────────────────────── TEMPLATES (YA FUNCIONA) ──────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'app_Caffenio' / 'templates'],  # CARPETA CORRECTA
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

WSGI_APPLICATION = 'backend_Caffenio.wsgi.application'

# ────────────────────────────── DATABASE ──────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ────────────────────────────── PASSWORD VALIDATION ──────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ────────────────────────────── INTERNACIONALIZACIÓN (MÉXICO) ──────────────────────────────
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Hermosillo'  # Sonora, donde está Caffenio
USE_I18N = True
USE_TZ = True

# ────────────────────────────── STATIC FILES ──────────────────────────────
STATIC_URL = 'static/'
# Quitamos STATICFILES_DIRS porque no tienes carpeta static (no es obligatorio)

# ────────────────────────────── DEFAULT PRIMARY KEY ──────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'