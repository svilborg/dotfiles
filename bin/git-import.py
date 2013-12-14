#!/usr/bin/env python
# encoding=utf8
# Clones agit poject from URL in a folder with the name of the git repo
#
# Usage : ./git-import.py https://github.com/someuser/someproject.git
#

from urlparse import urlparse
import sys
import os
import subprocess

if __name__ == '__main__':

	if len(sys.argv) == 2 :

		giturl = sys.argv[1];

		path_split = giturl.rsplit('/')[1:]

		if len(path_split) > 0 :
			repo_name = path_split[-1]
			repo_name = repo_name.replace(".git", "")

			# create dir
			if not os.path.exists(repo_name) :
				os.makedirs(repo_name)

			print "Cloning Repo " + giturl 
			print "into ./" + repo_name

			output = subprocess.check_output(["git","clone", giturl, "./"+repo_name])
			
		else :
			print "Invalid URL"

	else :
		print "Missing Paramter"