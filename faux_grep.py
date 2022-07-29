import sys
import fileinput
import argparse

description = """
faux grep -- searches one or more files (or STDIN) for lines matching a pattern. 
"""

parser = argparse.ArgumentParser(description=description)

parser.add_argument('-i', dest="ignore_case", action="store_true", help="Ignore case")
parser.add_argument('-f', dest="show_file_names", action="store_true", help="Show file names")
parser.add_argument('pattern', help="Pattern to find")
parser.add_argument('files', nargs="*", help="Files to search")

args = parser.parse_args()
print(f"args: {args}")

pattern = args.pattern
if args.ignore_case:
    pattern = pattern.lower()

for raw_line in fileinput.input(args.files):
    line = raw_line.rstrip()
    original_line = line
    if args.ignore_case:
        line = line.lower()
    if args.pattern in line:
        if args.show_file_names:
            print(fileinput.filename(), end=' ')
        print(original_line)

