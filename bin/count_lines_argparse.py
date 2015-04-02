#!/usr/bin/env python


import argparse
import sys

def word_count(input_file):
    count = 0
    for line in input_file:
        count += 1
    return count

parser = argparse.ArgumentParser(description='Count lines in file')
parser.add_argument('input_file', type=argparse.FileType(),
                    help='Input filename')
parser.add_argument('output_file', type=argparse.FileType('w'),
                    nargs='?', default=sys.stdout,
                    help='Output filename')
args = parser.parse_args()

with args.input_file:
    print >>args.output_file, args.input_file.name, word_count(args.input_file)
