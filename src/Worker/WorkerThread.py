'''
WorkerThread to run the external Program and capture the output.

@author: Max Maass
'''
import threading
from subprocess import Popen, PIPE

class Thread(threading.Thread):
    def __init__(self,pjs_path, ndjs_path, gen, ow, stat):
        threading.Thread.__init__(self)
        self.PHANTOMJS_PATH = pjs_path
        self.NETDOMAINS_PATH = ndjs_path
        self.GENERATOR = gen
        self.OUTWRITER = ow
        self.STAT = stat
        
    def run(self):
        try:
            for self.url in self.GENERATOR:
                try:
                    self.OUTWRITER.writeOut(self.url, self.runExternal(self.url))
                    self.STAT.done()
                except Exception as inst:
                    print type(inst)
                    print inst
        except:
            return
    
    def runExternal(self,url):
        self.process = Popen([self.PHANTOMJS_PATH, self.NETDOMAINS_PATH, "http://" + url], stdout=PIPE)
        return self.process.communicate()[0].strip()
        
        