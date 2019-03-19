import json

data_file_path = "bitly_usagov_example.txt";
records = [json.loads(line) for line in open(data_file_path)]
# print(records[0]['tz'])

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
# print(time_zones[:10])

from pandas import DataFrame, Series
import numpy as np
# import pandas as pd
data_frame = DataFrame(records)
# 计数
# print(data_frame["tz"].value_counts()[:10])
print(data_frame["tz"][:14])
clean_tz = data_frame["tz"].fillna("Missing")
print(clean_tz[:14])
clean_tz[clean_tz == ""] = "Unknown"
print(clean_tz[:14])
# 浏览器、设备、应用程序信息
print(data_frame["a"][50])

_in_frame = [x.split()[0] for x in data_frame.a.dropna()]
results = Series(_in_frame)
print(results[:5])
print(results.value_counts()[:8])

c_frame = data_frame[data_frame.a.notnull()]
print(c_frame["a"][:5])
o_sys = np.where(c_frame["a"].str.contains("Windows"),"Windows","Not Windows")
print(o_sys[:10])

# import matplotlib.pyplot as plt
# clean_tz.value_counts()[:10].plot(kind="barh",rot=0)
# plt.show()
