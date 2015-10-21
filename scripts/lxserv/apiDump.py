#python

import lx, lxu, modo, re, json, sys, os

def dive(name,context,maxdepth=1,depth=0,exceptions=None):
  
  if isinstance(exceptions,dict):
    for k,v in exceptions.iteritems():
      maxdepth = v if k == name else maxdepth
      
  if depth < maxdepth:
    try:
      obj = getattr(context,name)
      a = dir(obj)
      b = {}
      b["name"] = name
      b["docstring"] = obj.__doc__ if obj.__doc__ else None
      b["type"] = type(obj).__name__
      if b["type"] == "instancemethod":
        b["parameters"] = obj.func_code.co_varnames
      if b["type"] == "builtin_function_or_method":
        b["parameters"] = ["unavailable"]
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
    except:
      return None
  
  else:
    return None

class myGreatCommand(lxu.command.BasicCommand):
  
  def __init__(self):
    lxu.command.BasicCommand.__init__(self)
    
  def basic_Execute(self, msg, flags):
    TODO = [
      {
        "name":"lx",
        "context":sys.modules[__name__],
        "depth":2,
        "exceptions":{
          "service":4,
          "object":4
        },
        "outputPath":os.path.normpath(
          "D:/\Box Sync/Adam_WIP/MechanicalColor/sky_py/kit/mecco_sky_py/apidump/lx.json"
        )
      },
      {
        "name":"lxu",
        "context":sys.modules[__name__],
        "depth":4,
        "exceptions":{

        },
        "outputPath":os.path.normpath(
          "D:/Box Sync/Adam_WIP/MechanicalColor/sky_py/kit/mecco_sky_py/apidump/lxu.json"
        )
      },
      {
        "name":"modo",
        "context":sys.modules[__name__],
        "depth":3,
        "exceptions":{

        },
        "outputPath":os.path.normpath(
          "D:/Box Sync/Adam_WIP/MechanicalColor/sky_py/kit/mecco_sky_py/apidump/modo.json"
        )
      }
    ]



    for i in TODO:
      thelist = []
      thelist.append(dive(i["name"],i["context"],i["depth"],0,i["exceptions"]))

      target = open(i["outputPath"],'w')
      target.write(json.dumps(thelist, sort_keys=False, indent=4, separators=(',', ': ')))
      target.close()
    
    
lx.bless(myGreatCommand, "mecco.apidump")