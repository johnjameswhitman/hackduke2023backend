# Pre-requisites

Today we're going to be writing code in Python and versioning it in git. To get
your environment ready let's install those dependencies and check out the lab
code. Here's a checklist of what we're going to do:

- Install git
- Install Python 3.9+
- Check out the lab code
- Run the lab code
- Play with git (optional, time-permitting)

If you get stuck, ask for help!

## Install git

There's a good chance you already have git installed. See with:

```shell
git --version
```

If you get something along the lines of _command not found_, then let's install
it:

```shell
# macOS
brew install git

# Windows
TODO: find install steps for windows
```

If you're running Linux, then I assume you know the right package management
commands to install git.

## Install Python

You're going to need at least Python 3.9 for this lab. Run the following and
confirm whether you have that version installed:

```shell
# macOS and Linux
python --version  # should output at least 3.9

# Windows
TODO: find command for version on Windows
```

## Pull and run the lab code

Tie the above together to get our lab environment ready.

```shell
# macOS and Linux
# clone the repo and enter it
git clone TODO: path to repo
cd hackduke2023backend
git checkout lab/00-prerequisites

# set up virtual environment to isolate dependencies
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.dev.txt

# test out the API
./run/test  # should all pass
./run/start  # starts the API

# Windows
TODO: find equiv steps for Windows
```

At this point your tests should all be passing, and you should see `ok` when you
load the API at: [http://127.0.0.1:3000/status](http://127.0.0.1:3000/status)

## Play with git

Git is a version control system based on a tree of hashed patches called
commits. This helps understand the evolution of your code, undo mistakes, and
collaborate with others. Let's demo a few of the things you can do with git.

### Confirm you're on the right branch

A branch is a named series of commits. You often have one primary branch (e.g.
`main`), with temporary branches to work on features and functionality. Some
projects also use branches as a way to version their releases.

Run `git branch`. It will show all of the repo's branches, with an asterisk next
to your currently-checked-out branch. Make sure it has an asterisk next to
`lab/00-prerequisites`. If not, run the following to check it out:

```shell
git checkout lab/00-prerequisistes
```

### Commit a modification

Git is all about tracking modifications to your code. Let's try that out:

```shell
# Make a dummy change to the README
echo "$(whoami) was here!" >> README.md

# Commit it
git commit -a -m "Says hi to the README."
```

The `-a` tells git to include all _modifications_. The `-m` tells git you're
going to pass a commit-message directly on the command-line. Without `-m` it
will open your default command-line text editor to draft the message instead.
Usually this is `vim`.

> Warning: If you end up using `vim`, then you can type `a` to go into _append
> mode_, followed by `ESC` plus `:wq` followed by `ENTER` to write and quit
> editing.

### Commit a new file

Above we modified an existing file. _Git avoids tracking new files_ unless you
explicitly ask it to. So, let's try adding a new file.

```shell
echo "I am a new file." > new_file.txt

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
```

