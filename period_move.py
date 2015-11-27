
#!/usr/bin/python
#_*_coding:utf-8_*_

import sys
import re


def main():
    ends_period = re.compile("\.")
    fin = open(sys.argv[1])
    for line in fin:
        line = line.strip()
        if line.endswith("."):
            #print line[-1]
            #exit()

            line = ends_period.sub(" .", line)
            print line


if __name__ == '__main__':
    main()
