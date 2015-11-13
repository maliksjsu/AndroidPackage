#===============================FUNC==================================
# |-------------------------------------------------------
# | def Profiling()
# |     Run emonxcli.
# | 
# |-------------------------------------------------------
def Profiling(f_iDevice, f_profile_cmd, f_rec):
    #time.sleep(15.1)
    p_time = time.time()
    print "[Profiling Started at] - " +  str(p_time)
    print "[Executing trigger command]...\n" + f_profile_cmd
    f_iDevice.executeShellCommand(cd_emonx_dir + f_profile_cmd, f_rec, 0) 
    
    print "[Profiling Done]"
    MonkeyRunner.sleep(3.0)

#---------------------------------------------------------------------
