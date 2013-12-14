#!/usr/bin/env python
# encoding=utf8

import os
import subprocess
from shutil import copyfile, rmtree, copy

homeDir = os.getenv("HOME") + "/"
bkpDir  = homeDir + "bashrc_bkp/"
bashDir = homeDir + "bashrc/"
tmpDir  = homeDir + "bashrc_tmp/"

repoUrl = "https://github.com/svilborg/dotfiles"

files   = [".bashrc", ".bash_logout", ".gitconfig"]

def cleanup () :

	if os.path.exists(bashDir) :
		rmtree(bashDir)
	
	if os.path.exists(tmpDir) :
		rmtree(tmpDir)

	pass

def backup () :

	if not os.path.exists(bkpDir) :
		print "Create backup dir - " + bkpDir
		os.makedirs(bkpDir)

	for file in files:
		if os.path.exists(homeDir + file) :
			print "Backup file - ~." + file
			copyfile(homeDir + file, bkpDir + file)
		
	pass

def checkout () :
	try:
		output = subprocess.check_output(["git","clone", "--recursive", repoUrl, tmpDir])
		pass
	except subprocess.CalledProcessError, e:
	 	print "CalledProcessError"
	except Exception, e:
		print "Error - " + e.message
	else:
		pass
	finally:
		pass

	pass

def install_aliases () :

	# Create Destination Dir
	if not os.path.exists(bashDir) :
		print "Create bashrc dir - " + bashDir
		os.makedirs(bashDir)

	# Copy from Destination to Bashrc Dir
	src_files = os.listdir(tmpDir + "/bashrc/")
	
	print "Coping aliases"
	
	for file in src_files :
		fullFile = os.path.join(tmpDir + "/bashrc/", file)

		if (os.path.isfile(fullFile)):
			copy(fullFile, bashDir + file)

	pass

def install_bashrc () :
	print "Replace .bashrc"

	print copyfile(tmpDir + ".bashrc", homeDir + ".bashrc")

	pass

def install () :

	cleanup()

	backup()

	checkout()

	install_aliases()

	install_bashrc()

	pass

if __name__ == '__main__':

	install()

	print "Installed"