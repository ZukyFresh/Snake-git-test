#!/usr/bin/python

# import modulu pro parsovani options
from optparse import OptionParser

# zde se definuje jak to bude vypadat
optparser = OptionParser()
optparser.set_defaults(listmode=0)
optparser.add_option("-n", "--name", action="store", dest="name", help="nazev souboru")
optparser.add_option("-y", "--assume-yes", action="store_true", dest="yes", help="predpokladat souhlas")

# zde se provede vlastni zpracovani
(options, args) = optparser.parse_args() 

if options.yes:
  print "Rekli jste ANO"

if options.name:
  print "Zadali jste jmeno ", options.name
else:
  print "Nezadali jste jmeno"

print "Zbytek je: ", args
