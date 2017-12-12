from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest

class UtilYamlParserTest(unittest.TestCase):
    def setUp(self):
        import util_yaml_parser as yp
        self.doc = yp.parse_config('./data_schema_sample.yaml')

    def test_parse_data_subject(self):
        assert(self.doc['data_subject'] 
			== 'prebid_traffic_log'), 'parse data subject fails.' 

    def test_parse_partition(self):
	assert(self.doc['partition']
	                == ['dt', 'agent']), 'parse partition fails.'

    def test_parse_streaming_host(self):
	assert(self.doc['streaming']['host']
			== '127.0.0.1'), 'parse streaming host fails.'

    def test_parse_schema_col_type(self):
	assert(self.doc['schema']['timestamp']['type']
			== 'bigint'), 'parse schema column type fails.'

    def test_parse_schema_col_max_value(self):
	assert(self.doc['schema']['bid_price']['max_value']
			== 100.0), 'parse schema column max value fails.'

    def test_parse_schema_col_valid_value(self):
	assert(self.doc['schema']['seller_id']['valid_value']
			== [6, 12, 45]), 'parse schema column valid value fails'

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
