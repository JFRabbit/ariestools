# ariestools

## Install
pip install ariestools==1.0.4

## Limitation
support python3.7+

## Function

* graphql query
```python
from ariestools import graphql_query

_res_json = graphql_query(query_url, payload)
```
* json path
```python
from ariestools import JsonPath

_json_path = JsonPath()

_json_dict = {'k': 'v'}
print(_json_path.path("$.k", _json_dict))

_json_list = [{'k': 'v'}]
print(_json_path.path("$.[0].k", _json_list))

_json_complex = {'k': [{'k': 'v'}]}
print(_json_path.path("$.k.[0].k", _json_complex))
```
* load json file
```python
from ariestools import load_json
_json = load_json(json_file_path)
```
* get relative path & load yaml
```python
import os
from ariestools import replace_sys_path, load_yaml

_yaml = load_yaml(os.path.realpath('') + replace_sys_path("/.xxx/xxx.yaml"))
```

* parse time
```python
t_time_str = '2019-08-01 00:00:00.000'
t_dt = parse(t_time_str) # 2019-08-01T00:00:00+08:00

print(get_local_time(t_dt)) # 2019-08-01 00:00:00.000
print(get_cloud_time(t_dt)) # 1564588800000000000

t_time_str2 = '2019-08-01 00:00:05.000'
t_dt2 = parse(t_time_str2)

print(get_dt_duration_seconds(t_dt2, t_dt)) # 5

print(t_dt2 > t_dt) # True

print(now()) # 1576224515111
```