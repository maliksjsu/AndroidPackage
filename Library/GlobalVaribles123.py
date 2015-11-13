#THIS IS GENERATED DIRECTLY FROM generate_Global_Vars_Static Method

wkld_dir               ="/home/intel/workspace/IcyRocks"
pipeline_dir           ="/mnt/sc-nfs2/incoming/qt/"
emonx_dir              ="/data/emonx_xxxx_02112015_prdS_x64_andlolli50/"
wkld_runtime           =  135
android_setup_script   ="./data/scripts/setup_android_for_tracing.sh"
android_scripts_dir    ="/data/scripts/"
android_wkld_name      ="com.intel.gameworkload/.MainActivity"
hsdes_id                =  0
wkld_name              ="quicktrace_-_icyrocks_1-0-32bit_android-501-x86_-_slm2000-x1_600m-lcat-2gb-em64t_1509"
wkld_ids_loop          = ['0000000061'] 
run_cmd                ="am start -S com.intel.gameworkload/.MainActivity"
traceoffsets_dir       ="/home/intel/workspace/IcyRocks/traceoffsets/quicktrace_-_icyrocks_1-0-32bit_android-501-x86_-_slm2000-x1_600m-lcat-2gb-em64t_1509/"
profile_cmd            ="./emonxcli -j 1000000 -c mrm_counters.txt -sync "
profile_loop           = [1, 2, 3] 
profile_output_dir     ="/home/intel/workspace/IcyRocks/profiles/"
tt_max                 =  0
trigger_indices        = [0, 1, 2, 15, 16, 17, 30, 31, 32, 45, 46, 47] 
cd_emonx_dir           ="cd /data/emonx_xxxx_02112015_prdS_x64_andlolli50/; "
cd_android_scripts_dir ="cd /data/scripts/"
