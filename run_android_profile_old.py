# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.ddmlib import ShellCommandUnresponsiveException
from com.android.ddmlib import AndroidDebugBridge, IDevice, MultiLineReceiver
from java.lang import String
import os
import sys
import string
import getopt

import time
import re

import subprocess
import threading

# |----------------------------------------------------------------
import SetupAndroid, SetupScript
import config






# |----------------------------------------------------------------
# | Setup:
# |  emonx_dir      = Location of MTMON driver/tool inside the android device
# |  android_scripts_dir    = Location of android setup scripts inside the android device. [Hardcoding]
# |  android_setup_script   = Android script to install driver, set CPU freq, etc. Script located in android device. [Hardcoding]
# |  android_wkld_name      = Android name of installed application
# |  run_cmd    	    = Android command to start android workload app. Using adb shell from Linux to issue command.
# |  monkeyrunner_dir       = Location of monkeyrunner toolset needed to run this automation script
# |  profile_cmd            = MTMON tool used to profile workload.
# |  tt_max                 = Number of trace triggers in workload. Range of trace triggers range from 0-(tt_max-1). Set tt_max = 0 if no trace triggers.
# |  wkld_runtime 	    = Workload run time
# |  wkld_name    	    = Trace workload file name
# |
# | SVN Rev. 6821
# |
# | Comments:
# | - Android workload name can be gotten by starting the app and running 
# |        >adb logcat | grep START
# | New:        
# | 0 Added Countdown() function. (Faisal A.)
# | Improvement suggestions:
# | 0 Create cfg files for Trace Point Selection Tool phase
# | 0 Seperate profiles by workload/trigger into folders
# | 0 Add countdown function
# | 0 Install zxJDBC package which provides Python DB interface for Jython and get rid of get_var_from_db.py script(MySQLdb package).
# |----------------------------------------------------------------		



def main():
    
    
    (device, iDevice, rec) = SetupAndroid()
    
   
    
    (tt_loop) = SetupScript(config.tt_max)
    
    sys.exit(0)
    print "TT LOOP =" + str(tt_loop) 

    wkld_choice = RunWorkloadSelect()

    for index in profile_loop:    
         
        for wkld_ids_index in wkld_ids_loop:
            
            print "\n\n"
            print "=====================PROFILING============================="
            
            
            for tt_index in range(0, tt_loop):
            #hack - Switch between upper of lower line (CM 130918) 
            #for tt_index in trigger_indices:

                #Get and set the script global variables from MySQL database for current workload ID
                #GetVarFromDB(wkld_ids_index)

                #print "Executing warm-up run without profiling..."
                #RunWorkload(device, wkld_choice, iDevice, rec)
                #MonkeyRunner.sleep(10.0 + wkld_runtime)

                #sys.exit(0)
                

                print "[Print profiling command]"
                (built_profile_cmd) = BuildProfilingCommand(profile_cmd, tt_index, tt_max, wkld_runtime)
                
                #Add CheckCPUIdle() ???

                print "[Begin profiling]"
                
                
                workload_thread = threading.Thread(RunWorkload(device, wkld_choice, iDevice, rec))
                profile_thread= threading.Thread(Profiling(iDevice, built_profile_cmd, rec))
                
               
                workload_thread.start()
                profile_thread.start()
                
                profile_thread.join()
                workload_thread.join()
                
                print "[sleep for 650 seconds and wait for the workload to finish]"
                MonkeyRunner.sleep(650)
                
                
                CheckAppCrash()
                print "[Finished profiling]"
                
                print "[Transferring files from Android to PC]"
                CopyFilesFromAndroid(index, tt_index, tt_max, wkld_name)

                print "[Sleep 10 seconds]"
                MonkeyRunner.sleep(10.0)
                
                
                # Reboot after capturing profile 
                
                print "[Kill adb Server before rebooting]"
                subprocess.call(['adb','kill-server'])
                
                print "[Rebooting Android]"
                RebootAndroid()  
                 
                (device, iDevice, rec) = SetupAndroid()
                
    print "\n=============END============="

#===============================main program start==================================
main()
