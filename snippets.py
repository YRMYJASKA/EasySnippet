import os
def getSnips(directory, outfile):
    for file in os.listdir(directory):
        if file.endswith(".ezsnip"):
            print(file)       
   
def WriteSnippet(lang, outfile, snip):
    if lang == "cpp":
        getSnips("Snippets/Cpp", outfile)
    elif lang == "header":
        getSnips("Snippets/Header", outfile)
    elif lang == "ruby":
        getSnips("Snippets/Ruby", outfile)
    elif lang == "c":
        getSnips("Snippets/C", )
    elif lang == "python":
        getSnips("Snippets/Python", outfile)
    else:
        print("Snippets not found")
    return
