import config

from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as m

import collections

def prettyConverter(c):
    if type(c) is dict or type(c) is collections.OrderedDict:
        if 'type' in c:
            if c['type'] == 'SINGLE_LINKED':
                res = []
                for n in lt.iterator(c):
                    res.append(prettyConverter(n))
            elif c['type'] == 'BST':
                res = {}
                for k in lt.iterator(om.keySet(c)):
                    res[k] = prettyConverter(om.get(c, k)['value'])
            elif c['type'] == 'PROBING' or c['TYPE'] == 'CHAINING':
                res = {}
                for k in lt.iterator(m.keySet(c)):
                    res[k] = prettyConverter(m.get(c, k)['value'])

        else:
            res = {}
            for k, v in c.items():
                res[k] = prettyConverter(v)

        return res
    else:
        return c