import json

code = 200
#data = json.dumps(["response", {"code":code, "results": {"topic": "topic_name", "valid_dest": "valid_s3_path", "invalid_dest": "invalid_s3_path"}}], separators=(',',':'))
data = json.dumps({'response':{'code':code, 'results': {'topic': 'topic_name', 'valid_dest': 'valid_s3_path'}}})
print(data)

with open("json.txt", "w") as outfile:
    json.dump(data, outfile)

