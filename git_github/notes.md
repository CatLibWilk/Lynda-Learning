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
