import os
import configparser

conf = configparser.ConfigParser()
conf.read(".conf")

dirs = [x[0] for x in os.walk(conf['DEFAULT']['directory'])]

print(dirs)