'''
Main executable. Controls Workers and IO

@author: Max Maass
'''
import IO.OutputWriter
import IO.CSVParser
import Worker.WorkerThread
import Worker.StatWorker

csv_path = "/home/Max/Downloads/top-1m-ns-nc.csv"
outfile = "/home/Max/outfile.txt"
pjs_path = "/home/Max/Downloads/phantomjs-1.8.2-linux-x86_64/bin/phantomjs"
ndjs_path = "/home/Max/Downloads/phantomjs-1.8.2-linux-x86_64/netdomains.js"
THREADCOUNT = 10

with open(csv_path, 'r') as fobj:
    LC = sum(1 for line in fobj)
parserc = IO.CSVParser.Parser(csv_path)
parser = parserc.getJob()
writer = IO.OutputWriter.writer(outfile)
stat = Worker.StatWorker.Progress(LC)
threads = []
for i in range(THREADCOUNT):
    t = Worker.WorkerThread.Thread(pjs_path, ndjs_path, parser, writer, stat)
    threads.append(t)
[x.start() for x in threads]
[x.join() for x in threads]
print "|"
print "All Threads done, shutting down"
writer.shutdown()
