import json

print(json.dumps({'key1': 1, 'key2':2}))
sample_file = open('test_data/10.20.32.40.feed','r')
sample_file_json = json.load(sample_file)
print(sample_file_json['core.resources']['connections'])