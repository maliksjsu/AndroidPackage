import ConfigParser
config_file_path = '/home/intel/workspace/IcyRocks/Package/Library/config.ini'

Config = ConfigParser.ConfigParser()
print "[Global Variables]"
#options = Config.options(section)
print Config.read(config_file_path )
for sec in  Config.sections():
    for i in  (Config.items(sec)):
        print i
