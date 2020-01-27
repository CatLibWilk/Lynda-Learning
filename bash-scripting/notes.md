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