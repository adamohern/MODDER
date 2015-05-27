#python

import re;
def pathname(string):
    pathname = re.findall('^.*[\/\\\]',string);
    try:
        lx.out('pathname: ' + pathname[0]);
        return pathname[0];
    except:
        lx.out('no pathname found');
        return false;

testString = "C:\Users\Adam\Dropbox\zen\801\cj_Zen\Scripts\cj_fixSymmetry.py"
pathname(testString);