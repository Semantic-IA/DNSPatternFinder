'''
Writes results to the output file

@author: Max Maass
'''
from threading import Lock
class writer():
    """writer

    Threadsafe writing to a file from multiple processes
    """
    def __init__(self,outfile):
        self.fobj = open(outfile, 'a') # Open the output file
        self.writeLock = Lock() # Create a lock object for thread safety
        
    def writeOut(self,url,result):
        """writeOut

        Write output to file

        @param url: URL that was processed (string)
        @param result: Resulting queries (string)
        """
        try:
            with self.writeLock:
                self.fobj.write(url + ":" + result + "\n") # Write output
        except Exception as inst: # Notify about exceptions, if any
            print type(inst)
            print inst
    
    def shutdown(self):
        """shutdown

        Cleanly close the file on shutdown.
        """
        with self.writeLock:
            self.fobj.close()