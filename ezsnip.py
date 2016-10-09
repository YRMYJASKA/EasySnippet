#!/usr/bin/env python

import os
FILEPATH = os.path.dirname(os.path.abspath(__file__))
import snippets
import sys
#Refrence to the programs arguments:
#argv[1] = Language
#argv[2] = Snippet
#argv[3] = File name

print("Creating File!")
if len(sys.argv) < 2:
    print("Too few arguments. See ezsnip -help for help")
elif sys.argv[1] == "cpp":
    #print("CPP!")
    FILE = "%s.cpp" % sys.argv[3]
    snippets.WriteSnippet("cpp", FILE, sys.argv[2], FILEPATH)
#In development. Feel free to enable this and remove the comments
#elif (sys.argv[1] == "header") | (sys.argv[1] == "h"):
#    #print("Header")
#    FILE = "%s.h" % sys.argv[3]
#    snippets.WriteSnippet("header", FILE, sys.argv[2])
elif (sys.argv[1] == "ruby") |  (sys.argv[1] == "rb"):
    #print("Ruby")
    FILE = "%s.rb" % sys.argv[3] 
    snippets.WriteSnippet("ruby", FILE, sys.argv[2], FILEPATH)
elif sys.argv[1] == "c":
    #print("C")
    FILE = "%s.c" % sys.argv[3] 
    snippets.WriteSnippet("c", FILE, sys.argv[2], FILEPATH)
elif (sys.argv[1] == "python") |  (sys.argv[1] == "py"):
    #print("Python")
    FILE = "%s.py" % sys.argv[3]
    snippets.WriteSnippet("python", FILE, sys.argv[2], FILEPATH)
elif sys.argv[1] == "java":
    #print("Java")
    FILE = "%s.java" % sys.argv[3]
    snippets.WriteSnippet("java", FILE, sys.arg[2], FILEPATH)
elif sys.argv[1] == "-help":
    print("help")
else:
    print("ERROR: Invalid first input. Check ezsnip -help for help")
    exit()
print("DONE!")
