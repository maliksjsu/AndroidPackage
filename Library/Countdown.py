
#=====================================================================
def Countdown(f_time):
   for i in range(f_time,0,-1):

   	print 'Script execution will resume in %d seconds\r' % i,
   	MonkeyRunner.sleep(1.0)
   print ""
#---------------------------------------------------------------------
