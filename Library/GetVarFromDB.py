#===============================FUNC==================================
# |------------------------------------------------------- 
# | def GetVarFromDB()
# |     Get settings and workloads from database and set script global variables.
# |
# | Comments: 
# | o Can't use MySQLdb with jython (monkeyrunner). Calling external python
# |      that does use MySQLdb to get data
# |-------------------------------------------------------

import subprocess, sys


try:
    from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
except:
    pass


def GetVarFromDB(f_wkld_ids_index = None):
    
    if f_wkld_ids_index == None  :
        
        try:
            id_here = MonkeyRunner.input("[Enter The ID Number: ]")
            
            f_wkld_ids_index = str(id_here)
            
        
        except:
            id_here = input ("[Enter The ID Number: ] ")
            
            f_wkld_ids_index = str(id_here)
            pass
        
    f_wkld_ids_index = str(f_wkld_ids_index)
    
    #To modify a global variable you must declare it in this function
    
    global wkld_name, emonx_dir, run_cmd, profile_cmd, tt_max, wkld_dir, wkld_runtime,  hsdes_id, traceoffsets_dir, pipeline_dir
    global android_setup_script, android_scripts_dir, android_wkld_name, trigger_indices, wkld_ids_loop  
    global profile_output_dir , profile_loop, cd_emonx_dir,cd_android_scripts_dir 
    

    #Get database data using external python script. 
    
    pipe = subprocess.Popen(["python","./get_var_from_db.py", (f_wkld_ids_index) ], stdout=subprocess.PIPE)
    result = pipe.stdout.read()
    row = result.split(",")

    #Need to add code to check for NULL/empty vars or set default values in MySql db. (CM 140114)
    
    #ID
    wkld_setup_id           = row[0]
    
    #HOST
    wkld_dir                = row[6]
    traceoffsets_dir        = row[9]
    pipeline_dir            = row[10]
    
    #PLATFORM ANDROID
    emonx_dir               = row[2]
    wkld_runtime            = int(row[8])
    android_setup_script    = "./data/scripts/setup_android_for_tracing.sh"
    android_scripts_dir     = "/data/scripts/"
    android_wkld_name       = "com.intel.gameworkload/.MainActivity"
    
    #WORKLOAD
    hsdes_id                = int(row[1])
    wkld_name               = row[7]
    wkld_ids_loop           = ['0000000061']
    run_cmd                 = row[3]
    
    #PROFILING SETTINGS
    profile_cmd             = row[4]
    profile_loop            = [1,2,3]
    profile_output_dir      = "/home/intel/workspace/IcyRocks/profiles/"
    tt_max                  = int(row[5])
    
    #MISC
    trigger_indices         = [0,1,2,15,16,17,30,31,32,45,46,47]
    cd_emonx_dir            = "cd " + emonx_dir + "; "
    cd_android_scripts_dir  = "cd " + android_scripts_dir 
    run_cmd                 = "am start -S " + android_wkld_name
    
        
    print "[Global Variables]"
    print "\n"
    print "[ID ----------------------------------------- "     + wkld_setup_id 
    
    print "[HOST]"
    print "\t[Workload Dir]:          wkld_dir             = " + wkld_dir
    print "\t[Pipeline Dir.]:         pipeline_dir         = " + pipeline_dir
    
    print "\n"
    print "[EMONX]"
    print "\t[Emonx Dir.]:           emonx_dir             = " + emonx_dir
    print "\t[Emonx Runtime.]:       wkld_runtime          = " + str(wkld_runtime)
    
    
    print "\n"
    print "[ANDROID]"
    print "\t[Android Setup Dir.]:   android_setup_script  = " + android_setup_script
    print "\t[Android Scripts Dir.]: android_scripts_dir   = " + android_scripts_dir
    print "\t[Android Workloa Name]:  android_wkld_name    = " + android_wkld_name
    
    print "\n"
    print "[WORKLOAD]"
    print "\t[HSID]:                 hsdes_id              = " + str(hsdes_id)
    print "\t[Workload name]:        wkld_name             = " + wkld_name
    print "\t[Workload ids loop]:    wkld_ids_loop         = " + str(wkld_ids_loop)
    print "\t[Run Command]:          run_cmd               = " + run_cmd
    
    print "\n"
    print "[PROFILING SETTINGS]"
    print "\t[Trace Offsets Dir.]:    traceoffsets_dir     = " + traceoffsets_dir 
    print "\t[Profiling command]:      profile_cmd         = " + profile_cmd
    print "\t[Profiling loop]:         profile_loop        = " + str(profile_loop)
    print "\t[Profiling output Dir.]:  profile_output_dir  = " + profile_output_dir
    print "\t[TT MAX]:                 tt_max              = " + str(tt_max)
    
    print "\n"
    print "[MISC]"
    print "\t[Trigger Indices]:         trigger_indices     = " + str(trigger_indices)
    print "\t[Cd emonx_dir]:            cd_emonx_dir        = " + cd_emonx_dir
    print "\t[Cd android scr. dir.]:    cd_android_scripts_dir = " + cd_android_scripts_dir
    

def GetVarFromDB_generate_Globalvariables():
    
    f = open('GlobalVaribles1234.py' , 'w')
    
    f.write("#THIS IS GENERATED DIRECTLY FROM GetVarFromDB_generate_Globalvariables Method\n\n")
    
    
    f.write('wkld_dir               ' + '=' + "\"" + wkld_dir  + "\"" + '\n')
    f.write('pipeline_dir           ' + '=' + "\"" + pipeline_dir.strip() + "\"" + '\n')#strip is added because there is seems to be whitespace coming from database
    
    f.write('emonx_dir              ' + '=' + "\"" + emonx_dir + "\"" + '\n')
    f.write('wkld_runtime           =  %d\n' % wkld_runtime)
    
    f.write('android_setup_script   ' + '=' + "\"" + android_setup_script + "\"" + '\n')
    f.write('android_scripts_dir    ' + '=' + "\"" + android_scripts_dir + "\"" + '\n')
    f.write('android_wkld_name      ' + '=' + "\"" + android_wkld_name + "\"" + '\n')
    
    f.write('hsdes_id                =  %d\n' % hsdes_id) 
    f.write('wkld_name              ' + '=' + "\"" + wkld_name + "\"" + '\n')
    f.write("wkld_ids_loop          = {} \n" .format(wkld_ids_loop))
    f.write('run_cmd                ' + '=' + "\"" + run_cmd + "\"" + '\n')
    
    f.write('traceoffsets_dir       ' + '=' + "\"" + traceoffsets_dir   + "\"" + '\n') #any windows related directory with backslash on it will give an error so you have to have double backslash //
    f.write('profile_cmd            ' + '=' + "\"" + profile_cmd + "\"" + '\n')
    f.write("profile_loop           = {} \n" .format(profile_loop))
    f.write('profile_output_dir     ' + '=' + "\"" + profile_output_dir + "\"" + '\n')
    f.write('tt_max                 =  %d\n' % tt_max)
    
    f.write("trigger_indices        = {} \n" .format(trigger_indices))
    f.write('cd_emonx_dir           ' + '=' + "\"" + cd_emonx_dir + "\"" + '\n')
    f.write('cd_android_scripts_dir ' + '=' + "\"" + cd_android_scripts_dir+ "\"" + '\n')
    
    
   
    #f.write(' ' + '=' + "\"" + 7 + "\"" + '\n')

    
    f.close()
    
if __name__ == "__main__":
    GetVarFromDB(62)
    GetVarFromDB_generate_Globalvariables()
    sys.exit(0)
    
    
    try:
        id_here = MonkeyRunner.input("[Enter The ID Number: ]")
        
        GetVarFromDB(str(id_here))
        
    
    except:
        id_here = input ("[Enter The ID Number: ] ")
        
        GetVarFromDB(str(id_here))
        pass
    
   
    
    