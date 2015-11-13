#---------------------------------------------------------------------
#===============================FUNC==================================
# |------------------------------------------------------- 
# | def CheckAppCrash()
# |     Check if Android app crashed
# | Comments: 
# | o 
# |-------------------------------------------------------

import os, sys, re



from config import *



def CheckAppCrash():
    output = ""
    match = ""
    print "output before is: " + output
    output = os.popen("adb logcat -d CRASH:E *:S").readlines()
    match = re.search(r'CRASH', str(output))
    print "match = "
    print match
    if match:
        print "Output is:"
        print output
        sys.exit(2)

if __name__ == "__main__":
    CheckAppCrash()
    
    
    
    
#---------------------------------------------------------------------