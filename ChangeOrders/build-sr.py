#!/usr/bin/python
"""
Build Cerner SR
"""
import sys
import os

def main():
    f = open('orders.txt','rU')
    sr_lines = []
    for line in f:
        if(line.find('ORDER SUMMARY:') != -1):
            line = next(f)
            lines = line.split(',')
            full_line = lines[0] + lines[1][0:3]
            sr_lines.append(full_line)

    f.close()

    if(os.path.exists('sr.txt')):
            os.remove('sr.txt')

    f = open('sr.txt','w')
    f.write('Please add the following providers.  Reference SR 420444155:\n')
    for line in sr_lines:
        f.write(line)
        f.write('\n')

if __name__ == "__main__":
    sys.exit(main())
