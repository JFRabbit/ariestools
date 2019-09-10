# ariestools

## Install
pip install ariestools==1.0.1

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
* pendulum parse time
```python
from ariestools import parse
parse("2009-08-01T00:00:00.000").format('YYYY-MM-DD HH:mm:ss.SSS')

```