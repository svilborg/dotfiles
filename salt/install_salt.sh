#!/bin/bash

sudo add-apt-repository ppa:saltstack/salt
sudo apt-get update
sudo apt-get install salt-minion

# Exec : sudo salt-call --local state.highstate --file-root ./salt/