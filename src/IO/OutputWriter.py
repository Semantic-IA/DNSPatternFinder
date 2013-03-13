'''
Writes results to the output file

@author: Max Maass
'''
from threading import Lock
class writer():
    def __init__(self,outfile):
        self.fobj = open(outfile, 'a')
        self.writeLock = Lock()
        
    def writeOut(self,url,result):
        try:
            with self.writeLock:
                self.fobj.write(url + ":" + result + "\n")
        except Exception as inst:
            print type(inst)
            print inst
    
    def shutdown(self):
        with self.writeLock:
            self.fobj.close()