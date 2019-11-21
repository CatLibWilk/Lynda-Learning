# Chpt. 1
- git add stages a document/documents
    - use git checkout [filename] to discard changes to a file in the working directory (ie. pulls the version that is in the staging environment to working environment)
- git reset HEAD [filename] will remove a file from the staging area (`pull back from commit`)

- deleting files
    - git checkout [filename] will take from staging and put back in working if you've deleted a file
    - git add -A will move the deletion into staging
    - git reset HEAD [filename] will unstage the deletion
    - git rm [filename] will delete a file from working and move the deletion into staging

- managing log
    - git log shows the hashes for each commit
    - use git checkout [hash] to return to the given commit in `detached head state`
    - detached head state: 'sandbox' version of project starting at the given commit
        - to save the changes you make, git add/commit, then use git branch [new_branch_name] [partial_hash_given] 

- State control with branches
    - git branch [branchname] will create a branch but keep state in current, so like a save point
    - git checkout [branchname] will put you in the new branch to sandbox stuff
    - change branch name: git branch -m [original_branch_name] [newname]
    - delete: git branch -D [branchname]

    - revert to second-to-last commit:
        - git revert [hash_of_current_commit]
        - in prompt: I to enter insert mode, make note, esc to exit insert mode, ctrl+q, then "w!' to save, then ctrl+q! to exit
        - now current commit will be the one you reverted to

# Chpt. 2 Working with Projects
- Cloning Branches
    - git clone only downloads the master, but has all the info about other branches
    - `git branch -a` will show names of other branches
    - to download `git checkout -b [a_name_you_give] [name_of_branch_in_list]`
        - ex. git checkout -b 02_01 origin/02_01
    - to pull all the branches and master at once:
        - `git clone --mirror [repo_url] .git`
            - ex. git clone --mirror http://github.com/awpenn/id_db.git .git (yes, .git 2x)
        - this will clone 'bare repo', which is empty except for the .git directory that tracks all the files, then:
        - `git config --bool core.bare false` , then:
        - `git reset --hard`
    
    - using a github branch as a template for another project
        - `git clone -b [branch_name] [git_repo_url]`
        - `rm -rm .git` ie. deleting .git folder essentially makes it no longer a git repo
        - then `git init` initializes it as a new repo and a new project