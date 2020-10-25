
import math
from random import random
import sys
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[1;94m'
    OKCYAN = '\033[1;96m'
    OKGREEN = '\033[1;38;5;34m'
    OKYELLOW = '\033[1;4;93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[1;4;35;40m'
    HEADER1 = '\033[1;032;40m'
    BOLDGREEN = '\033[1;38;5;22m'

number = 1000
for i in range(5000):
    rng = int(math.ceil(random() * number))
    if rng > 900:
        sys.stdout.write(bcolors.OKGREEN + "," + bcolors.ENDC),
        continue
    if rng >= 850 and rng < 900:
        sys.stdout.write(bcolors.OKCYAN + "=" + bcolors.ENDC),
        continue   
    if rng >= 750 and rng < 800:
        sys.stdout.write(bcolors.OKBLUE + "v" + bcolors.ENDC),
        continue   
    if rng == 55 :
        sys.stdout.write(bcolors.UNDERLINE + " /\ " + bcolors.ENDC),
        continue   
    if rng == 56 :
        sys.stdout.write(bcolors.UNDERLINE + "[^]" + bcolors.ENDC),
        continue           
    sys.stdout.write(bcolors.OKYELLOW + "--" + bcolors.ENDC)
#for i in range(5000):
    #rng = int(math.ceil(random() * number))
    #if rng > 900:
        #sys.stdout.write(bcolors.BOLDGREEN + "T" + bcolors.ENDC),
        #continue
    #if rng >= 800 and rng < 900:
        #sys.stdout.write(bcolors.OKCYAN + "=" + bcolors.ENDC),
        #continue   
    #if rng >= 600 and rng < 800:
        #sys.stdout.write(bcolors.OKBLUE + "vVv" + bcolors.ENDC),
        #continue   
    #if rng == 55 :
        #sys.stdout.write(bcolors.UNDERLINE + ".//\." + bcolors.ENDC),
        #continue
    #sys.stdout.write("0")         
    #sys.stdout.write(bcolors.OKGREEN + ",," + bcolors.ENDC)

