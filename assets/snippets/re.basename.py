#python

import re;
def basename(string):
    basename = re.sub('^.*[\/\\\]','',string);
    lx.out('basename: ' + basename);
    return basename;

testString = "C:\Users\Adam\Dropbox\zen\801\cj_Zen\Scripts\cj_fixSymmetry.py"
basename(testString);