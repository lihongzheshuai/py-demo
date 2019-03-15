import json
data_file_path = "bitly_usagov_example.txt";
records = [json.loads(line) for line in open(data_file_path)]
print(records[0]['tz'])

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:10])