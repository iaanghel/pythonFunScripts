#!/usr/bin/python
# -*- coding: utf-8 -*-

import fnmatch
import os


def fileSearch():
    root = '/home'
    images = [
        '*.jpg',
        '*.jpeg',
        '*.png',
        '*.tif',
        '*.tiff',
        '*.py',
        ]
    matches = []

    a = raw_input('Want to search for file or directory?(f/d)')
    fileFlag = True
    if a == 'f' or a == 'F':
        search = raw_input('Chose the number for your extension\n'
                           + ', '.join(images) + '\n' + ', '.join([
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            ]) + '\n')
        if search not in [
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            ]:
            print 'You did not chose an extension, the search will be done without one. '
            search = '*'
        else:
            search = images[int(search) - 1]
        n = \
            raw_input('Type a word or leave it blank and  press ENTER:  \n'
                      )
        if n is not '':
            search = search.replace('*', n)
    elif a == 'd' or a == 'D':
        search = raw_input('Type a Directory:')
        fileFlag = False
    else:
        return 'You did not pick a valid choice: '

    for (root, dirs, filenames) in os.walk(root):

        if fileFlag:
            for filename in fnmatch.filter(filenames, search.lower()
                    + '*'):
                matches.append(os.path.join(root, filename))
        else:
            for dir in fnmatch.filter(dirs.lower(), '*'
                    + search.lower()):
                matches.append(os.path.join(root, dir))

    return ', \n'.join(matches)


print fileSearch()

