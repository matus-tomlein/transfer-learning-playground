#!/usr/bin/env python3
# -*- coding: utf8 -*-

from single_activity_models import test_for_source, devices_in_dataset
from redis import Redis
from rq import Queue

datasets = [
    "synergy-final-iter1",
    "synergy-final-iter2",
    "scott-final-iter1",
    "robotics-final",
    "synergy-final-iter4",
    "synergy-final-iter5"
]

q = Queue(connection=Redis())
for source_dataset in datasets:
    devices = devices_in_dataset(source_dataset)

    for source_device in devices:
        q.enqueue(test_for_source, source_dataset, source_device)
        break
    break
