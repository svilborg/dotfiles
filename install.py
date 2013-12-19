#!/usr/bin/env python
# encoding=utf8

import os
import sys
import getopt
import subprocess
from shutil import rmtree, copy

homeDir = os.getenv("HOME") + "/"
bkpDir = homeDir + ".bashrc_bkp/"
bashDir = homeDir + ".bashrc_include/"
tmpDir = homeDir + ".bashrc_tmp/"

repoUrl = "https://github.com/svilborg/dotfiles"

files = [".bashrc", ".bash_logout", ".gitconfig"]


def cleanup_bash():

    if os.path.exists(bashDir):
        rmtree(bashDir)

    pass


def cleanup_tmp():

    if os.path.exists(tmpDir):
        rmtree(tmpDir)

    pass

def cleanup_bkp():

    if os.path.exists(bkpDir):
        rmtree(bkpDir)

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
        fullFile = os.path.join(tmpDir + "bashrc/", file)

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
    src_files = os.listdir(tmpDir + "bin/")

    print "Copying bin files"
    print tmpDir + "/bin/"

    for file in src_files:
        fullFile = os.path.join(tmpDir + "/bin/", file)
        print "Add file - ~./bin/" + file

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

    cleanup_bash()

    cleanup_tmp()

    backup()

    checkout()

    install_aliases()

    install_files()

    install_bin()

    reload_bashrc()

    cleanup_tmp()

    print "Installed"

    pass


def revert():

    revertHomeFiles()

    cleanup_bash()

    cleanup_tmp()

    print "Reverted"

    pass


def main(argv):
    info = """
    Usage : 
    Install - install.py -i 
    Uninstall - install.py -u
    Clean backup - install.py -c
    Reload .bashrc - install.py -u
    """

    try:
        opts, args = getopt.getopt(argv, "hiurc")
    except getopt.GetoptError:
        print info
        sys.exit(2)

    if len(opts) > 0:
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
            elif opt in ("-c"):
                print "Clean backup"
                cleanup_bkp()
            else:
                print info
    else:
            print info

    pass

if __name__ == "__main__":
    main(sys.argv[1:])
