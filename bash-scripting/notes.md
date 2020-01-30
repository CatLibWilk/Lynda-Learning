## Chpt. 1 Working with Bash
Bash (Bourne again Shell)
- Reviewing Common Commands
    - ls -l shows difference between types of members in a directory
        - `drwxrx...` etc. "d" is directory, "-" will be a file
    - man [commandname] will give manual page for a command
    - cat [filename] prints linebyline contents of a file (if is text)
    - more [filename] paginates printout of a long file
    - head [filename] shows first few lines
    - tail [filemane] shows last few lines 
- expansions
    - tilde represents users HOME variable
    - tilde + `-` (`~-`) shows `old pwd`, or the directory that user last moved from 
    - brace expansion: helps with repeated commands featuring different terms or interpolation within a range
         e.g. touch `{one.txt, two.txt, three.txt}` or `touch file_{1..100}.txt will create 100 files as file_1.txt, file_2.txt, etc.
- pipes and redirection
    pipe: takes results of command and redirects it somewhere
        - e.g. `pipe | more` takes results of ls and paginates with more
    redirection: moves results of command, but uses standard input, standard output and standard error.
        - `1>`: standard output `>2` standard error
        - `&>` redirects both stout and error to same place
        - e.g. `cp -v * ../newfolder 1>../success.txt 2>error.txt`: copy all files in current dir into new folder, where successful (-v means verbose printout of execution of cp), write message to success file, where error, write to error file

- grep, awk, cut
    grep: search to things in files
        - basic syntax: `grep [searchterm] [filename]` => `grep andy names.txt`
        - enable color highlighting for terms: ` export GREP_OPTIONS='--color=auto' `
        - `-i` option in command makes case-insensitive
        - can grep the output of commands as well
            - eg. ` ping example.com | grep 'bytes from' `
    awk: scans files for lines that match any of a set of patterns specified 
        - eg: `grep -i break-in auth.log | awk {'print $12'}` = grep file for `break-in`, pipe the results to awk, awk prints the twelveth "column" of the line in a space delimited sense, here returning the IP addresses from the log file that appear to be break-in attempts

    cut: can cut out portions of lines in a file/output of a command
        - eg. ` ping example.com -c 1 | grep 'bytes from' | cut -d = -f 4 ` : ping example.com (`-c 1` means only do it once rather than until the command is stopped), grep lines with 'bytes from' in the line, the use cut to only return the 4th thing delimited (-d) by `=` , in the example, the time for ping to complete

- bash script syntax
    - script starts with interpreter directive (hashbang, shebang)
    - followed by path to bash executable
    - generally: `#!bin/bash`
    
    - template:
        #!bin/bash
        #comment
        commands
- running bash scripts
    - in command line: `bash my.sh` 
    - or, make script executable with `chmod +x ./[filename]` and can run directly by typing filename in CL
        - need `./` because current working directory isn't part of "path executable variable", but if put somewhere like `usr/bin` the could run directly (not good in practice though)

## Chpt. 2 Building Bash Script
- echo
    - `echo`: displays text
    - syntax = `echo [statement]`
    - no quotes, single, double quotes cause different conditions
        - no quotes: need to escape special characters
        - single: nothing in quotes is interpreted, so printed as written, ie. ignores variables (e.g. `$variable`) 
        - double: allows for variables (which can be escaped with backslash if necessary)
    - echo without a statement prints  empty line

- variables
    - var=[value]
    - no spaces, if value needs a space, put in quotes
    - called with `$var`
    - adding attributes to variable
        - `declare` before variable and use `-[attr]`
            - eg. declare -i a=123 : "a is an integer"
        - `-i`: is integer
        - `r`: is read-only
        - `l`: converts value to lowercase
        - `u`: converts value to uppercase 
    - built-in vars
        - `$PWD`: returns working directory
        - `$MACHTYPE`: returns machine type
        - `$HOSTNAME`: returns system name
        - `$ BASH_VERSION`
        - `$SECONDS`: returns how long script has been running
    - command substitution
        - get information back from a command in-script, rather than just running it
        - syntax: [varname]=$([cmd]) e.g. `d=$(pwd)`
    - arithmatic expressions
        - math wrapped in double parenthesis e.g. `$d=((2+2))`
        - bash math only works with integers
            - if need floating-point, need to use `bc` program to process
                - e.g. `g=$(echo 1/3 | bc -l)` returns .33333
    - comparing values
        - double squared brackets, with spaces between the inner brackets and values
            - eg. `[[ "cat" == "cat ]]` returns `0`
        - returns boolean, 0=true, 1=false
        - get value with `$?` in script
        - to compare numbers use operators to tell bash they are numbers
            - `-lt`: less than, `-gt`: greater than, `-le`: less than equal to, `-ge`: greater than equal to, `-eq`: equal, `-ne`: not equal
            - eg. `[[ 20 -lt 100 ]]`, `echo $?` returns `0` for true
        - logical operators
            - `&&`: AND
            - ` | `: OR
            - `!`: NOT

        - checking nullity
            - `-z` is null, `-n` not null

- string manipulation
    - for a='hello', b="world":
        - concatenation: variables next to each other, eg. `$a$b` = 'helloworld'
        - substring: brackets with index, eg. `${a:1}` = 'ello'
            - ask for number of chars after index: `$a{a:1:2}` = 'el'
        - replace text in string:
            - `${[varname]/[what-to-replace]/[what-to-replace-first-instance-with]}`
                - eg. text='one two three', `echo ${text/two/chew}` returns 'one chew three'
            - double-slash before search term replaces all the instances
            - `#` before search term will replace only if is the beginning of the string
            - `%` replaces only if at end of string
- coloring/styling
    - ANSI escape sequences
        - use `echo -e` to enable escaping
        - eg. `echo -e '\033[34;42mColor Text\033[0m'` to coloring output 'Color Text'
        - to reduce typing and typos, can save the escape seqs as variables and use string concatenation where needed
    - can also use `tput` (see `man terminfo` for operations and attributes)