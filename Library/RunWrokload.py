import time, os, sys


try:
    from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
    from com.android.ddmlib import ShellCommandUnresponsiveException
    from com.android.ddmlib import AndroidDebugBridge, IDevice, MultiLineReceiver
    from java.lang import String

except:
    pass


from CheckAppCrash import CheckAppCrash
from Countdown import Countdown
from RunWorkloadSelect import RunWorkloadSelect
from SetupAndroid import just_return_f_params
from config import *


 
   



def RunWorkload(f_device, f_choice, f_iDevice, f_rec, run_cmd):
    if f_choice == 1:
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)
        MonkeyRunner.sleep(2.0)

        print "====READY TO RUN WORKLOAD===="
        MonkeyRunner.sleep(3.0)
       
        #Select performance suite from main screen
        f_device.touch(170, 350, f_device.DOWN)
        MonkeyRunner.sleep(1.0)
        f_device.touch(170, 350, f_device.UP)

        #Select individual performance workload
        MonkeyRunner.sleep(3.0)
        f_device.touch(170, 220, f_device.DOWN_AND_UP)

        #Press Start
        MonkeyRunner.sleep(3.0)
        f_device.touch(170, 1220, f_device.DOWN_AND_UP)
        
    elif f_choice == 2:
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)
        MonkeyRunner.sleep(2.0)

        print "====READY TO RUN WORKLOAD===="
        MonkeyRunner.sleep(3.0)
       
        #Select performance suite from main screen
        f_device.touch(170, 350, f_device.DOWN)
        MonkeyRunner.sleep(1.0)
        f_device.touch(170, 350, f_device.UP)

        #Select individual performance workload
        MonkeyRunner.sleep(3.0)
        f_device.touch(170, 330, f_device.DOWN_AND_UP)


        #Press Start
        MonkeyRunner.sleep(3.0)
        f_device.touch(170, 1220, f_device.DOWN_AND_UP)
        
    elif f_choice == 3:
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)
        MonkeyRunner.sleep(2.0)

        print "====READY TO RUN WORKLOAD===="
        MonkeyRunner.sleep(3.0)
       
        #Select performance suite from main screen
        f_device.touch(170, 350, f_device.DOWN)
        MonkeyRunner.sleep(1.0)
        f_device.touch(170, 350, f_device.UP)

        #Select individual performance workload
        MonkeyRunner.sleep(3.0)
        f_device.touch(170, 430, f_device.DOWN_AND_UP)

        #Press Start
        MonkeyRunner.sleep(3.0)
        f_device.touch(170, 1220, f_device.DOWN_AND_UP)
        
    elif f_choice == 4:
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)
        MonkeyRunner.sleep(2.0)

        print "====RUN WORKLOAD===="
        MonkeyRunner.sleep(3.0)
       
        #Select performance suite from main screen
        f_device.touch(170, 350, f_device.DOWN)
        MonkeyRunner.sleep(1.0)
        f_device.touch(170, 350, f_device.UP)

        #Select individual performance workload
        MonkeyRunner.sleep(3.0)
        f_device.touch(170, 530, f_device.DOWN_AND_UP)

        #Press Start
        MonkeyRunner.sleep(3.0)
        f_device.touch(170, 1220, f_device.DOWN_AND_UP)
        
    elif f_choice == 5:
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)
        MonkeyRunner.sleep(2.0)

        print "====RUN WORKLOAD===="
        MonkeyRunner.sleep(3.0)
       
        #Select performance suite from main screen
        f_device.touch(170, 350, f_device.DOWN)
        MonkeyRunner.sleep(1.0)
        f_device.touch(170, 350, f_device.UP)

        #Select individual performance workload
        MonkeyRunner.sleep(3.0)
        f_device.touch(170, 630, f_device.DOWN_AND_UP)

        #Press Start
        MonkeyRunner.sleep(3.0)
        f_device.touch(170, 1220, f_device.DOWN_AND_UP)

    elif f_choice == 6:
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)
        MonkeyRunner.sleep(2.0)

        print "====RUN WORKLOAD===="
        MonkeyRunner.sleep(30.0)
       
        #Press NFL icon to reveal menu
        f_device.touch(50, 80, f_device.DOWN)
        MonkeyRunner.sleep(1.0)
        f_device.touch(50, 80, f_device.UP)

        #Select team (49ers) tab
        MonkeyRunner.sleep(10.0)
        f_device.touch(200, 430, f_device.DOWN_AND_UP)
        #f_device.touch(200, 650, f_device.DOWN_AND_UP)

        #Select video tab
        MonkeyRunner.sleep(10.0)
        f_device.touch(400, 200, f_device.DOWN_AND_UP)

        #Select Panthers vs 49ers tab
        MonkeyRunner.sleep(10.0)
        f_device.touch(200, 800, f_device.DOWN_AND_UP)

        #Tap video to see full screen button
        MonkeyRunner.sleep(10.0)
        f_device.touch(200, 800, f_device.DOWN_AND_UP)

        #Press full screen button
        MonkeyRunner.sleep(2.0)
        f_device.touch(650, 850, f_device.DOWN_AND_UP)

        #Wait time for any commercial to be over
        MonkeyRunner.sleep(30.0)

        #sys.exit(2)

    elif f_choice == 7:
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)
        MonkeyRunner.sleep(2.0)

        print "====RUN WORKLOAD===="
        MonkeyRunner.sleep(5.0)
       
        #Press iteration pulldown menu
        f_device.touch(400, 150, f_device.DOWN_AND_UP)


        #Select 100,000 iterations
        MonkeyRunner.sleep(5.0)
        f_device.touch(400, 250, f_device.DOWN_AND_UP)

        #Scroll screen up to see yuv2rgb tab
        MonkeyRunner.sleep(10.0)
        f_device.drag((400, 950),(400,450), 1.0)
        
        #Select yuv2rgb tab
        MonkeyRunner.sleep(5.0)
        f_device.touch(100, 1220, f_device.DOWN_AND_UP)

    elif f_choice == 8:

        #Clear Player data so game always starts with 45 coins
        print "Clear Player data..."
        f_device.shell("pm clear com.leftover.CoinDozer")
        MonkeyRunner.sleep(5.0)
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)
        #MonkeyRunner.sleep(40.0)

        print "====RUN WORKLOAD===="
        #MonkeyRunner.sleep(5.0)
        #Run events
        #f_device.shell("cd /data/suit/; ./sendevents -f /data/suit/coindozer_event_input.txt /dev/input/event7")
        #os.system("adb shell /data/suit/sendevents -f /data/suit/coindozer_event_input.txt /dev/input/event7")
        #f_iDevice.executeShellCommand("cd /data/suit/; ./sendevents -f /data/suit/coindozer_event_input.txt /dev/input/event7", f_rec, 0)

    elif f_choice == 9:

        #Clear Player data so game always starts with 45 coins# | SVN Rev. 6821
        print "Clear Player data..."
        f_device.shell("pm clear com.noodlecake.ssg2")
        MonkeyRunner.sleep(5.0)
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)


        print "====RUN WORKLOAD===="
        
    elif f_choice == 10:
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)
        MonkeyRunner.sleep(2.0)

        print "====RUN WORKLOAD===="
        MonkeyRunner.sleep(5.0)
       
        #Press iteration pulldown menu
        f_device.touch(400, 150, f_device.DOWN_AND_UP)


        #Select 1,000,000 iterations
        MonkeyRunner.sleep(5.0)
        #f_device.touch(400, 250, f_device.DOWN_AND_UP)
        f_device.touch(400, 470, f_device.DOWN_AND_UP)

        #Scroll screen up to see yuv2rgb tab
        #MonkeyRunner.sleep(10.0)
        #f_device.drag((400, 950),(400,450), 1.0)
        
        #Select libyuv compare tab
        MonkeyRunner.sleep(5.0)
        f_device.touch(100, 420, f_device.DOWN_AND_UP)
        
    elif f_choice == 11:
        MonkeyRunner.sleep(15.0)
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)

        print "====RUN WORKLOAD===="

    elif f_choice == 12:
        #Clear data so app runs stable
        print "Clear data..."
        f_device.shell("pm clear air.com.myheritage.mobile")
        MonkeyRunner.sleep(15.0)
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)

        print "====RUN WORKLOAD===="

    elif f_choice == 13:
        
        #Clear data so app runs stable 
        #print "Clear data..."
        #f_device.shell("pm clear com.picadelic.fxguru")
        #MonkeyRunner.sleep(15.0)
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)
        MonkeyRunner.sleep(2.0)
        
        print "====RUN WORKLOAD===="
        MonkeyRunner.sleep(30.0)   
        #sys.exit(0)# | SVN Rev. 6821
        
        #Press START in main window
        print "Press START in main window"
        f_device.touch(730, 500, f_device.DOWN_AND_UP)
        
        #Select satellite crash
        MonkeyRunner.sleep(10.0)
        print "Select satellite crash"
        f_device.touch(300, 200, f_device.DOWN_AND_UP)
        
        #Press START
        MonkeyRunner.sleep(20.0)
        print "Press START"
        f_device.touch(1000, 160, f_device.DOWN_AND_UP)
        
        #Press RECORD
        MonkeyRunner.sleep(20.0)
        print "Press RECORD"
        f_device.touch(630, 650, f_device.DOWN_AND_UP)
        
        #Press Finish
        MonkeyRunner.sleep(40.0)
        print "Press FINISH"
        f_device.touch(630, 654, f_device.DOWN_AND_UP)
        MonkeyRunner.sleep(2.0)
        #MonkeyRunner.sleep(4.0)
        f_device.touch(630, 655, f_device.DOWN_AND_UP)
        MonkeyRunner.sleep(4.0)
        f_device.touch(629, 654, f_device.DOWN_AND_UP)
        MonkeyRunner.sleep(6.0)
        f_device.touch(628, 654, f_device.DOWN_AND_UP)

        #Press OK for Choosing Timing
        print "Wait 20 sec..."
        MonkeyRunner.sleep(20.0)

    elif f_choice == 14:
        
        print "Starting up workload application..."
        f_device.shell(run_cmd)
        MonkeyRunner.sleep(2.0)

        print "====RUN WORKLOAD===="
        MonkeyRunner.sleep(180.0)

        #Stop profiling if app crashed
        CheckAppCrash()
        
        #Tap in window
        print "Tap in window"
        f_device.touch(700, 400, f_device.DOWN_AND_UP)
        
        #Select Utah mission
        MonkeyRunner.sleep(20.0)
        print "Select Utah mission"
        f_device.touch(275, 235, f_device.DOWN_AND_UP)
        
    elif f_choice == 15:


        print "Starting up workload application..."
        print run_cmd
        f_device.shell(run_cmd)

        print "Waiting for App to load..."
        Countdown(60)
        #CheckAppCrash()
        print "=== Starting the Game now ==="
        run_automation = "adb shell ./data/suit/sendevents -f /data/suit/touch_event_input.txt /dev/input/event7"
        os.system(run_automation)
   

    elif f_choice == 16:
       
        print "Starting up workload application..."
        f_device.shell(run_cmd)
        MonkeyRunner.sleep(45.0)
    
        #Tap in screen
        print "Tap in window"
        f_device.touch(614, 463, f_device.DOWN_AND_UP)
        MonkeyRunner.sleep(45.0)
    
            #Select campaign mode
        print "Tap in window"
        
        f_device.touch(1132, 366, f_device.DOWN_AND_UP)
        MonkeyRunner.sleep(2.0)
        
        #Select New Game 
        print "Tap in window"
        f_device.touch(640, 410, f_device.DOWN_AND_UP)
        MonkeyRunner.sleep(2.0)
    
        #Select yes
        print "Tap in window"
        f_device.touch(809, 460, f_device.DOWN_AND_UP)
        MonkeyRunner.sleep(2.0)
    
        #Select Easy Mode
        print "Tap in window"
        f_device.touch(460, 276, f_device.DOWN_AND_UP)
        MonkeyRunner.sleep(30.0)
    
        #Select Tap to Continue
        print "Tap in window"
        f_device.touch(460, 276, f_device.DOWN_AND_UP)
        MonkeyRunner.sleep(60.0)

    elif f_choice == 17:
        
        #Clear Cachs: clears the buffers and cache
        p_time = time.time()
        print "[Clearing Cache]"
        drop_caches_script    = "./data/scripts/drop_caches.sh"
        f_iDevice.executeShellCommand(drop_caches_script, f_rec, 0)
        
        print "--[Starting up workload application]--"
        #am start -n com.intel.gameworkload/.MainActivity -e nrocks 50 -e nsnows 100
        
        print "[Clicking Home Button]"
        f_device.touch(963, 930, f_device.DOWN_AND_UP)
        
        print "[Clicking GameWorkloadLauncher]"
        MonkeyRunner.sleep(5.0)
        f_device.touch(1649, 495, f_device.DOWN_AND_UP)
        
        
        
        print "[Clicking Benchmark] "
        MonkeyRunner.sleep(10.0)
        p_time = time.time()
        print "[Workload Started at] - " + str( p_time)
        f_device.touch(185, 216, f_device.DOWN_AND_UP)
        
        
        #MonkeyRunner.sleep(45.0)
    
    else:
        print "Non existent choice."
        sys.exit(2)
#---------------------------------------------------------------------



if __name__ == "__main__":
    
    f_choice = RunWorkloadSelect()
    f_choice = int(f_choice)
    (f_device, f_iDevice, f_rec) = just_return_f_params()
    RunWorkload(f_device, f_choice, f_iDevice, f_rec, run_cmd)