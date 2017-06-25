#!/usr/bin/env python3
# -*- coding: utf8 -*-

from redis import Redis
from rq import Queue

q = Queue("default", connection=Redis())
print(q.count)
q.empty()
print(q.count)
