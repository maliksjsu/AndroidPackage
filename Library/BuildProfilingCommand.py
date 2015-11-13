
#===============================FUNC==================================
# |------------------------------------------------------- 
# | def BuildProfilingCommand()
# |     Build trigger command from args based on emonx trace collection specification
# | Comments: 
# | o 
# |-------------------------------------------------------
def BuildProfilingCommand(f_profile_cmd, f_tt_index, f_tt_max, f_wkld_runtime):
    
    if( f_tt_max > 0):
        f_profile_cmd += " -tt " + str(f_tt_index)
    else:
        f_profile_cmd += " -s " + str(f_wkld_runtime)
    
    print "****EMONX Profiling command   : ", f_profile_cmd
    
    
    return (f_profile_cmd)

   