

#===============================FUNC==================================
# |------------------------------------------------------- 
# | def CheckCPUIdle()
# |     Check that CPU is idle
# | Comments: 
# | o 
# |-------------------------------------------------------

import time, os, re, sys, string
import subprocess
from RebootAndroid import RebootAndroid

def CheckCPUIdle():

    cpu_idle = 0.0

    print "========== Checking if CPU is idle  ========"
    while (cpu_idle < 98.0):
        time.sleep(5)
        os.system("adb shell top -n 1 -m 5 > /home/intel/workspace/IcyRocks/top_text.txt")

        top_file = open('/home/intel/workspace/IcyRocks/top_text.txt','r')
        
        i = 0
        d = {}
        
        for line in iter(top_file.readline, ''): 
            txt = line.rstrip() 
            if re.match("User", txt):
                loading_int = re.findall("([+]?\d+[\.]?\d*?)", txt)
                d["loading_int" + str(i)] = loading_int  
                i = i +1 
        
        cpu_idle0 = sum( map(int, d['loading_int0']))
        cpu_idle = 100.0 - float(cpu_idle0)
        print "[CPU Idle] = " + str(cpu_idle) + "%"

def CheckCPUIdle_old():
    
    start = time.time()
    print "========== executing top command  ========"
    time.sleep(5)
    run_top = "adb shell top -n 1 -m 5 > top_test.txt"
    os.system(run_top)
    
    top_file = open('/home/skiddyam/top_test.txt','r')
    print "== Checking pattern =="

    for line in top_file:
        str = line 
        match = re.search(r'User \d+%', str)
        if match:
            print 'found',match.group()
            fields = string.split(match.group(), ' ')
            print fields[1]
        if fields[1] <= '2%':
            #if match.group(1) <= '0%':
            print "=== CPU is at 0% proceeding with collection ==="
            continue
        else:
            print "=== CPU is not at 0%, checking again ==="
            CheckCPUIdle()
            end = time.time() - start
            print end

if __name__ == "__main__":
    
    p = subprocess.Popen('adb devices', shell =True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate()
    
    try: 
    
        if (output[0] == 'List of devices attached \n\n') or (output[0]== '* daemon not running. starting it now on port 5037 *\n* daemon started successfully *\nList of devices attached \n\n')or (output[0] == 'error: protocol fault (no status)\n') :        
            print "[Device wasn't found!]"
            print "[Run serial script]"
            subprocess.call("python" + " /home/intel/workspace/IcyRocks/connect_android.py", shell=True)
        else:
            print "[Device was found!]\n"
            pass
            
    except:
        print "[Device wasn't found EVEN AFTER RUNNING THE SCRIPT!]\n" + output[0]
        sys.exit(1)
        
    CheckCPUIdle()
    