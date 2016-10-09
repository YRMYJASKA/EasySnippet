#!/usr/bin/env python

import snippets
import sys
import os

#Refrence to the programs arguments:
#argv[1] = Language
#argv[2] = Snippet
#argv[3] = File name

#print("Creating File!")
if len(sys.argv) < 3:
    print("Too few arguments. See ezsnip -help for help")
elif sys.argv[1] == "cpp":
    #print("CPP!")
    FILE = "%s.cpp" % sys.argv[3]
    snippets.WriteSnippet("cpp", FILE, sys.argv[2])
#In development. Feel free to enable this and remove the comments
#elif (sys.argv[1] == "header") | (sys.argv[1] == "h"):
#    #print("Header")
#    FILE = "%s.h" % sys.argv[3] 
elif (sys.argv[1] == "ruby") |  (sys.argv[1] == "rb"):
    #print("ruby")
    FILE = "%s.rb" % sys.argv[3] 
elif sys.argv[1] == "c":
    #print("C")
    FILE = "%s.c" % sys.argv[3] 
elif (sys.argv[1] == "python") |  (sys.argv[1] == "py"):
    #print("Python"
    FILE = "%s.py" % sys.argv[3] 
elif sys.argv[1] == "-help":
    print("help")
else:
    print("ERROR: Invalid first input. Check ezsnip -help for help")
    exit()
