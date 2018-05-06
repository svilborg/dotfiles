#!/usr/bin/env bash
# General Bash Aliases

# ---------------- General Commands ---------------------------------------------------

# Setup some colors to use later in interactive shell or scripts
export COLOR_NC='\033[0m' # No Color
export NC=${COLOR_NC}
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

export COLOR_BG_NC='\033[49m' # No BG Color
export COLOR_BG_WHITE='\033[1;107m'
export COLOR_BG_GREEN='\033[0;42m'
export COLOR_BG_RED='\033[0;41m'
export COLOR_BG_YELLOW='\033[1;43m'

export STYLE_BOLD=$(tput bold)
export STYLE_NORMAL=$(tput sgr0)

alias bashrc='. ~/.bashrc'
alias colorslist="set | egrep 'COLOR_\w*='" # lists all the colors

# ---------------- Other Commands ------------------------------------------------------
# Shows most used commands, from: http://lifehacker.com/software/how-to/turbocharge-your-terminal-274317.php
alias profileme="history | awk '{print \$5}' | awk 'BEGIN{FS=\"|\"}{print \$1}' | sort | uniq -c | sort -n | tail -n 20 | sort -nr"

# Share current dir
alias sharethisdir="echo 'now sharing cur directory at port 9000'; python -m SimpleHTTPServer 9000"

# Get all IPs OSX/Linux compatible
alias myip='curl "http://www.networksecuritytoolkit.org/nst/cgi-bin/ip.cgi"'

#Get IP
alias ipaddr="ifconfig | grep 'inet addr'"

alias wgetdir="wget -r -nH --no-parent"
alias wgetmirror="wget --mirror -U Firefox/3.0 -p -erobots=off --html-extension --convert-links"

# Open files for open apps!
alias openapps='lsof -P -i -n'

alias py="python"

# Alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

function pss() { /bin/ps $@ -u ${USER} -o pid,%cpu,%mem,command ; }

function make-list() {
    make -qp | awk -F':' '/^[a-zA-Z0-9][^$#\/\t=]*:([^=]|$)/ {split($1,A,/ /);for(i in A)print A[i]}'
}

# ======================== Sys Resources ==============

## pass options to free ##
alias meminfo='free -m -l -t' ## get top process eating memory
alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10' ## get top process eating cpu ##
alias pscpu='ps auxf | sort -nr -k 3'
alias pscpu10='ps auxf | sort -nr -k 3 | head -10' ## Get server cpu info ##
alias cpuinfo='lscpu' ## older system use /proc/cpuinfo ##
alias gpumeminfo='grep -i --color memory /var/log/Xorg.0.log'

json() {
    if [ -t 0 ]; then # argument
        python -mjson.tool <<< "$*" | pygmentize -l javascript
    else # pipe
        python -mjson.tool | pygmentize -l javascript
    fi
}

scan-ports () {
    echo "Scanning TCP ports..."

    for p in {1..1023}
    do
        (echo >/dev/tcp/localhost/${p}) >/dev/null 2>&1 && echo " - $p open"
    done
}


pathmunge () {
        if ! echo "$PATH" | /bin/grep -Eq "(^|:)$1($|:)" ; then
           if [ "$2" = "after" ] ; then
              PATH="$PATH:$1"
           else
              PATH="$1:$PATH"
           fi
        fi
}
