
#===============================FUNC==================================
# |-------------------------------------------------------
# | def RebootAndroid()
# |     
# | 
# |-------------------------------------------------------    
def RebootAndroid():

    #os.system("python /home/intel/workspace/IcyRocks/connect_android.py")
    
    print "[ADB - REBOOT]"
    p = subprocess.Popen(['adb', 'reboot'])
    #p.communicate()
    #print "Rebooting Android system..."
    #os.system("adb reboot")
        
    print "Waiting for system to boot up..."
    MonkeyRunner.sleep(60.0)
    #time.sleep(60)
    
    #os.system("python /home/intel/workspace/IcyRocks/connect_android.py")
    print "[DONE rebooting]"
#---------------------------------------------------------------------
