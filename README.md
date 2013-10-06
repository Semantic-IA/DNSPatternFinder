DNSPatternFinder.py
===================

A basic implementation that finds the DNS Patterns created when viewing a
Website. Meant to be used to generate the Database for the
[Simulator for semantic intersection attacks](https://github.com/malexmave/DRQPatternAttack)
on the DNS Range Query algorithm proposed by Zhao et al.

# Dependencies

* [PhantomJS](https://github.com/ariya/phantomjs)

# Usage

    usage: DNSPatternFinder.py [-h] [-V] [-c N] [-f sc] [-b bin] input output

    DNSPatternFinder -- Automatically capture DNS Query Patterns

      Created by Max Maass on 2013-03-13.
      Copyright 2013 Max Maass.
      
      Licensed under the BSD License.
      
      Distributed on an "AS IS" basis without warranties
      or conditions of any kind, either express or implied.

    USAGE

    positional arguments:
      input                 File containing the target Domains, one per line,
                            without the leading 'http://www.'
      output                Output file

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      -c N, --threads N     Sets the number of Processes to be used to N [default
                            10]
      -f sc, --script sc    Set the used phantomJS-script to sc [default
                            script/netdomains.js]
      -b bin, --binary bin  Set the used phantomJS-binary to bin [default
                            phantomjs]

# Bugs

At the time of the last run, there were some bugs in PhantomJS leading to errors not being
caught by the provided error handlers and instead being written to the output file. Manual checking
of the results is recommended.

Also, the program had the tendency to deadlock after a while. It is unknown why this happened,
but you should occasionally check if the program is still doing work.

# License

The program is licensed under the BSD 2-clause license.