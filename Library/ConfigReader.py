import configparser
def readConfigData(section,key):
    global config
    config=configparser.ConfigParser()
    config.read("..\\Config\\conf.cfg")
    return config.get(section,key)

def readele(section,key):
    config.read("..\\Config\\Elements.cfg")
    return config.get(section,key)