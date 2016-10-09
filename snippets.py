import os
def getSnips(directory):
    snipList = []
    for file in os.listdir(directory):
        if file.endswith(".ezsnip"):
            #print(file)
            snipList.append(str(file))
    return snipList
   
def WriteSnippet(lang, outfile, snip):
    FILE = open(outfile, 'w')
    if lang == "cpp":
        SnippetsList = getSnips("Snippets/Cpp")
        #print (SnippetsList)
        x = 0
        while x < len(SnippetsList):
            if SnippetsList[x] == "%s.ezsnip" % snip:
                infile = open("Snippets/Cpp/%s" % SnippetsList[x], 'r')
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
        SnippetsList = getSnips("Snippets/Ruby")
        #print (SnippetsList)
        x = 0
        while x < len(SnippetsList):
            if SnippetsList[x] == "%s.ezsnip" % snip:
                infile = open("Snippets/Ruby/%s" % SnippetsList[x], 'r')
                for line in infile.readlines():
                     FILE.write(line)
            x = x+1
    elif lang == "c":
        SnippetsList = getSnips("Snippets/C")
        #print (SnippetsList)
        x = 0
        while x < len(SnippetsList):
            if SnippetsList[x] == "%s.ezsnip" % snip:
                infile = open("Snippets/C/%s" % SnippetsList[x], 'r')
                for line in infile.readlines():
                     FILE.write(line)
            x = x+1
    elif lang == "python":
        SnippetsList = getSnips("Snippets/Python")
        #print (SnippetsList)
        x = 0
        while x < len(SnippetsList):
            if SnippetsList[x] == "%s.ezsnip" % snip:
                infile = open("Snippets/Python/%s" % SnippetsList[x], 'r')
                for line in infile.readlines():
                     FILE.write(line)
            x = x+1
    elif lang == "java":
        SnippetsList = getSnips("Snippets/Java")
        #print (SnippetsList)
        x = 0
        while x < len(SnippetsList):
            if SnippetsList[x] == "%s.ezsnip" % snip:
                infile = open("Snippets/Java/%s" % SnippetsList[x], 'r')
                for line in infile.readlines():
                     FILE.write(line)
            x = x+1

    else:
        print("Snippets not found")
    FILE.close()
    return

