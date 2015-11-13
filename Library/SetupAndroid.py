
#===============================FUNC==================================
# |------------------------------------------------------- 
# | def SetupAndroid()
# |     Run setup commands and scripts to get Android ready for profiling.
# |
# |
# |-------------------------------------------------------


import subprocess

try:
    from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
    from com.android.ddmlib import ShellCommandUnresponsiveException
    from com.android.ddmlib import AndroidDebugBridge, IDevice, MultiLineReceiver
    #from com.android.monkeyrunner import Package
    
except:
    pass

try : 

    from RebootAndroid import RebootAndroid
    from RootADB import RootADB
    from Receiver import Receiver
    from CheckCPUIdle import CheckCPUIdle

except:
    
    pass

from config import android_setup_script
from config import config_Database_import

def just_connect_android():
    
    print "*****[JUST CONNECT]*****"
    
    print "[Kill adb Server before rebooting]"
    subprocess.call(['adb','kill-server'])
    
    
    p = subprocess.Popen('adb devices', shell =True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate()
    
    try: 
    
        if (output[0] == 'List of devices attached \n\n') or (output[0]== '* daemon not running. starting it now on port 5037 *\n* daemon started successfully *\nList of devices attached \n\n')or (output[0] == 'error: protocol fault (no status)\n') :        
            print "[Device wasn't found!]"
            print "[Run serial script]"
            subprocess.call("python" + " /home/intel/workspace/IcyRocks/connect_android.py", shell=True)
        else:
            pass
    except:
        print "[Device was found!]\n" + output[0]

def just_return_f_params():
    
    print "[Just Returning the Values]: "
    just_connect_android()
    f_device = MonkeyRunner.waitForConnection()
    adb = AndroidDebugBridge.getBridge()
    f_iDevice = adb.getDevices()[0]
    print "[Connected to] : ", f_iDevice  
    
    f_rec = Receiver()
    return (f_device, f_iDevice, f_rec)
    
def SetupAndroid():
  
    print "*****[SETUP ANDROID]*****"
    
    print "[Kill adb Server before rebooting]"
    subprocess.call(['adb','kill-server'])
    
    
    p = subprocess.Popen('adb devices', shell =True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate()
    
    try: 
    
        if (output[0] == 'List of devices attached \n\n') or (output[0]== '* daemon not running. starting it now on port 5037 *\n* daemon started successfully *\nList of devices attached \n\n')or (output[0] == 'error: protocol fault (no status)\n') :        
            print "[Device wasn't found!]"
            print "[Run serial script]"
            subprocess.call("python" + " /home/intel/workspace/IcyRocks/connect_android.py", shell=True)
        else:
            pass
    except:
        print "[Device was found!]\n" + output[0]
    
    p = subprocess.Popen('adb devices', shell =True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate()
    
    try: 
    
        if (output[0] == 'List of devices attached \n\n') or (output[0]== '* daemon not running. starting it now on port 5037 *\n* daemon started successfully *\nList of devices attached \n\n')or (output[0] == 'error: protocol fault (no status)\n') :        
            
            print "[Device wasn't found!]"
            print "[[REBOOT AGAIN]]"
            
            RebootAndroid()  
            
            print "[Run serial script]"
            subprocess.call("python" + " /home/intel/workspace/IcyRocks/connect_android.py", shell=True)
        else:
            pass
    except:
        print "[Device was found!]\n" + output[0]
    
    RootADB()
    
    # |----------------------------------------------------------------
    # | Connects to the current device returning a MonkeyDevice object
    # | used to simulate screen touches and other events. It may also
    # | be used to issue shell commands using device.shell(cmd).
    # | 
    # |----------------------------------------------------------------
    f_device = MonkeyRunner.waitForConnection()

    # Gets the debug bridge for the device currently connected
    adb = AndroidDebugBridge.getBridge()

    # |----------------------------------------------------------------
    # | Gets an IDevice object used to execute adb shell commands
    # | that may throw a ShellUnresponsiveException.
    # |----------------------------------------------------------------
    f_iDevice = adb.getDevices()[0]
    print "[Connected to] : ", f_iDevice   

    # Receives output, if any, from commands executed in shell
    f_rec = Receiver()
    

    # |----------------------------------------------------------------
    # | Preparing Android device for next profiling run
    # |    => Disable EIP randomization
    # |    => Disable Power management
    # |    => Configure to 1P
    # |    => Set constant CPU frequency
    # |    => Install Driver
    # | Comment: Android setup script located in android device script dir
    # |----------------------------------------------------------------
    
    #f_iDevice.executeShellCommand(cd_android_scripts_dir + android_setup_script, f_rec, 0)
    #f_iDevice.executeShellCommand(cd_android_scripts_dir + android_setup_script, f_rec, 0)
    
    f_iDevice.executeShellCommand(android_setup_script, f_rec, 0)
    MonkeyRunner.sleep(5.0)
    
    print "[Clear logcat]"
    #Clear logcat
    
    f_iDevice.executeShellCommand("logcat -c", f_rec,0)
    MonkeyRunner.sleep(15.0)
    
    #ClearCache(f_device)
    CheckCPUIdle()

    return (f_device, f_iDevice, f_rec)
#---------------------------------------------------------------------

if __name__ == "__main__":
   
    #just_connect_android()
    SetupAndroid()

