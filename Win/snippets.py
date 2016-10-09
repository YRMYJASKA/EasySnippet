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
        SnippetsList = getSnips("../Snippets/Cpp")
        #print (SnippetsList)
        x = 0
        while x < len(SnippetsList):
            if SnippetsList[x] == "%s.ezsnip" % snip:
                infile = open("../Snippets/Cpp/%s" % SnippetsList[x], 'r')
                for line in infile.readlines():
                     FILE.write(line)
            x = x+1
                
    elif lang == "header":
        getSnips("Snippets/Header")
    elif lang == "ruby":
        getSnips("Snippets/Ruby")
    elif lang == "c":
        getSnips("Snippets/C", )
    elif lang == "python":
        getSnips("Snippets/Python")
    else:
        print("Snippets not found")
    FILE.close()
    return

