#!/usr/bin/env python

import sys
import os
from platform import system

print("Creating File!")

print("Windows")
if sys.argv[1] == "cpp":
    #print("CPP!")
    FILE = open("%s.cpp" % sys.argv[2], 'a')
    FILE.close()
elif (sys.argv[1] == "header") | (sys.argv[1] == "h"):
    #print("Header")
    FILE = open("%s.h" % sys.argv[2], 'a')
elif sys.argv[1] == "ruby":
    #print("ruby")
    FILE = open("%s.rb" % sys.argv[2], 'a')
    FILE.close()
elif sys.argv[1] == "c":
    #print("C")
    FILE = open("%s.c" % sys.argv[2], 'a')
    FILE.close()
elif sys.argv[1] == "python":
    #print("Python"
    FILE = open("%s.py" % sys.argv[2], 'a')
    FILE.close()


