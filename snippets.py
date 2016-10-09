import os
def getSnips(directory):
    snipList = []
    for file in os.listdir(directory):
        if file.endswith(".ezsnip"):
            print(file)
            snipList.append(str(file))
    return snipList
   
def WriteSnippet(lang, outfile, snip):
    FILE = open(outfile, 'w')
    if lang == "cpp":
        snippetList = getSnips("Snippets/Cpp")
        for x in range(0, len(snippetList)):
            if snippetList[x] == "%s.ezsnip" % snip:
                infile = open(snippetList[x], 'r')
                for line in infile:
                    FILE.write(line)
                infile.close()
                break
                
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

WriteSnippet("cpp", "moi.cpp", "class")
