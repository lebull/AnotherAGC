#Read file

import re



if __name__ == "__main__":
    filePath = "Apollo-11/Comanche055/GIMBAL_LOCK_AVOIDANCE.agc"

    with open(filePath) as testFile:
        lines = testFile.read().split("\n")

    lineNumber = 0

    for line in lines:
        line = re.sub(r'(\s|(\\t))+', "\t", line)
        line = re.sub(r'#(.)*', "", line)
        line = re.sub(r'\A(\s)*\Z', "", line)


        if line != "":
            #print line
            words = line.split("\t")
            print "{}: {}".format(lineNumber, words)
            lineNumber+=1

            
    #Split stuff
