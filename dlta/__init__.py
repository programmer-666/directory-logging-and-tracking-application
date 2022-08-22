import os, configparser

conf = configparser.ConfigParser()
conf.read(".conf")

dirs = [x[0] for x in os.walk(conf['DEFAULT']['directory'])]
files = [os.listdir(x) for x in dirs]

print((dirs[0]+"\\"+files[0][0]))
print(os.path.getsize(dirs[0]+"\\"+files[0][0])) # byte
print(os.path.getatime(dirs[0]+"\\"+files[0][0])) # access
print(os.path.getctime(dirs[0]+"\\"+files[0][0])) # metadata change
print(os.path.getmtime(dirs[0]+"\\"+files[0][0])) # modification