import pandas as pd

test_str='revenue_report.sql'
##split string
print('first part substr:{}'.format(test_str.split(".",1)[0]))
print('second part substr:{}'.format(test_str.split(".",1)[1]))
print test_str.split(".",1)
print test_str.split("@",0)

##reverse string
print(test_str[::-1]) 
print(test_str[6::-1])

##find
test_substr='re'
print(test_str.find(test_substr))
print(test_str.find(test_substr, 5))

