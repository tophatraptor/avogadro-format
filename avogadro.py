import sys
import os

#Ordinal code from user 'Winston Ewert' on stackexchange
SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def ordinal(num):
    # I'm checking for 10-20 because those are the digits that
    # don't follow the normal counting scheme.
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        # the second parameter is a default.
        suffix = SUFFIXES.get(num % 10, 'th')
    return str(num) + suffix

def generator(inputfile):
    for line in inputfile:
        yield line.strip()

f1 = open(sys.argv[1],'rt')
lines = generator(f1)
eventlist = []
for x in lines:
    eventlist.append(x)
f2 = open(sys.argv[2],'rt')
lines = generator(f2)
for x in lines:
     scorelist = x.split()
     for i in range(len(eventlist)):
         print("{}: {}".format(eventlist[i],ordinal(int(scorelist[i]))))
