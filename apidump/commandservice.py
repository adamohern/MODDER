#python

import re, lx, os.path, gc

def commandserviceRef():
  
  kit_path  = lx.eval("query platformservice alias ? {kit_mecco_apidump:}")
  

  text = '<html>\n<body>\n'
  text += '<head><link rel="stylesheet" type="text/css" href="reset.css"><link rel="stylesheet" type="text/css" href="style.css"></head>'

  commands = lx.eval('query commandservice commands ?')
  attributesArray = lx.eval('query commandservice "" ?')

  text += '<h1>commandservice:</h1>\n\n'
  text += '<p><em>query commandservice "" ?</em></p>'

  text += '<ul>\n'
  for attribute in attributesArray:
    text += '<li>'+attribute+'</li>\n'
  text += '</ul>\n'

  text += '\n\n<h2>commands:</h2>\n\n'
  
  f = open(os.path.join(kit_path,'html','commandservice.html'),'w')
  f.write(text)
  f.close()

  
  for command in commands:
    
    text = ""
    
    f = open(os.path.join(kit_path,'html','commandservice.html'),'a')

    text += '<h3>'+command+'</h3>\n'
    text += '<p><span class="light">(query commandservice %s ?)</span></p>' % (command)
    attributesArrayList = '<ul>\n'

    for attribute in attributesArray:
      if (attribute.startswith('command.')) and (attribute.startswith('command.arg') == 0):
        try:
          query = 'query commandservice %s ? %s' % (attribute,command)
          q = lx.eval(query)
          if isinstance(q,(list,tuple)):
            attributesArrayList += '\t<li><strong>'+attribute+':</strong><br />\n\t\t<ul>'
            for v in q:
              if v == '': v = '(n/a)'
              try:
                attributesArrayList += '\n\t\t\t<li>'+ v + '</li>'
              except:
                attributesArrayList += '\n\t\t\t<li>(error)</li>'
            attributesArrayList += '\n\t\t</ul>\n\t</li>\n'
          else:
            try:
              if (str(q) != '') and (str(q) != 'None') and (str(q) != '0'):
                attributesArrayList += '\t<li><strong>%s</strong><br />' % (attribute)
                #attributesArrayList += '%s<br />\n<span class="light">%s</span></li>\n' % (str(q),query)
            except:
              attributesArrayList += '<!--error reading %s--></li>\n' % attribute
        except:
          lx.out('FAILED: query commandservice {%s} ? {%s}' % (attribute,command))


    argNames = lx.eval('query commandservice command.argNames ? %s' % command)
    argTypeNames = lx.eval('query commandservice command.argTypeNames ? %s' % command)
    argUsernames = lx.eval('query commandservice command.argUsernames ? %s' % command)
    argDescs = lx.eval('query commandservice command.argDescs ? %s' % command)
        
    if isinstance(argNames,basestring):
      argNames = [argNames]
      argTypeNames = [argTypeNames]
      argUsernames = [argUsernames]
      argDescs = [argDescs]
    
    attributesArrayList += '<li><strong>command.argNames</strong><br />\n<ul>'
    
    if isinstance(argNames,(list,tuple)):
      
      for i in range(len(argNames)):
        argName = argNames[i]
        try:
          argTypeName = argTypeNames[i]
        except:
          argTypeName = 'unspecified'
        try:
          argDesc = argDescs[i]
          argUsername = argUsernames[i]
        except:
          argDesc = 0
          argUsername = 0
          
        attributesArrayList += '<li><strong>%s:</strong> %s' % (argName,argTypeName)
        if argDesc and argUsername:
          attributesArrayList += '<br />\n<p>(%s: %s)</p>\n</li>\n' % (argUsername,argDesc)
        else:
          attributesArrayList += '</li>\n'
        
      attributesArrayList += '</ul>\n\n'
      
    else:
      attributesArrayList += '<li><span class="light">(none)</span></li></ul>'
    
    attributesArrayList += '</ul>\n</li>\n'

    if attributesArrayList != '<ul></ul>\n':
      text += attributesArrayList+'\n\n\n'
      
    f.write(text)
    f.close()

  text = ""
  f = open(os.path.join(kit_path,'html','commandservice.html'),'a')
  text += '</body>\n</html>'
  f.write(text)
  f.close()
      
  
  
  