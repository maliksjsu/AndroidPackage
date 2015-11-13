#===========================Setup=====================================
#=====================================================================
emonx_dir           = "/data/emonx_xxxx_02112015_prdS_x64_andlolli50/"

android_scripts_dir     = "/data/scripts/"

android_setup_script    = "./data/scripts/setup_android_for_tracing.sh"

android_wkld_name       = "com.intel.gameworkload/.MainActivity"

profile_output_dir      = "./home/intel/workspace/IcyRocks/profiles/"

profile_cmd             = "./emonxcli -j 1000000 -c mrm_counters.txt -sync "

tt_max                  = 0

wkld_runtime            = 135 #715 #135 #780

wkld_name               = "quicktrace_-_icyrocks_1-0-32bit_android-501-x86_-_slm2000-x1_600m-lcat-2gb-em64t_1509"



#monkeyrunner_dir = ""
# ---
profile_loop        = [1,2,3]
#trigger_indices        = [0,1,2,15,16,17,30,31,32,45,46,47]
cd_emonx_dir           = "cd " + emonx_dir + "; "
cd_android_scripts_dir  = "cd " + android_scripts_dir 
run_cmd              = "am start -S " + android_wkld_name
wkld_ids_loop        = ['0000000061']
#=====================================================================
#======================================================