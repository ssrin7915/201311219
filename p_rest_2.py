import os

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        d[row[0]]=row[1].strip()
    return d
	
keyPath=os.path.join(os.getcwd(),'src','key.properties')
key=getKey(keyPath)

print key['dataseoul']
print key['gokr']