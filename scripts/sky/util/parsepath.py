#python

import lx
import re

def marco():
	return "polo!"

def basename(string):
	basename = re.sub('^.*[\/\\\]','',string)
	try:
		lx.out('basename: ' + basename);
		return basename;
	except:
		lx.out('no basename found')
		return false;
	
def pathname(string):
	pathname = re.findall('^.*[\/\\\]',string);
	try:
		lx.out('pathname: ' + pathname[0]);
		return pathname[0];
	except:
		lx.out('no pathname found');
		return false;