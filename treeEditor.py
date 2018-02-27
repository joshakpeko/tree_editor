#!/usr/bin/env python3

""" miniscript to recursively rename subdirs and filenames in a given
    root directory.
    The specified regex or a self-defined one help replace(or remove)
    annoying substrings of the filenames.
    Ex: "[ Torrenteleven.dummy ] FiftyShadesOfBlack.FRENCH.avi"
    can be renamed to "FiftyShadesOfBlack.FRENCH.avi".
"""

import os, re
import os.path as path

wd = os.getcwd()
regex = re.compile(r'^\[.*\]\s?')

def main():
    """ Navigate top-down the directories tree and rename directories
        and files which name matches regex."""

    for root, dirs, files in os.walk(wd):
        for d in dirs:
            d = path.join(root, d)
            newname = rename(d, '')
            if newname:
                dirs[dirs.index(path.basename(d))] = newname
        for f in files:
            f = path.join(root, f)
            newname = rename(f, '')
            if newname:
                files[files.index(path.basename(f))] = newname

def rename(filename, repl, pattern=regex):
    """ Subitute with repl, a substring of filename matching pattern.
        Rename the file with the new made string.
        Return True if the rename was successful. False otherwise."""

    basename = path.basename(filename)

    if pattern.match(basename):
        newname = pattern.sub(repl, basename)
        newpath = path.join(path.dirname(filename), newname)
        if newpath:
            try:
                os.rename(filename, newpath)
            except OSError as exc:
                print(exc)
                return None
        return newname
    return None


if __name__ == '__main__':
    main()
