###Avogadro formatter

Avogadro is a formatting tool currently used by Illinois Science Olympiad to release score results - however, their formatting is an eyesore at best. Using the list stored in events.txt, along with the tsv of scores that you can find on the page, it'll generate a scoresheet in the form of:

School Name
Event Name - Place
...
Event Name - Place

Nothing crazy. Note that for a set of standard and trial events, events.txt should be arranged where standard events are arranged alphabetically and trial events are arranged alphabetically, afterwards. For example, given standard events Astronomy and Robot Arm, and trial events Geolocation and Rocks and Minerals, events.txt should look like:

>Astronomy

>Robot Arm

>Geolocation

>Rocks and Minerals

You should only need to make one events text file per year.

Usage:

usage: ``` avogadro.py [-h] [--outfile OUTFILE] eventlist scoresheet```

positional arguments:

  eventlist - Path to alphabetically-arranged, newline-delimited list
                     of ISO events

  scoresheet - Path to scoresheet tsv

optional arguments:

-h, --help         show this help message and exit

--outfile OUTFILE  Path to output file
