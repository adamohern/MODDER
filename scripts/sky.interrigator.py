#python

import lx, re, json

OUTPUT_FILE_NAME = 'C:\Users\Adam\Desktop\dump.json'

def dive(obj,context=sys.modules[__name__],depth=0):
    if depth < 3:
        a = dir(getattr(context,obj))
        b = {}
        if isinstance(a,list):
            for i in a:
                if re.search('__.*__$',i) == None:
                        b[i] = dive(i,getattr(context,obj),depth+1)
#                else:
#                    b[i] = None

        else:
            b = None

        return b
    
    else:
        return "Stop"

dictionary = dive('lx')

target = open(OUTPUT_FILE_NAME,'w')
target.write(json.dumps(dictionary, sort_keys=False, indent=4, separators=(',', ': ')))
target.close()