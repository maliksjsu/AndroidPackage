#---------------------------------------------------------------------

#===============================FUNC==================================
# |------------------------------------------------------- 
# | def SetupScript()
# |     Set the tt_loop paramater.
# | Comments: f_iDevice.executeShellCommand(cd_emonx_dir + f_profile_cmd, f_rec, 0)
# | o 
# |-------------------------------------------------------



from config import tt_max
def SetupScript(f_tt_max):

    if (f_tt_max > 0):
        #Set if trace triggering
        f_tt_loop = f_tt_max
    else:
        f_tt_loop = 1
    
    return f_tt_loop

 
  
#---------------------------------------------------------------------
if __name__ == "__main__":
    
    SetupScript(tt_max)
    
    
    