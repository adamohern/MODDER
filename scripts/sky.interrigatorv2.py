#python

import lx, lxu, re, json

TODO = [
    {
        "name":"lx",
        "context":sys.modules[__name__],
        "depth":2,
        "exceptions":{
            "service":4,
            "object":4
        },
        "outputPath":"C:\Users\Adam\Desktop\lx.json"
    },
    {
        "name":"lxu",
        "context":sys.modules[__name__],
        "depth":1,
        "exceptions":{

        },
        "outputPath":"C:\Users\Adam\Desktop\lxu.json"
    }
]

def dive(name,context,maxdepth=1,depth=0,exceptions=None):
    
    if isinstance(exceptions,dict):
        for k,v in exceptions.iteritems():
            maxdepth = v if k == name else maxdepth
            
    if depth < maxdepth:
        obj = getattr(context,name)
        a = dir(obj)
        b = {}
        b["name"] = name
        b["docstring"] = obj.__doc__ if obj.__doc__ else None
        if isinstance(a,list):
            c = []
            if depth < maxdepth - 1:
                for i in a:
                    if re.search('__.*__$',i) == None:
                        c.append(dive(i,obj,maxdepth,depth+1,exceptions))
            else:
                for i in a:
                    if re.search('__.*__$',i) == None:
                        c.append(i)
            
            if len(c) != 0:
                b["children"] = c

        else:
            b = None

        return b
    
    else:
        return None

for i in TODO:
    thelist = []
    thelist.append(dive(i["name"],i["context"],i["depth"],0,i["exceptions"]))

    target = open(i["outputPath"],'w')
    target.write(json.dumps(thelist, sort_keys=False, indent=4, separators=(',', ': ')))
    target.close()

