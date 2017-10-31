#!/usr/bin/python

import subprocess

p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line,
retval = p.wait()
if retval == 0:
    print "Probehlo OK"
else:
    print "Chyba nastala"
