#!/usr/bin/env python
# -*- coding utf-8 -*-

from __future__ import unicode_literals
import os
import subprocess
import sys

class col:
    LOWRED	= '\033[94m'
    OKGREEN	= '\033[92m'
    YELLOW	= '\033[93m'
    FAIL	= '\033[91m'
    ENDC	= '\033[0m'
    BOLD 	= '\033[1m'
    UNDERLINE	= '\033[4m'
    KILL	= '\033[95m'



def isCmd(cmd):
    return (subprocess.call("type " + cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0)

def printFail(moduleName):
    nbSpace = 11 - len(moduleName)
    print (moduleName + (" " * nbSpace) + "....................." + col.BOLD + col.FAIL + "NOPE" + col.ENDC)

def printFailInstallation(moduleName):
    print (col.BOLD + col.FAIL + "### FAIL TO INSTALL:    " + col.KILL + moduleName + col.FAIL + "    ###" + col.ENDC)

def printSuccess(moduleName):
    nbSpace = 11 - len(moduleName)
    print (moduleName + (" " * nbSpace) + "....................." + col.BOLD + col.OKGREEN + "OK" + col.ENDC)

def printHello():
    print ('      ' + col.UNDERLINE + col.LOWRED + '=== W3lcome r00t ===' + col.ENDC)
    print (col.YELLOW + '\nCheck dependencies:' + col.ENDC)


def printBye():
    print ('      ' + col.LOWRED + '===   Bye r00t   ===' + col.ENDC)


#########################################
#					#
#	START DEPENDANCIES CHECK	#
#					#
#########################################

def init():
    printHello()
    isPipInstall()
    installLibavTools()
    areModulesInstall()
    importStreamDl()
    printBye()

def areModulesInstall():
    isTkinter()
    isTtk()
    isPIL()
    isYoutubeDl()



def isPipInstall():
    if (isCmd("pip") == False):
        printFail("pip")
        print ('initialise pip installation:')
        os.system("apt-get -yqq install python-pip")
    printSuccess("pip")


def installLibavTools():
    os.system("sudo apt-get -yqq install libav-tools")
    printSuccess("libav-tools")

def isTkinter():
    try:
        if (sys.version_info < (3,0)):
            import Tkinter
        else:
            import tkinter
    except ImportError:
        printFail("tkinter")
        print ('initialise Tkinter installation:')
        if (sys.version_info < (3,0)):
            os.system('apt-get -yqq install python-tk')
        else:
            os.system('apt-get -yqq install python3-tk')
            os.system('apt-get -yqq install python-imaging-tk')
    else:
        printSuccess("tkinter")


def isTtk():
    try:
        import ttk
    except ImportError:
        printFail("ttk")
    else:
        printSuccess("ttk")


def isPIL():
    try:
        from PIL import ImageTk, Image
    except ImportError:
        printFail("PIL")
    else:
        printSuccess("PIL")


def isYoutubeDl():
    try:
        import youtube_dl
    except ImportError:
        printFail("youtube_dl")
        print ('initialise youtube_dl installation:')
        os.system('pip -q install youtube_dl')
    else:
        printSuccess("ttk")


def importStreamDl():
    try:
        import stream_dl
    except ImportError:
        print (col.BOLD + col.FAIL + 'ERROR: can\'t access to stream_dl.py\n' + col.ENDC)
    else:
        print ('\n\n' + col.FAIL + col.BOLD + "If everything is" + col.OKGREEN + " OK " + col.FAIL +
               "you can start by tiping:\n" + col.ENDC)
        print (col.KILL + col.BOLD + "   python2 stream_dl    \n\n" + col.ENDC)





def isUserRoot():
    return (os.getuid())


def askForRoot():
    print (col.BOLD + 'I cannot run as a mortal.\n' + col.UNDERLINE + col.FAIL + 'Try again as r00t' + col.ENDC)

if __name__ == '__main__':
    if (isUserRoot() == 0):
        init()
    else:
        askForRoot()
