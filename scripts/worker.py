#!/usr/bin/env python3
# -*- coding: utf8 -*-

from redis import Redis
from rq import Worker

worker = Worker('default', connection=Redis())
worker.work(logging_level='WARNING')
