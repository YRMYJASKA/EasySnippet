#!/usr/bin/env python

import os
def getSnips(directory):
    snipList = []
    for file in os.listdir(directory):
        if file.endswith(".ezsnip"):
            #print(file)
            snipList.append(str(file))
    return snipList
   
def WriteSnippet(lang, outfile, snip, absdir):
    FILE = open(outfile, 'w')
    if lang == "cpp":
        SnippetsList = getSnips(absdir + "/Snippets/Cpp")
        #print (SnippetsList)
        x = 0
        while x < len(SnippetsList):
            if SnippetsList[x] == "%s.ezsnip" % snip:
                infile = open(absdir + "/Snippets/Cpp/%s" % SnippetsList[x], 'r')
                for line in infile.readlines():
                     FILE.write(line)
            x = x+1
                
#    elif lang == "header":
#        SnippetsList = getSnips("Snippets/Header")
#        #print (SnippetsList)
#        x = 0
#        while x < len(SnippetsList):
#            if SnippetsList[x] == "%s.ezsnip" % snip:
#                infile = open("Snippets/Header/%s" % SnippetsList[x], 'r')
#                for line in infile.readlines():
#                     FILE.write(line)
#            x = x+1
    elif lang == "ruby":
        SnippetsList = getSnips(absdir + "/Snippets/Ruby")
        #print (SnippetsList)
        x = 0
        while x < len(SnippetsList):
            if SnippetsList[x] == "%s.ezsnip" % snip:
                infile = open(absdir + "/Snippets/Ruby/%s" % SnippetsList[x], 'r')
                for line in infile.readlines():
                     FILE.write(line)
            x = x+1
    elif lang == "c":
        SnippetsList = getSnips(absdir + "/Snippets/C")
        #print (SnippetsList)
        x = 0
        while x < len(SnippetsList):
            if SnippetsList[x] == "%s.ezsnip" % snip:
                infile = open(absdir + "/Snippets/C/%s" % SnippetsList[x], 'r')
                for line in infile.readlines():
                     FILE.write(line)
            x = x+1
    elif lang == "python":
        SnippetsList = getSnips(absdir + "/Snippets/Python")
        #print (SnippetsList)
        x = 0
        while x < len(SnippetsList):
            if SnippetsList[x] == "%s.ezsnip" % snip:
                infile = open(absdir + "/Snippets/Python/%s" % SnippetsList[x], 'r')
                for line in infile.readlines():
                     FILE.write(line)
            x = x+1
    elif lang == "java":
        SnippetsList = getSnips(absdir + "/Snippets/Java")
        #print (SnippetsList)
        x = 0
        while x < len(SnippetsList):
            if SnippetsList[x] == "%s.ezsnip" % snip:
                infile = open(absdir + "/Snippets/Java/%s" % SnippetsList[x], 'r')
                for line in infile.readlines():
                     FILE.write(line)
            x = x+1

    else:
        print("Snippets not found")
    FILE.close()
    return


