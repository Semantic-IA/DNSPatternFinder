'''
Parses the input CSV File and provides targets for the workers

@author: Max Maass
'''
class Parser():
    def __init__(self,csv_path):
        self.fobj = open(csv_path, 'r')
    
    def getJob(self): # TODO: Rename? Something like JobGenerator? Strictly speaking, it is an iterable, not a function
        """getJob
        
        Iterable. Will yield job URLs for the worker thread.
        @return: URL to work on (string).
        """
        out = self.fobj.readline()
        while out != "":
            yield out.strip() # TODO: Check for format before yielding (leading http://?)
            out = self.fobj.readline()
        self.fobj.close()