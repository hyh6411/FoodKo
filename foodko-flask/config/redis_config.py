import redis


class RedisConfig:
    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'
    REDIS_DB = 5

    # flask_session的配置
    SESSION_KEY = 'flask'
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    PERMANENT_SESSION_LIFETIME = 60*60*24*14
