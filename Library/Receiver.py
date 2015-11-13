try:
    from com.android.ddmlib import AndroidDebugBridge, IDevice, MultiLineReceiver
except: 
    pass

class Receiver(MultiLineReceiver):
    def __init__(self):
        MultiLineReceiver.__init__(self)

    def processNewLines(self, lines):
        for line in lines:
            print line
