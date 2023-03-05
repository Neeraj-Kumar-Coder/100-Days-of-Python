import argparse

parser = argparse.ArgumentParser()

parser.add_argument("url", help="URL of the file")
parser.add_argument("output", help="Output file name")

args = parser.parse_args()

print(args.url, args.output)

# HOW TO RUN: python .\Command_Line_Utility.py www.google.com/file.txt output_file.txt
