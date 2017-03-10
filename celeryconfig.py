# -*- coding: utf-8 -*-

from kombu import (
    Exchange,
    Queue
)

BROKER_URL = "amqp://guest:guest@localhost:5672/zeus"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"

CELERY_DEFAULT_QUEUE = 'default'


CELERY_QUEUES = (
    Queue("default", routing_key='task.#'),
    Queue("for_task_A", Exchange("for_task_A", type='topic'), routing_key="task.#"),
    Queue("for_task_B", Exchange("for_task_B"), routing_key="task_b")
)

CELERY_ROUTES = {
    'tasks.taskA': {"queue": "for_task_A", "routing_key": "task.a"},
    'tasks.taskB': {"queue": "for_task_B", "routing_key": 'task_b'}
 }

CELERY_DEFAULT_EXCHANGE = 'tasks'
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
