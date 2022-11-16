import os
import time
from celery import Celery
from dotenv import load_dotenv

load_dotenv("../.env")

worker = Celery("tasks")
worker.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
worker.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@worker.task(name="task")
def task(delay, name):
    time.sleep(delay)
    return name
