#!/usr/bin/python2.7
# encoding: utf-8
'''
DNSPatternFinder -- Automatically capture DNS Query Patterns

@author:     Max Maass
        
@copyright:  2013 Max Maass
        
@license:    To be determined

@contact:    0maass@informatik.uni-hamburg.de (PGP Key ID: 3408825E, Fingerprint 84C4 8097 A3AF 7D55 189A  77AC 169F 9624 3408 825E)
@deffield    updated: Updated
'''

import sys
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
import IO.CSVParser
import IO.OutputWriter
import Worker.StatWorker
import Worker.WorkerThread
import signal

__all__ = []
__version__ = 0.1
__date__ = '2013-03-13'
__updated__ = '2013-04-06'

DEBUG = 0
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg
def main(argv=None): # IGNORE:C0111
    '''Command line options.'''
    
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by Max Maass on %s.
  Copyright 2013 Max Maass.
  
  Licensed under the TBD License.
  
  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument('-V', '--version', action='version', version=program_version_message)
        parser.add_argument(dest="infile", help="File containing the target Domains, one per line, without the leading 'http://www.'", metavar="input")
        parser.add_argument(dest="outfile", help="Output file", metavar="output")
        parser.add_argument('-c', '--threads', dest="threadc", help="Sets the number of Processes to be used to N [default %(default)s]", metavar="N", default="10", type=int)
        parser.add_argument('-f', '--script', dest="script", help="Set the used phantomJS-script to sc [default %(default)s]", default="script/netdomains.js", metavar="sc")
        parser.add_argument('-b', '--binary', dest="pjs_bin", help="Set the used phantomJS-binary to bin [default %(default)s]", default="phantomjs", metavar="bin")
        
        # Process arguments
        args = parser.parse_args()
        
        INFILE = args.infile        # Input File
        OUTFILE = args.outfile      # Output File
        WORKERS = args.threadc      # Thread count
        SCRIPTFILE = args.script    # Script to use with PhantomJS
        BINARY = args.pjs_bin       # PhantomJS binary
        for f in [INFILE, SCRIPTFILE, BINARY]:
            try:
                with open(f): pass
            except IOError:
                if f != "phantomjs":
                    sys.stderr.write("Error: File " + f + " does not exist. EXITING.\n")
                else:
                    sys.stderr.write("Error: phantomjs not found. Please make sure it is installed and inside the system PATH. Alternatively, specify the path to the binary using the '-b'-Switch. EXITING.\n")
                return 1
        if WORKERS < 1:
            sys.stderr.write("Error: Thread count must be at least 1. EXITING.")
            return 1
        with open(INFILE, 'r') as fobj:
            LC = sum(1 for line in fobj)
        threads = []
        def clean_shutdown(signal, frame):
            [x.shutdown() for x in threads]
        parser = IO.CSVParser.Parser(INFILE).getJob()
        writer = IO.OutputWriter.writer(OUTFILE)
        stat = Worker.StatWorker.Progress(LC)
        for i in range(WORKERS):
            t = Worker.WorkerThread.Thread(BINARY, SCRIPTFILE, parser, writer, stat)
            threads.append(t)
        [x.start() for x in threads]
        signal.signal(signal.SIGINT, clean_shutdown)
        signal.signal(signal.SIGTERM, clean_shutdown)
        [x.join() for x in threads]
        print "|"
        print "All Threads done, shutting down"
        writer.shutdown()

        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception, e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    sys.exit(main())