# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from django.conf import settings

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# app = Celery('FirstTry')  # Replace 'your_project' with your project's name.

# # Configure Celery using settings from Django settings.py.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load tasks from all registered Django app configs.
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# app.autodiscover_tasks()

import os 
from celery import Celery 

# set the default Django settings module for the 'celery' program. 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings') 

app = Celery('mysite') 

# Using a string here means the worker doesn't 
# have to serialize the configuration object to 
# child processes. - namespace='CELERY' means all 
# celery-related configuration keys should 
# have a `CELERY_` prefix. 
app.config_from_object('django.conf:settings', 
					namespace='CELERY') 

# Load task modules from all registered Django app configs. 
app.autodiscover_tasks() 
