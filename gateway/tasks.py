from gateway import celery

import time


@celery.task(bind=True, default_retry_delay=300, max_retries=5)
def add(self, x, y):
    time.sleep(4)
    return x+y