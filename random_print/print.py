
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
    BROWN = '\033[1;4;42;38;5;52m'
    DEEPBLUE = '\033[1;38;5;18m'

def draw_desert(size):
    number = 1000
    for i in range(size):
        rng = int(math.ceil(random() * number))
        desert_style = []
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

def draw_grass(size):
    number = 1000
    for i in range(size):
        rng = int(math.ceil(random() * number))
        if rng > 900:
            sys.stdout.write(bcolors.BOLDGREEN + "T" + bcolors.ENDC),
            continue
        if rng >= 800 and rng < 900:
            sys.stdout.write(bcolors.OKCYAN + "=" + bcolors.ENDC),
            continue   
        if rng >= 600 and rng < 800:
            sys.stdout.write(bcolors.OKBLUE + "vVv" + bcolors.ENDC),
            continue   
        if rng == 55 :
            sys.stdout.write(bcolors.UNDERLINE + ".//\." + bcolors.ENDC),
            continue
        if rng == 56 :
            sys.stdout.write(bcolors.UNDERLINE + "_|{|^\." + bcolors.ENDC),
            continue
        sys.stdout.write(bcolors.OKGREEN + ",," + bcolors.ENDC)

def draw_sea(size):
    number = 1000
    for i in range(size):
        rng = int(math.ceil(random() * number))
        if rng > 900:
            sys.stdout.write(bcolors.OKBLUE + "v" + bcolors.ENDC),
            continue
        if rng >= 800 and rng < 900:
            sys.stdout.write(bcolors.OKCYAN + "vVv" + bcolors.ENDC),
            continue   
        if rng >= 600 and rng < 800:
            sys.stdout.write(bcolors.DEEPBLUE + "wWWWw" + bcolors.ENDC),
            continue   
        if rng == 55 :
            sys.stdout.write(bcolors.BROWN + "\_P_/" + bcolors.ENDC),
            continue
        sys.stdout.write(bcolors.OKCYAN + "==" + bcolors.ENDC)        

for i in range(8):
    rng1 = int(math.ceil(random() * 100))
    rng2 = int(math.ceil(random() * 1000 + 1000))
    if rng1 >= 40 and rng1 < 78:
        draw_desert(rng2)
    if rng1 <= 39:
        draw_grass(rng2)
    if rng1 >= 78:
        draw_sea(rng2+500)
