#===========================Setup=====================================
#=====================================================================
import os, subprocess

try:
    
    from SetupAndroid import just_connect_android
    

except:
    pass
    

try:
    from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

except:
    pass


##################################################    
   
  
wkld_dir                = "/home/intel/workspace/IcyRocks"
pipeline_dir            = "/mnt/sc-nfs2/incoming/qt/"


emonx_dir               = "/data/emonx_xxxx_02112015_prdS_x64_andlolli50/"
wkld_runtime            = 135 #715 #135 #780

android_setup_script    = "./data/scripts/setup_android_for_tracing.sh"
android_scripts_dir     = "/data/scripts/"
android_wkld_name       = "com.intel.gameworkload/.MainActivity"

hsdes_id                = 0
wkld_name               = "quicktrace_-_icyrocks_1-0-32bit_android-501-x86_-_slm2000-x1_600m-lcat-2gb-em64t_1509"
wkld_ids_loop           = ['0000000061']
run_cmd                 = "am start -S " + android_wkld_name

traceoffsets_dir        = "/home/intel/workspace/IcyRocks/traceoffsets/" + wkld_name + "/"
profile_cmd             = "./emonxcli -j 1000000 -c mrm_counters.txt -sync "
profile_loop            = [1,2,3]
profile_output_dir      = "/home/intel/workspace/IcyRocks/profiles/"
tt_max                  = 0

trigger_indices        = [0,1,2,15,16,17,30,31,32,45,46,47]
cd_emonx_dir           = "cd " + emonx_dir + "; "
cd_android_scripts_dir  = "cd " + android_scripts_dir 


#=====================================================================

def generate_Global_Vars_Static():
    config_print_static ()
    
    f = open('GlobalVaribles123.py' , 'w')

    f.write("#THIS IS GENERATED DIRECTLY FROM generate_Global_Vars_Static Method\n\n")
    
    
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
    
    f.close()


def config_print_static ():
    
    print "[Global Variables]"
    print "\n"
    
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
    

def config_test_static_paths():
    
    print "[CHECKING FOR PATH VALIDITY]"
    
    host_directories = [profile_output_dir]
    android_directories = [emonx_dir, android_scripts_dir,android_setup_script]
    
    print "[Checking the host directories]"
    
    for x in host_directories:
        #print x
        if os.path.exists(x):
            print "[Valid Path] : " + x
    
        else:
            try:
                y = input ("[Enter a Valid Path : ] ")
                print "You have entered: " + y
    
            except:
                y = MonkeyRunner.input("[Enter a Valid Path: ]")
                print "You have entered: " + y
    
    just_connect_android()
    
    print "[Checking the android directories]"
   
    for y in android_directories:
            
        p = subprocess.Popen(['adb','shell','ls',y], stdout = subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate() 
        
        if len(out.split(':')) == 2:
            print "[Not Valid] = " + y 
        
        elif len(out.split(':')) == 1 :
            print "[Valid] = " + y

             
if __name__ == "__main__":
    
    generate_Global_Vars_Static()
    
    #config_print_static()
    
    #config_test_static_paths()
    
    #config_Database_import()
  
