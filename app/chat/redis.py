import os
import redis

redisClient = redis.Redis.from_url(
    os.environ["REDIS_URI"],
    decode_responses=True
)
