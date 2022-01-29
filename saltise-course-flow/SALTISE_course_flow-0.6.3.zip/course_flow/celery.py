import os
from functools import wraps

import celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "course_flow.settings")

app = celery.Celery("course_flow")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task
def heartbeat():
    pass


def try_async(func):
    """
    From https://github.com/SALTISES4/dalite-ng/blob/master/dalite/celery.py
    Decorator for celery tasks such that they default to synchronous operation
    if no workers are available
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            heartbeat.delay()

        except heartbeat.OperationalError:
            print("Celery unavailable.  Executing synchronously.")
            return func(*args, **kwargs)

        else:
            available_workers = celery.current_app.control.inspect().active()

            if available_workers:
                return func.delay(*args, **kwargs)
            else:
                return func(*args, **kwargs)

    return wrapper
