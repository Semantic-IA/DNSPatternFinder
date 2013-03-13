'''
Shows a progress bar
@author: Max Maass
'''
from threading import Lock
from math import floor
from sys import stdout
class Progress():
    def __init__(self, LC):
        self.lock = Lock()
        self.lp = 0
        self.cp = 0
        self.cc = 0
        self.ONEP = float(LC / 100.0)
        self.COLS = 50
        self.STEP = 2
        print "               0%  10%  20%  30%  40%  50%  60%  70%  80%  90% 100%"
        stdout.write("              |")
        stdout.flush()
    
    def done(self):
        with self.lock:
            self.cc +=1
            self.cp = floor(float(self.cc / self.ONEP))
            while (self.cp - self.lp >= self.STEP):
                stdout.write("=")
                stdout.flush()
                self.lp += self.STEP
            self.lp = self.cp
            
        