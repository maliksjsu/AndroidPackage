
#===============================FUNC=================st=================			
# |------------------------------------------------------- 
# | 1. Run workload
# | 2. Kill workload
# | 
# | Note: device or iDevice NOT used for killing app
# |       because grep is not installed on tablet
# |-------------------------------------------------------

try:
    from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
except:
    pass

def RunWorkloadSelect(f_choice = None):    
    
    print "====================================================================="
    print "= Choose workload to run (1-5):"
    print "=   1: MobileXPRT->Performance Tests->Apply Photo Effects"
    print "=   2: MobileXPRT->Performance Tests->Create Photo Collages"
    print "=   3: MobileXPRT->Performance Tests->Create Slideshow"
    print "=   4: MobileXPRT->Performance Tests->Encrypt Personal Content"
    print "=   5: MobileXPRT->Performance Tests->Detect Faces to Organize Photos"
    print "=   6: Mobile NFL"
    print "=   7: Houdini Micros: NFL Mobile Micro"
    print "=   8: Coin Dozer"
    print "=   9: SSG2 (Super Stickman Golf 2)"
    print "=   10: Houdini Micros: Libyuv Compare"
    print "=   11: Slotomania"
    print "=   12: MyHeritage"
    print "=   14: Frontline Commandos: D-Day->Utah"
    print "=   15: Need for speed: Most Wanted"
    print "=   16: Modern Combat 4: Zero Hour"
    print "=   17: IcyRocks"
    print "====================================================================="
    
    if not f_choice :
        
        try:
            f_choice = MonkeyRunner.input("[Enter The ID Number]:  ")
        
        except:
            f_choice = input ("[Enter the ID Number]:  ")
            
            pass
    
    print "[You have Selected] : " + str(f_choice)
    return f_choice

if __name__ == "__main__":
    
    RunWorkloadSelect()
#---------------------------------------------------------------------
    