from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest
from . import py_redis as redis

class UtilRedisTest(unittest.TestCase):
    def setUp(self):
        self.redis_conn = redis.get_connection('redis', 6379)

    def test_set_value_by_name(self):
        self.assertEqual(redis.set_value_by_name(self.redis_conn,
                                                 'test_name',
				                 'test_value'), 
                         0), 'set value by name fails.'

    def test_get_value_by_name(self):
        self.assertEqual(redis.get_value_by_name(self.redis_conn, 'test_name').pop().decode("utf-8"), 
			 'test_value'), 'get value by name fails.'

    def test_set_hash_key_value_by_name(self):
        self.assertEqual(redis.set_hash_key_value_by_name(self.redis_conn,
                                                          'test_hash_name',
						          'test_key',
                                                          'test_value'), 
                         0), 'set hash key value by name fails.'

    def test_get_hash_value_by_name_key(self):
        self.assertEqual(redis.get_hash_value_by_name_key(self.redis_conn,
                                                          'test_hash_name',
						          'test_key'), 
                         'test_value'), 'get hash value by name key fails.'

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
