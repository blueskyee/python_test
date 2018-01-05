import redis

def get_connection(host):
    pool = redis.ConnectionPool(host=host, port=6379, db=0)
    return redis.Redis(connection_pool=pool)


def set_hash_key_value_by_name(redis, name, key, value):
    return redis.hset(name, key, value)


def get_hash_key_value_by_name(redis, name, key):
    return redis.hget(name, key)

