import time
import serial
import os
import re
import io
import subprocess

ip_found = None
def serial_data(port, baudrate):
    
    ser = serial.Serial(port, baudrate)
    ser.close()
    
    ser.open()
    ser.write("\r\nsu\n")
    time.sleep(10)
    ser.write("\r\nnetcfg eth0 dhcp\n")
    time.sleep(10)
    ser.write("\r\nnetcfg\n")
    time.sleep(10)
    
    while True:
        yield ser.readline()
    
    
    ser.close()

for line in serial_data('/dev/ttyUSB0', 115000):
    print line
    found = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',line)
    if found:
        if found[0].startswith("172"):
            print found[0]
            ip_found = found[0]
            break
        
    
print "Found it: "+str(ip_found)
os.system("adb connect " + ip_found)
'''
#picocom -b 115200 -r -l /dev/ttyUSB0

#ser = serial.Serial('/dev/ttyUSB0', timeout=None, baudrate=115000, xonxoff=False, rtscts=False, dsrdtr=False) 
ser = serial.Serial('/dev/ttyUSB0', timeout=0, baudrate=115000, parity=serial.PARITY_EVEN, rtscts=1)

ser.close()
ser.baudrate=115200
ser.open()

#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))


time.sleep(10)
#sio.write(unicode ("\r\nsu\n"))

ser.write("\r\nsu\n")
#print sio.readline()
print sio.readline()



time.sleep(10)
#sio.write("\r\nnetcfg eth0 dhcp\n")
ser.write("\r\nnetcfg eth0 dhcp\n")
time.sleep(10)
print sio.readline()

ser.write("\r\nnetcfg\n")
sio.flush()
print sio.readline()

ser.write("\r\nnetcfg\n")

read= ser.read(100)
print read

#time.sleep(3)
#os.system("adb connect 172.20.4.180")

'''

def _readline():
    eol = b'\r'
    leneol = len(eol)
    line = bytearray()
    while True:
        c = self.ser.read(1)
        if c:
            line += c
            if line[-leneol:] == eol:
                break
        else:
            break
    return bytes(line)


def sudo_exec(cmdline, passwd):
    
    osname = platform.system() # 1
    if osname == 'Linux':
        prompt = r'\[sudo\] password for %s: ' % os.environ['USER']
    elif osname == 'Darwin':
        prompt = 'Password:'
    else:
        assert False, osname

    child = pexpect.spawn(cmdline)
    idx = child.expect([prompt, pexpect.EOF], 3) # 2
    if idx == 0: # if prompted for the sudo password
        log.debug('sudo password was asked.')
        child.sendline(passwd)
        child.expect(pexpect.EOF)
    return child.before
#ser.write("\nnetcfg")

#while True:
    #print ser.readline()
    #ser.write("\r\nnetcfg\n")
    
    #rcv = readlineCR(ser)
    #ser.write("\r\nYou sent:" + repr(rcv))


'''
ser.write("su")
time.sleep(3)
ser.write("netcfg eth0 dhcp")
time.sleep(3)
ser.write("netcfg")
'''
'''

if ser.isOpen():
    
    ser.flushInput() #flush input buffer, discarding all its contents
    ser.flushOutput()#flush output buffer, aborting current output 
else: 
    pass

                     #and discard all that is in buffer
    
while True :
    # Check whether the user has typed anything (timeout of .2 sec):
    inp, outp, err = select.select([stdin ,ser], [], [], .2)

    # If the user has typed anything, send it to the Arduino:
    if sys.stdin in inp :
        line = sys.stdin.readline()
        ser.write(line)

    # If the Arduino has printed anything, display it:
    if ser in inp :
        line = ser.readline().strip()
        print "Arduino:", line
'''