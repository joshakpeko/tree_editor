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
regex = re.compile(r'\[.*\]\s?')

def rename(filename, repl, pattern=regex):
    """ Subitute with repl, a substring of filename matching pattern.
        Rename the file with the new made string.
        Return True if the rename was successful. False otherwise."""

    if pattern.match(filename):
        newname = pattern.sub(repl, filename)
        oldpath = path.join(root, filename)
        newpath = path.join(root, newname)
        os.rename(oldpath, newpath)
        return newname
    return None


if __name__ == '__main__':
    for root, dirs, files in os.walk(wd):
        for d in dirs:
            newname = rename(d, '')
            if newname:
                dirs[dirs.index(d)] = newname
        for f in files:
            newname = rename(f, '')
            if newname:
                files[files.index(f)] = newname
