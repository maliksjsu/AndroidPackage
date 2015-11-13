
#---------------------------------------------------------------------
#===============================FUNC==================================
# |------------------------------------------------------- 
# | def ClearCache()
# |     Clears cache
# | Comments: 
# | o 
# |-------------------------------------------------------
def ClearCache(device): # , iDevice, rec):
    cache_file = "/proc/sys/vm/drop_caches"
    
    print "======= Clearing Cache ========="
    device.shell("sync && echo 3 > /proc/sys/vm/drop_caches")#, rec, 0)
    MonkeyRunner.sleep(3.0)
    print "Checking to see if cache is cleared"
    os.system("adb pull " + cache_file + " " + profile_output_dir)
    print "====== Getting cache file from Android device ======"
    #cache_read = open('/home/skiddyam/Desktop/profiles/drop_caches','r')
    cache_read = open(profile_output_dir + 'drop_caches','r')
    for number in cache_read:
        if number[0] == '3':
            print "======== Cache is clear, continue with profiling ===="
            MonkeyRunner.sleep(3.0)	
            #os.remove('/home/skiddyam/Desktop/profiles/drop_caches')
            os.remove(profile_output_dir + 'drop_caches')
            print "======== Cache file removed ======="		
            continue

        else: 
            logcat_clear(device)#device.shell("cat /proc/sys/vm/drop_caches")#, rec, 0)
            print "===== Cache is not cleared, trying again ==========="
            device.shell("sync && echo 3 > /proc/sys/vm/drop_caches")
            ClearCache(device)
            MonkeyRunner.sleep(3.0)
      
#---------------------------------------------------------------------