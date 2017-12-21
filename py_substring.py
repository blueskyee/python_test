import pandas as pd

test_str='revenue_report.sql'
print('first part substr:{}'.format(test_str.split(".",1)[0]))
print('second part substr:{}'.format(test_str.split(".",1)[1]))
print test_str.split(".",1)
print test_str.split("@",0)
