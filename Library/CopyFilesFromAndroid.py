
#===============================FUNC==================================
# |-------------------------------------------------------
# | def CopyFilesFromAndroid(f_iDevice, f_index, f_rec)
# |     
# | 
# |-------------------------------------------------------

import subprocess, os, string
from config import *


def CopyFilesFromAndroid(f_index, f_tt_index, f_tt_max, f_wkld_name):
    
    new_f_wkld_name = ""
    
    if( f_tt_max > 0):
        
        wkld_name_fields = string.split(f_wkld_name, '_')

        #Assemble name
        new_f_wkld_name  = wkld_name_fields[0] + "_"
        new_f_wkld_name += wkld_name_fields[1] + "_"
        new_f_wkld_name += wkld_name_fields[2] + "-"
        new_f_wkld_name += str(f_tt_index) + "_"
        new_f_wkld_name += wkld_name_fields[3] + "_"
        new_f_wkld_name += wkld_name_fields[4] + "_"
        new_f_wkld_name += wkld_name_fields[5] + "_"
        new_f_wkld_name += wkld_name_fields[6] + "_"
        new_f_wkld_name += wkld_name_fields[7] + "_"
        new_f_wkld_name += wkld_name_fields[8]
        new_f_wkld_name += "-p" + str(f_index) + ".emon.txt"

    else:
        new_f_wkld_name = f_wkld_name + "-p" + str(f_index) + ".emon.txt"

    print "[Get emonx.txt and save as]: /n" + profile_output_dir + new_f_wkld_name 
    os.system("adb pull " + emonx_dir + "emonx.txt" + " " + profile_output_dir + new_f_wkld_name)
    os.system("adb shell rm " + emonx_dir + "emonx.txt")
    
    print"[Get the Screen Shot and Save it] as: / "  + profile_output_dir + new_f_wkld_name+".png"
    subprocess.call(['adb', 'shell' , 'screencap', '-p' , '/sdcard/screen.png'])
    subprocess.call(['adb', 'pull','/sdcard/screen.png', profile_output_dir+new_f_wkld_name+".png"])
    subprocess.call(['adb', 'shell' , 'rm', '/sdcard/screen.png'])
#---------------------------------------------------------------------
