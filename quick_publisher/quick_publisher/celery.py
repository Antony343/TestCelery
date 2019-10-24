import os
from celery import Celery

# associate a Celery environment variable called DJANGO_SETTINGS_MODULE with the Django project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quick_publisher.settings')

app = Celery('quick_publisher')

# get celery configurations from projects' settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
