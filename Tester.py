import re
import os
import subprocess
from os import listdir
from os.path import isfile, join

def main():
    mypath = "./Test_results"
    mypath2 = "./Test_files"
    onlytestfiles = [f for f in listdir(mypath2) if isfile(join(mypath2, f))]
    onlyresultsfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    myresults = []
    results = []
    #### Compile ####
    os.system("javac -cp .;algs4.jar -Xlint:deprecation PrimVsKruskal.java")
    #### Your Results ####
    for file in onlytestfiles:
        filepath = "./Test_files/"+file
        cmd = "java -cp .;algs4.jar PrimVsKruskal "+filepath
        line = os.popen(cmd).read()
        strippedline = re.findall('Does Prim MST = Kruskal MST\?\s*(\w+)', line)
        myresults.append(strippedline[0])

    #### Results List ####
    for file in onlyresultsfiles:
        filepath = "./Test_results/"+file
        with open(filepath, 'r') as f:
            lines = f.read().splitlines()
            for line in lines:
                #if not line.strip():
                result = re.findall('Does Prim MST = Kruskal MST\?\s*(\w+)', line)
                if len(result) > 0:
                    break;
            results.append(result[0])
    print(list(set(results)-set(myresults)))

if __name__ == '__main__':
    main()
