import json

code = 200
result_dict = {'topic': 'topic_name', 'valid_dest': 'valid_s3_path'}
result_dict = {'error_msg': 'error from service'}
data = json.dumps({'response':{'code':code, 'results': result_dict}}, 
                  indent=4, separators=(',', ': '))
print(data)

with open("json.txt", "w") as outfile:
    json.dump(data, outfile)

