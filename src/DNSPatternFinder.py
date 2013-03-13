'''
Main executable. Controls Workers and IO

@author: Max Maass
'''
import IO.OutputWriter
import IO.CSVParser
import Worker.WorkerThread

parser = IO.CSVParser.Parser("/home/max/Downloads/top-1m-ns-nc-2.csv").getJob()
writer = IO.OutputWriter.writer("/home/max/outfile.txt")
threads = []
for i in range(4):
    t = Worker.WorkerThread.Thread("/home/max/Downloads/phantomjs-1.8.2-linux-x86_64/bin/phantomjs", "/home/max/Downloads/phantomjs-1.8.2-linux-x86_64/netdomains.js",parser,writer)
    threads.append(t)
[x.start() for x in threads]
[x.join() for x in threads]
print "All Threads done, shutting down"
writer.shutdown()