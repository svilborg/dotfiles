# ~/bashrc/.bash_aliases: General Bash Aliases

# ---------------- General Commands ---------------------------------------------------

# Setup some colors to use later in interactive shell or scripts
export COLOR_NC='\033[0m' # No Color
export NC=$COLOR_NC
export COLOR_WHITE='\033[1;37m'
export COLOR_BLACK='\033[0;30m'
export COLOR_BLUE='\033[0;34m'
export COLOR_LIGHT_BLUE='\033[1;34m'
export COLOR_GREEN='\033[0;32m'
export COLOR_LIGHT_GREEN='\033[1;32m'
export COLOR_CYAN='\033[0;36m'
export COLOR_LIGHT_CYAN='\033[1;36m'
export COLOR_RED='\033[0;31m'
export COLOR_LIGHT_RED='\033[1;31m'
export COLOR_PURPLE='\033[0;35m'
export COLOR_LIGHT_PURPLE='\033[1;35m'
export COLOR_BROWN='\033[0;33m'
export COLOR_YELLOW='\033[1;33m'
export COLOR_GRAY='\033[1;30m'
export COLOR_LIGHT_GRAY='\033[0;37m'

alias bashrc='. ~/.bashrc; echo ".bashrc reloaded"'
alias colorslist="set | egrep 'COLOR_\w*'" # lists all the colors

#--------------------Apt Get-----------------------------------------------------------
alias apt-i='sudo apt-get install'

apt-clean () {
	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get clean
	sudo apt-get autoclean
	sudo apt-get autoremove
	sudo deborphan | xargs sudo apt-get remove --purge
}

alias birth="sudo aptitude install"
alias searchy="apt-cache search"

# ---------------- Other Commands ------------------------------------------------------
# Shows most used commands, from: http://lifehacker.com/software/how-to/turbocharge-your-terminal-274317.php
alias profileme="history | awk '{print \$5}' | awk 'BEGIN{FS=\"|\"}{print \$1}' | sort | uniq -c | sort -n | tail -n 20 | sort -nr"

# Share current dir
alias sharethisdir="echo 'now sharing cur directory at port 9000'; python -m SimpleHTTPServer 9000"

# Get all IPs OSX/Linux compatable
alias myip='curl "http://www.networksecuritytoolkit.org/nst/cgi-bin/ip.cgi"'


alias wgetdir="wget -r -nH --no-parent"
alias wgetmirror="wget --mirror -U Firefox/3.0 -p -erobots=off --html-extension --convert-links"

# Open files for open apps!
alias openapps='lsof -P -i -n'

# Alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

function pss() { /bin/ps $@ -u $USER -o pid,%cpu,%mem,command ; }

