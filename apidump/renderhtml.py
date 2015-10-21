#python

import json, re, os

FILES = ['lxu.json','lx.json','modo.json']
DEBUG_MODE = False

for FILE in FILES:

  thefile = open(FILE,'r')
  thejson = json.loads(thefile.read())

  TAB = "  "
  NL = "\n"

  def h(s,d):
      d = min(d,6)
      return ind(d) + "<h" + str(d) + ">" + s + "</h" + str(d) + ">" + NL

  def s(s,c=""):
      return "<span class=\"" + c + "\">" + s + "</span>"

  def ind(d):
      return TAB * d

  def div(s,d):
      return ind(d) + "<div class=\"d" + str(d) + "\">" + NL + s + NL + ind(d) + "</div>" + NL

  def p(s,d,c=""):
      if c:
          c = " " + c
      if s:
          return ind(d) + "<p class=\"d" + str(d) + c + "\">" + s + "</p>" + NL
      else:
          return ""

  def iterate(obj, d = 0, pre = ""):
      html = ""
      if pre != "" and not re.search("\.$",pre):
          pre += "."
      if d < 15:
          if isinstance(obj, dict):
              t = obj["type"] if obj.has_key("type") else "unspecified"
              params = ",".join(obj["parameters"]) if obj.has_key("parameters") else ""
              params = "?" if params == "unavailable" else params
              suff = ""
              suff = "("+s(params,"lo")+")" if t == "function" or t == "classobj" or t == "instancemethod" or t == "method_descriptor" or t == "builtin_function_or_method" else suff
              if obj.has_key("name"):
                  html += h(pre + s(obj["name"],"hi " + t) + suff,d)
              html += p(t,d,"objectType " + t)
              if obj.has_key("docstring") and obj["docstring"]:
                  html += p(s(obj["docstring"]),d,"docstring")
              if obj.has_key("children"):
                  if isinstance(obj["children"],str):
                      html += p(obj["children"],d)
                  else:
                      html += div(iterate(obj["children"],d + 1,pre + s(obj["name"],t) + suff),d) + NL

          elif isinstance(obj, list):
              for i in obj:
                  if isinstance(i,str):
                      html += p(pre + s(i),d)
                  else:
                      html += div(iterate(i,d + 1,pre),d)

          else:
              html += p(str(obj),d)

      return html

  html = "<html><head>" + NL
  html += "<link rel=\"stylesheet\" type=\"text/css\" href=\"reset.css\" />" + NL
  html += "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" />" + NL
  html += "</head><body>" + NL
  html += iterate(thejson) + NL
  html += "</body></html>"

  target = open(os.path.splitext(os.path.basename(FILE))[0]+".html",'w')
  target.write(html)
  target.close()
