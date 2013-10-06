'''
WorkerThread to run the external Program and capture the output.

@author: Max Maass
'''
import threading
from subprocess import Popen, PIPE
from sys import stderr

class Thread(threading.Thread):
    def __init__(self,pjs_path, ndjs_path, gen, ow, stat):
        """Initialize Thread with the provided parameters"""
        threading.Thread.__init__(self)
        self.PHANTOMJS_PATH = pjs_path
        self.NETDOMAINS_PATH = ndjs_path
        self.GENERATOR = gen
        self.OUTWRITER = ow
        self.ERRWRITER = stderr
        self.STAT = stat
        self.RUN = True
        
        
    def run(self):
        """run

        Main loop of the thread. Checks URLs using PhantomJS and saves the output.
        """
        try:
            for self.url in self.GENERATOR: # Iterate through all URLs in the Generator
                if self.RUN: # If we are still active...
                    try:
                        self.output = self.runExternal(self.url) # We run the external program and capture the output
                        self.OUTWRITER.writeOut(self.url, self.output[0].strip()) # Then write it to file
                        if len(self.output[1]) != 0: # Something must have gone wrong. Notify
                            self.ERRWRITER.write("ERROR: " + self.url + ": " + self.output[1].strip())
                        self.STAT.done() # Notify progress bar
                    except Exception as inst:
                        self.ERRWRITER.write(type(inst))
                        self.ERRWRITER.write(str(inst))
                else:
                    return
        except:
            return
    
    def runExternal(self,url):
        """runExternal

        Run PhantomJS on the provided URL.

        @param url: The URL phantomjs should check.
        """
        self.process = Popen([self.PHANTOMJS_PATH, self.NETDOMAINS_PATH, "http://" + url], stdout=PIPE, stderr=PIPE)
        return self.process.communicate()
    
    def shutdown(self):
        """shutdown

        Cleanly shut down the thread.
        """
        self.RUN = False