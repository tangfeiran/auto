from __future__ import unicode_literals

from django.db import models

# Create your models here.

from ws4redis.redis_store import RedisMessage

class publish_message(object):

    def __init__(self, redis_publisher):
        self.redis_publisher = redis_publisher

    def send(self, msg):
        self.redis_publisher.publish_message(RedisMessage(msg))