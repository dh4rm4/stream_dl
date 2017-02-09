#!/usr/bin/env python
# -*- coding utf-8 -*-

from __future__ import unicode_literals
import os
import subprocess
import sys

class col:
    LOWRED = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# CHECK IF A CMD EXIST IN YOUR SYSTEM
def cmd_exists(cmd):
    return subprocess.call("type " + cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

# CHECK IF PIP IS ALREADY INSTALL
def check_pip():
    if (cmd_exists('pip') == False):
        print 'pip        .....................' + col.BOLD + col.FAIL + 'NOPE' + col.ENDC
        print 'initialise pip installation:'
        os.system("apt-get -yqq install pip")
        print 'pip        .....................' + col.BOLD + col.OKGREEN + 'OK' + col.ENDC
    else:

        print 'pip        .....................' + col.BOLD + col.OKGREEN + 'OK' + col.ENDC

# MANAGE THE DEPENDANCIES
def dependancies():
    try:
        if (sys.version_info < (3,0)):
            import Tkinter
        else:
            import tkinter
        print 'Tkinter    .....................' + col.BOLD + col.OKGREEN + 'OK' + col.ENDC
    except ImportError:
        print 'Tkinter    .....................' + col.BOLD + col.FAIL + 'NOPE' + col.ENDC
        print 'initialise Tkinter installation:'
        if (sys.version_info < (3,0)):
            os.system('apt-get -yqq install python-tk')
            os.system('apt-get -yqq install python-imaging-tk')
        else:
            os.system('apt-get -yqq install python3-tk')
            os.system('apt-get -yqq install python-imaging-tk')
            print 'Tkinter    .....................' + col.BOLD + col.OKGREEN + 'OK' + col.ENDC

    try:
        import ttk
        print 'ttk        .....................' + col.BOLD + col.OKGREEN + 'OK' + col.ENDC
    except ImportError:
        print 'ttk        .....................' + col.BOLD + col.FAIL + 'NOPE' + col.ENDC

    try:
        from PIL import ImageTk, Image
        print 'PIL        .....................' + col.BOLD + col.OKGREEN + 'OK' + col.ENDC
    except ImportError:
        print 'PIL        .....................' + col.BOLD + col.FAIL + 'NOPE' + col.ENDC

    try:
        import youtube_dl
        print 'youtube_dl .....................' + col.BOLD + col.OKGREEN + 'OK' + col.ENDC
    except ImportError:
        print 'youtube_dl .....................' + col.BOLD + col.FAIL + 'NOPE' + col.ENDC
        print 'initialise youtube_dl installation:'
        os.system('pip -q install youtube_dl')
        print 'youtube_dl .....................' + col.BOLD + col.OKGREEN + 'OK' + col.ENDC



if os.getuid() == 0:
    print '      ' + col.UNDERLINE + col.LOWRED + '=== W3lcome r00t ===' + col.ENDC
    print col.YELLOW + '\nCheck dependencies:' + col.ENDC
    check_pip()
    dependancies()
    print '\n\n' + col.FAIL + col.BOLD + '======== INITIALISATION STREAM_DL =======\n\n' + col.ENDC
    try:
        import stream_dl
    except ImportError:
        print col.BOLD + col.FAIL + 'ERROR: can\'t access to stream_dl.py\n' + col.ENDC
    print '      ' + col.LOWRED + '===   Bye r00t   ===' + col.ENDC
else:
    print col.BOLD + 'I cannot run as a mortal.\n' + col.UNDERLINE + col.FAIL + 'Try again as r00t' + col.ENDC
