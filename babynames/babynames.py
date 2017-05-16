#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import sys

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

_year_re = re.compile(r'<h3 align="center">Popularity in (?P<year>\d+)')
_name_rank_re = re.compile(
    r'<tr align="right"><td>(?P<rank>\d+)</td><td>(?P<male>\w+)</td><td>('
    r'?P<female>\w+)</td>')


def _find_names(f):
    for line in f:
        match = _name_rank_re.search(line)
        if match:
            rank = match.group('rank')
            female = match.group('female')
            yield f'{female} {rank}'
            male = match.group('male')
            yield f'{male} {rank}'


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year 
    string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    with open(filename, 'r', encoding='utf8') as f:
        yield from _find_year(f)
        yield from _find_names(f)


def _find_year(f):
    for line in f:
        match = _year_re.search(line)
        if match:
            yield match.group('year')
            return


def all_ranks_data(input_files):
    for f in input_files:
        yield from extract_names(f)


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    if args[0] == '--summaryfile':
        del args[0]
        output_file = args[0]
        del args[0]

        with open(output_file, 'w', encoding='utf8') as out:
            for data in all_ranks_data(args):
                out.writelines(data)

    for data in all_ranks_data(args):
        print(data)


if __name__ == '__main__':
    main()
