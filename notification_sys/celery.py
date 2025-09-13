from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification_sys.settings')

app = Celery('notification_sys')

# Load settings from Django settings, namespace=None because we use future-proof names
app.config_from_object('django.conf:settings', namespace='CELERY')

# Set timezone
app.conf.enable_utc = False
app.conf.timezone = 'Asia/Dhaka'

# Optional: beat schedule
app.conf.beat_schedule = {
    # Example:
    # 'broadcast-every-day-4am': {
    #     'task': 'notifications_app.tasks.broadcast_notification',
    #     'schedule': crontab(hour=4, minute=0),
    #     'args': ()
    # }
}

# Auto-discover tasks from installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
