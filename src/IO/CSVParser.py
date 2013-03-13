'''
Parses the input CSV File and provides targets for the workers

@author: Max Maass
'''
from threading import Lock
class Parser():
    def __init__(self,csv_path):
        self.fobj = open(csv_path, 'r')
    
    def getJob(self):
        out = self.fobj.readline()
        while out != "":
            yield out.strip()
            out = self.fobj.readline()
        self.fobj.close()