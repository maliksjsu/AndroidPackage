

#===============================FUNC==================================
# |-------------------------------------------------------
# | def RestartADB()
# |     
# | 
# |-------------------------------------------------------    

import os
from com.android.monkeyrunner import MonkeyRunner


def RestartADB():
    #print "Restarting adb server..."
    #os.system("adb kill-server && adb start-server")
    #MonkeyRunner.sleep(10)

    print "Checking adb connection status..."
    os.system("adb get-state")
    MonkeyRunner.sleep(5)
#---------------------------------------------------------------------
