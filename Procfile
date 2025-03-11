release: python manage.py migrate
web: gunicorn config.wsgi --bind 0.0.0.0:5000
worker: REMAP_SIGTERM=SIGQUIT celery -A config.celery_app worker --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery -A config.celery_app beat --loglevel=info
web: gunicorn ivasgroup.wsgi:application
web: gunicorn ivasgroup.wsgi:application --workers 3 --log-file -
