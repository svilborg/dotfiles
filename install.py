#!/usr/bin/env python
# encoding=utf8

import os
import sys
import getopt
import subprocess
from shutil import rmtree, copy

homeDir = os.getenv("HOME") + "/"
bkpDir = homeDir + "bashrc_bkp/"
bashDir = homeDir + "bashrc/"
tmpDir = homeDir + "bashrc_tmp/"

repoUrl = "https://github.com/svilborg/dotfiles"

files = [".bashrc", ".bash_logout", ".gitconfig"]


def cleanupBash():

    if os.path.exists(bashDir):
        rmtree(bashDir)

    pass


def cleanupTmp():

    if os.path.exists(tmpDir):
        rmtree(tmpDir)

    pass


def backup():

    if not os.path.exists(bkpDir):
        print "Create backup dir - " + bkpDir
        os.makedirs(bkpDir)

    for file in files:
        if os.path.exists(homeDir + file):
            print "Backup file - ~." + file
            copy(homeDir + file, bkpDir + file)

    pass


def checkout():

    print "Cloning repo"

    try:
        output = subprocess.check_output(
            ["git", "clone", "--recursive", repoUrl, tmpDir])
        pass
    except subprocess.CalledProcessError, e:
        print "CalledProcessError"
        print e
    except Exception, e:
        print e
    else:
        pass
    finally:
        pass

    pass


def install_aliases():

    # Create Destination Dir
    if not os.path.exists(bashDir):
        print "Create bashrc dir - " + bashDir
        os.makedirs(bashDir)

    # Copy from Destination to Bashrc Dir
    src_files = os.listdir(tmpDir + "/bashrc/")

    print "Copying aliases"

    for file in src_files:
        fullFile = os.path.join(tmpDir + "/bashrc/", file)

        if (os.path.isfile(fullFile)):
            copy(fullFile, bashDir + file)

    pass


def install_files():
    """ Install Bashrc """

    print "Replace .bashrc"

    for file in files:
        print "Replace file - ~." + file
        copy(tmpDir + file, homeDir + file)

    pass


def install_bin():

    print "Install bin"

    # Copy from Destination to Bashrc Dir
    src_files = os.listdir(tmpDir + "/bin/")

    print "Copying bin files"

    for file in src_files:
        fullFile = os.path.join(tmpDir + "/bin/", file)

        if (os.path.isfile(fullFile)):
            copy(fullFile, homeDir + "bin/" + file)

    pass


def reload_bashrc():
    print "Reload .bashrc"

    try:
        output = subprocess.check_output(['./bin/reload_bashrc.sh', '$HOME'])

        pass
    except Exception, e:
        print e
    else:
        pass
    finally:
        pass

    pass


def revertHomeFiles():

    src_files = os.listdir(bkpDir)

    for file in src_files:
        fullFile = os.path.join(bkpDir, file)

        if (os.path.isfile(fullFile)):
            print "Reverting " + file
            copy(fullFile, homeDir + file)

    pass


def install():

    cleanupBash()

    cleanupTmp()

    backup()

    checkout()

    install_aliases()

    install_files()

    install_bin()

    reload_bashrc()

    print "Installed"

    pass


def revert():

    revertHomeFiles()

    cleanupBash()

    cleanupTmp()

    print "Reverted"

    pass


def main(argv):
    info = """
    Usage : 
    Install - install.py -i 
    Uninstall - install.py -u
    Reload .bashrc - install.py -u
    """

    try:
        opts, args = getopt.getopt(argv, "hiur")
    except getopt.GetoptError:
        print info
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print info

            sys.exit()
        elif opt in ("-i"):
            install()
        elif opt in ("-r"):
            reload_bashrc()
        elif opt in ("-u"):
            revert()

    print 'Done'

if __name__ == "__main__":
    main(sys.argv[1:])
