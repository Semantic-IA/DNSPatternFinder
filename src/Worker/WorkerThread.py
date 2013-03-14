'''
WorkerThread to run the external Program and capture the output.

@author: Max Maass
'''
import threading
from subprocess import Popen, PIPE

class Thread(threading.Thread):
    def __init__(self,pjs_path, ndjs_path, gen, ow, ew, stat):
        threading.Thread.__init__(self)
        self.PHANTOMJS_PATH = pjs_path
        self.NETDOMAINS_PATH = ndjs_path
        self.GENERATOR = gen
        self.OUTWRITER = ow
        self.ERRWRITER = ew
        self.STAT = stat
        self.RUN = True
        
    def run(self):
        try:
            for self.url in self.GENERATOR:
                if self.RUN:
                    try:
                        self.output = self.runExternal(self.url)
                        self.OUTWRITER.writeOut(self.url, self.output[0].strip())
                        if len(self.output[1]) != 0:
                            self.ERRWRITER.writeOut(self.url, self.output[1].strip())
                            self.STAT.done()
                    except Exception as inst:
                        print type(inst)
                        print inst
                else:
                    return
        except:
            return
    
    def runExternal(self,url):
        self.process = Popen([self.PHANTOMJS_PATH, self.NETDOMAINS_PATH, "http://" + url], stdout=PIPE, stderr=PIPE)
        return self.process.communicate()
    
    def shutdown(self):
        self.RUN = False
        
        