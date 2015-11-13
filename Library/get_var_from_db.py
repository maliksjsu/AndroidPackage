import pymysql, sys


#===============================FUNC==================================
# |------------------------------------------------------- 
# | def GetVarFromDB()
# |     Get settings and workloads from database and set script global variables.
# |
# |
# |-------------------------------------------------------
def connect():
    
    print "Current id is: ", str(sys.argv[1])
    
    f_wkld_ids_index = sys.argv[1]
    
    #f_wkld_ids_index = '62'
    db = pymysql.connect(host="172.20.4.248",user="intel",passwd="intel123",db="wkld_db",port=3306)
    cursor = db.cursor()
    #cursor.execute("SHOW ENGINES")
    cursor.execute("SELECT * FROM wkld_setup WHERE id IN(" + f_wkld_ids_index + ")")
    
    #Need to add code to check for NULL/empty vars or set default values in MySql db. (CM 140114)
    for row in cursor.fetchall():
        wkld_setup_id   = row[0]
        hsdes_id	    = row[1]
        emonx_dir       = row[2]
        run_cmd         = row[3]
        trigger_cmd     = row[4]
        tt_max          = int(row[5])
        wkld_dir        = row[6]
        wkld_name       = row[7]
        wkld_runtime    = int(row[8])
        traceoffsets_dir = row[9]
        pipeline_dir    = row[10]
            

        print str(wkld_setup_id) + "," + str(hsdes_id) + "," + emonx_dir + "," + run_cmd + "," + trigger_cmd + "," + str(tt_max) + "," + wkld_dir + "," + wkld_name + "," + str(wkld_runtime)  + "," + traceoffsets_dir  + "," + pipeline_dir
        
    cursor.close()
    db.close()

connect()
#---------------------------------------------------------------------
