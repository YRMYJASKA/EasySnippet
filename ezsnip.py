#!/usr/bin/env python

import snippets
import sys
import os
from platform import system

#print("Creating File!")
if len(sys.argv[1]) < 2:
    print("Too few arguments. See ezsnip -help for help")
if sys.argv[1] == "cpp":
    #print("CPP!")
    FILE = open("%s.cpp" % sys.argv[2], 'a')
    FILE.close()
elif (sys.argv[1] == "header") | (sys.argv[1] == "h"):
    #print("Header")
    FILE = open("%s.h" % sys.argv[2], 'a')
elif (sys.argv[1] == "ruby") |  (sys.argv[1] == "rb"):
    #print("ruby")
    FILE = open("%s.rb" % sys.argv[2], 'a')
    FILE.close()
elif sys.argv[1] == "c":
    #print("C")
    FILE = open("%s.c" % sys.argv[2], 'a')
    FILE.close()
elif (sys.argv[1] == "python") |  (sys.argv[1] == "py"):
    #print("Python"
    FILE = open("%s.py" % sys.argv[2], 'a')
    FILE.close()
elif sys.argv[1] == "-help":
    print("help")
else:
    print("ERROR: Invalid first input. Check ezsnip -help for help")
    exit()
