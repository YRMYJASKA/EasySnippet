#!/usr/bin/env python

import snippets
import sys
import os

#Refrence to the programs arguments:
#argv[1] = Language
#argv[2] = Snippets name
#argv[3] = Files name

#print("Creating File!")
if len(sys.argv) < 3:
    print("Too few arguments. See ezsnip -help for help")
elif sys.argv[1] == "cpp":
    #print("CPP!")
    FILE = open("%s.cpp" % sys.argv[3], 'a')
    snippets.WriteSnippet("cpp", FILE, sys.argv[2])
    FILE.close()
elif (sys.argv[1] == "header") | (sys.argv[1] == "h"):
    #print("Header")
    FILE = open("%s.h" % sys.argv[3], 'a')
elif (sys.argv[1] == "ruby") |  (sys.argv[1] == "rb"):
    #print("ruby")
    FILE = open("%s.rb" % sys.argv[3], 'a')
    FILE.close()
elif sys.argv[1] == "c":
    #print("C")
    FILE = open("%s.c" % sys.argv[3], 'a')
    FILE.close()
elif (sys.argv[1] == "python") |  (sys.argv[1] == "py"):
    #print("Python"
    FILE = open("%s.py" % sys.argv[3], 'a')
    FILE.close()
elif sys.argv[1] == "-help":
    print("help")
else:
    print("ERROR: Invalid first input. Check ezsnip -help for help")
    exit()
