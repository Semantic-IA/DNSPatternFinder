'''
Parses the input CSV File and provides targets for the workers

@author: Max Maass
'''
class Parser():
    def __init__(self,csv_path):
        self.fobj = open(csv_path, 'r')
    
    def jobGenerator(self):
        """jobGenerator
        
        Iterable. Will yield job URLs for the worker thread.
        @return: URL to work on (string).
        """
        out = self.fobj.readline()
        while out != "":
            yield out.strip()
            out = self.fobj.readline()
        self.fobj.close()