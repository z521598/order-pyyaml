# -* encoding:utf-8 -*-
from collections import OrderedDict

import yaml
import yamlparser

# 测试json.load
path = 'load.yml'
result = yaml.load(open(path))
"""
result:
{'p2': 2, 'p3': 3, 'p1': 1, 'p4': 4, 'p5': 5}
"""

# 测试json.dump
pydir = {}
cdir = {}
pydir['c'] = cdir
cdir['rep1'] = 1
cdir['csd2'] = 2
cdir['fs3'] = 3
cdir['asd4'] = 4
cdir['ioweq5'] = 5
cdir['asd6'] = 6
res = yaml.dump(pydir, open('dump.yml', 'w'), default_flow_style=False)
"""
res:
c:
  asd4: 4
  asd6: 6
  csd2: 2
  fs3: 3
  ioweq5: 5
  rep1: 1

"""

# 测试yamlparser.ordered_yaml_load
result2 = yamlparser.ordered_yaml_load(path)
"""
resukt2:
OrderedDict([('p1', 1), ('p2', 2), ('p3', 3), ('p4', 4), ('p5', 5)])

"""
# 测试yamlparser.ordered_yaml_dump
pydir2 = {}
cdir2 = OrderedDict()
pydir2['c'] = cdir2
cdir2['rep1'] = 1
cdir2['csd2'] = 2
cdir2['fs3'] = 3
cdir2['asd4'] = 4
cdir2['ioweq5'] = 5
cdir2['asd6'] = 6
res2 = yamlparser.ordered_yaml_dump(pydir2, open('dump.yml', 'w'), default_flow_style=False)
"""
res2:
c:
  rep1: 1
  csd2: 2
  fs3: 3
  asd4: 4
  ioweq5: 5
  asd6: 6
"""
