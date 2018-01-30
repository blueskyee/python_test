from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest
import py_yaml_parser as yp

class UtilYamlParserTest(unittest.TestCase):
    def setUp(self):
        self.doc = yp.parse_config('config/data_schema_sample.yaml')

    def test_parse_data_subject(self):
        self.assertEqual(yp.parse_data_subject(self.doc),
            'prebid_traffic_log'), 'parse data subject fails.'

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()        
