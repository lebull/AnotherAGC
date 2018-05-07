#Read file

import re

if __name__ == "__main__":
    filePath = "/Users/administrator/Projects/AnotherAGC/Apollo-11/Comanche055/GIMBAL_LOCK_AVOIDANCE.agc"

    with open(filePath) as testFile:
        lines = testFile.read().split("\n")
    for line in lines:
        #line = re.sub(r'(\t)*', "\t", line)
        words = line.split("\t")
        print "----\n{}".format(words)
    #Split stuff
