#python

import lx, lxu, lxifc, modo, inspect, os, sys, re, commandservice, layerservice, sceneservice, imagesavers, symbols

DUMP_PATH = lx.eval("query platformservice alias ? {kit_KOMODO:html}")
SCRATCH = "scratch.html"
MAX = 10
NL = "\n"
TAB = "    "
EXT = ".html"
DUMP = ['lxu','lx','modo','lxifc']
DIVE = ['module','classobj','dict','type']
PARENTH = ['classobj','method','instancemethod','builtin_function_or_method','method_descriptor']
NODOCS = ['str','dict','float','list','int','long']

def ind(i=1):
    return TAB * i

def n(i=1):
    return NL * i

def t(t,c=None,i=None):
    c = ' class="%s"' % c if c else ''
    i = ' id="%s"' % i if i else ''
    return '<%s%s%s>' % (t,c,i)

def meta(obj,d):
    html = ""
    
    if type(obj).__name__ in NODOCS:
        try:
            html += ind(d) + t("span","meta") + "type: " + type(obj).__name__ + t("/span")
        except:
            pass
    
    else:
        html += ind(d) + t("div","meta") + n()
        
        try:
            html += ind(d+1) + t("p","meta") + "type: " + type(obj).__name__ + t("/p") + n()
        except:
            pass

        try:
            html += ind(d+1) + t("p","meta") + "doc: " + inspect.getdoc(obj) + t("/p") + n()
        except:
            pass    

        try:
            html += ind(d+1) + t("p","meta") + "file: " + inspect.getfile(obj) + t("/p") + n()
        except:
            pass
    
        html += ind(d) + t("/div") + n()
    
    return html
    

def dive(context,name,d=0,pre=""):
    html = ''
    
    obj = getattr(context,name)
    objType = type(obj).__name__
    
    root = re.search('[^.]*',pre) if pre else name
    
    args = ""
    try:
        if inspect.getargspec(obj)[0]:
            args = t("span","meta") + ",".join(inspect.getargspec(obj)[0]) + t("/span")
    except:
        pass
    args = '(%s)' % args if objType in PARENTH else ''
    suff = '()' if objType in PARENTH else ''
    
    
    
    
    html += ind(d) + t('div',"d"+str(d+1) + " wrapper",pre+name) + n()
    html += ind(d) + t("h" + str(d+1)) + pre + name + args + t("/h" + str(d+1)) + n()
    html += meta(obj,d)
    
    pre = pre + name + suff + "."
    
    
    
    
    members = inspect.getmembers(obj)
    html += ind(d) + t("ul")
    html += ind(d) + t("h" + str(d+2)) + re.sub('\.$','',pre) + " contents:" + t("/h" + str(d+2)) + n()
    
    
    membernames = []
    for member in members:
        membernames.append(member[0])
    membernames.sort(key=str.lower)
    
    
    for memberName in membernames:
        if (
            not memberName in DUMP and
            not memberName in pre.split('.')
            ):
            if re.search('^__',memberName):
                html += '<li>%s</li>' % (pre+memberName) + n()
            else:
                html += '<li><a href="#%s">%s</a></li>' % (pre+memberName,pre+memberName) + n()
    html += ind(d) + t("/ul")
    
    
    
    
    for memberName in membernames:
        
        memberObj = getattr(obj,memberName)
        memberObjType = type(memberObj).__name__
        
        args = ""
        try:
            if inspect.getargspec(memberObj)[0]:
                args = t("span","meta") + ",".join(inspect.getargspec(memberObj)[0]) + t("/span")
        except:
            pass
        
        memberSuff = '(%s)' % args if memberObjType in PARENTH else ''
        
        if (
                d<MAX 
                and memberObjType in DIVE 
                and not re.search('^__',memberName) 
                and not memberName in DUMP
                and not memberName in pre.split('.')
            ):
            
            html += n() + dive(obj,memberName,d+2,pre)
            
        elif not memberName in DUMP and not re.search('^__',memberName):
            html += ind(d+1) + t('p',"title",pre+memberName) + pre + memberName + memberSuff + t('/p') + n()
            html += meta(memberObj,d)
            
            
            
            
            
    html += ind(d) + t('/div') + n()
    return html
    
    

def dump():
    try:
        os.makedirs(DUMP_PATH)
    except:
        pass
    
    for module in DUMP:
        html = '<html>' + n()
        html += '<head>' + n()
        html += '<link rel="stylesheet" type="text/css" href="reset.css">' + n()
        html += '<link rel="stylesheet" type="text/css" href="style.css">' + n()
        html += '</head>' + n()
        html += '<body>' + n()
        html += dive(sys.modules[__name__],module)
        html += "</body></html>"
        target = open(os.path.join(DUMP_PATH,module+EXT),'w')
        target.write(html)
        target.close()
        
    reload(sceneservice)
    sceneservice.sceneserviceRef()
        
    reload(layerservice)
    layerservice.layerserviceRef()
        
    #reload(commandservice)
    #commandservice.commandserviceRef()
    
    reload(imagesavers)
    imagesavers.imagesaversRef(DUMP_PATH)
    
    reload(symbols)
    symbols.symbolDump(DUMP_PATH)
    
    lx.eval('python.dumpAPI {%s}' % os.path.join(DUMP_PATH,"dummy"))