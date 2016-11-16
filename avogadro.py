import sys
import os
import argparse
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

def main():
    parser = argparse.ArgumentParser(description='Tool for formatting python output in an easy-to-read format')
    parser.add_argument("eventlist",help="Path to alphabetically-arranged, newline-delimited list of ISO events")
    parser.add_argument("scoresheet",help="Path to scoresheet tsv")
    parser.add_argument("--outfile",help="Path to output file")
    args = parser.parse_args()
    event_file = args.eventlist
    scoresheet_file = args.scoresheet
    outfile = args.outfile
    events = []
    with open(event_file,'r') as fh:
        for line in fh:
            events.append(line.strip())
    school_list = []
    with open(scoresheet_file,'r') as fh:
        for line in fh:
            school_list.append(line.strip().split('\t'))
    if(outfile):
        with open(outfile,'w') as fh:
            for school in school_list:
                fh.write("{} - {} place\n".format(school[0],ordinal(int(school[-1]))))
                for i, x in enumerate(events):
                    fh.write(x + " - " + ordinal(int(school[i+1])) + "\n")
                fh.write('\n')
    else:
        for school in school_list:
            print("{} - {} place".format(school[0],ordinal(int(school[-1]))))
            for i, x in enumerate(events):
                print(x + " - " +ordinal(int(school[i+1])))
            print('\n')

if __name__=='__main__':
    main()
