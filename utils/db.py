try:
    import ujson as json
except ImportError:
    import json


import redis
from flask import g
from .rdb_provider import Rdb_Provider


config = json.load(open('config.json'))

REDIS_ADDRESS = config.get('redis_address', 'localhost')
REDIS_PORT = config.get('redis_port', 6379)
REDIS_DB = config.get('redis_db', 1)

db = Rdb_Provider()


def get_redis():
    if 'redis' not in g:
        g.redis = redis.Redis(host=REDIS_ADDRESS, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
    return g.redis
