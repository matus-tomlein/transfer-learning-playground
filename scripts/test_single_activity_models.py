#!/usr/bin/env python3
# -*- coding: utf8 -*-

from single_activity_models import test_for_source, tested_devices
from redis import Redis
from rq import Queue

q = Queue(connection=Redis())

for source_dataset_device in tested_devices:
    source_dataset = source_dataset_device[0]
    source_device = source_dataset_device[1]

    q.enqueue(test_for_source, source_dataset, source_device,
            timeout=5*(3600*24)) # 5 days
