# 01 Git Basics

Git is a version control system based on a tree of hashed patches called
commits. This helps understand the evolution of your code, undo mistakes, and
collaborate with others. Let's demo a few of the things you can do with git.

## Work with branches

A branch is a named series of commits. You often have one primary branch (e.g.
`main`), with short-lived branches to work on features and functionality. Some
projects also use branches as a way to version their releases.

### Check out an existing branch

Run `git branch`. It will show all the repo's branches, with an asterisk next to
your currently-checked-out branch. Make sure it has an asterisk next to
`lab/01-git-basics`. If not, run the following to check it out:

```shell
git checkout lab/01-git-basics
```

### Create a new branch

You can also create a new branch. By default, it will be based on the current 
branch (i.e. `lab/01-git-basics`).

```shell
git checkout -b lab/01-git-basics-demooo
```

### Rename a branch

Sometimes you need to rename a branch. You can do this with the `-m` option.

```shell
git branch -m lab/01-git-basics-demo
```

## Work with commits

A commit is an atomic set of patches to your code. Commits tell a story 
about how the code evolved. Let's try making some commits.

### Commit a modification

Git is all about tracking modifications to your code. Let's try that out:

=== "macOS"

    ```shell
    # Make a dummy change to the README
    echo "DukeHacker was here!" >> README.md
    
    # Commit it
    git commit -a -m "Says hi to the README."
    ```

=== "Windows"

    ```shell
    # Open README.md in your favorite text editor and add "DukeHacker was here!" 
    # to the end of the file. Save and exit.
    
    # Commit it
    git commit -a -m "Says hi to the README."
    ```

The `-a` tells git to include all _modifications_. The `-m` tells git you're
going to pass a commit-message directly on the command-line. Without `-m` it
will open your shell's default text editor to draft the message instead. Usually
this is `vim` on Unix-based systems.

!!! warning

    If you end up in `vim` and are not familiar it, then you can type `a` to go 
    into _append mode_ to edit content, followed by `ESC` to exit _append mode_,
    plus `:wq` followed by `ENTER` to write your changes and quit editing.

### Commit a new file

Above we modified an existing file. _Git avoids tracking new files_ unless you
explicitly ask it to. So, let's try adding a new file.

```shell
cp README.md new_file.md

# Observe that git is aware of the untracked file
git status

# Add and commit the file
git add .  # Adds all new files at or under the current directory (.)
git commit -m "Adds new file."
```

Note that we omitted `-a` on the commit because we explicitly added the change
on the prior line.

### Revert some changes

Sometimes you realize you made a mistake and want to back it out. Git allows you
to do this by reverting commits. This essentially creates a new commit with the
opposite changes of the one you would like to back out. There are two ways we
can do this.

If you want to revert your most recent change(s), you can ask git to roll back
relative to the `HEAD` commit (i.e. your most recent commit). Let's revert the
second most-recent commit where we modified the README.

```shell
git revert --no-edit HEAD~1
```

The `--no-edit` option tells git to use a canned commit-message for the revert
commit.

You can also revert commits by their exact hash (e.g. if it's older and using
offsets is inconvenient).

```shell
git log  # find the "Adds new file." commit hash
git revert --no-edit {hash from above}

# Finally, go back to the main branch
git checkout main
```

## Further reading

We scratched the very basics of working with Git. For more comprehensive 
tutorials, refer to:

- [the official tutorial](https://git-scm.com/docs/gittutorial), and
- [the official book](https://git-scm.com/book/en/v2),
- [branching strategies (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops)
