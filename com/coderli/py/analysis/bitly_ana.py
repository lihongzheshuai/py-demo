import json

data_file_path = "bitly_usagov_example.txt";
records = [json.loads(line) for line in open(data_file_path)]
# print(records[0]['tz'])

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
# print(time_zones[:10])

from pandas import DataFrame, Series
# import pandas as pd
# import numpy as np
data_frame = DataFrame(records)
# 计数
# print(data_frame["tz"].value_counts()[:10])
print(data_frame["tz"][:14])
clean_tz = data_frame["tz"].fillna("Missing")
print(clean_tz[:14])
clean_tz[clean_tz == ""] = "Unknown"
print(clean_tz[:14])
import matplotlib.pyplot as plt
clean_tz.value_counts()[:10].plot(kind="barh",rot=0)

print(123)