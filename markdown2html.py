#!/usr/bin/python3
"""
This is a script that convert a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file: the name of the Markdown file to be converted
    output_file: the name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""

import os
import sys

len = len(sys.argv)

if not len < 3:
    md = sys.argv[1]
    out = sys.argv[2]

if len < 3:
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)

if not os.path.exists(md):
    print("Missing {}".format(md))
    exit(1)
exit(0)