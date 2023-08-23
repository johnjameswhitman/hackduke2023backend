# 00 Prerequisites

Today we're going to be writing code in Python and versioning it in Git. To get
your environment ready let's install those dependencies and check out the lab
code. Here's a checklist of what we're going to do:

- Install Git
- Install Python 3.8+
- Set up lab environment

If you get stuck, ask for help!

## Confirm Git installation

There's a good chance you already have Git installed. See with:

=== "macOS"

    ```shell
    # In Terminal.app
    git --version  # if missing will prompt you to install command line developer tools.
    ```

=== "Windows"

    ```shell
    # In PowerShell
    git --version
    ```

If you get something along the lines of _command not found_, then let's install
it:

- macOS - If `git` was missing above, then macOS should have already prompted
  you to install _command line developer tools_.
- [Windows](https://git-scm.com/download/win) - Install Git from the official
  website.

If you're running Linux, then I assume you know the right package management
commands to install Git.

## Confirm Python installation

You're going to need at least Python 3.8 for this lab. Run the following and
confirm whether you have that version installed:

=== "macOS"

    ```shell
    # In Terminal.app
    python3 --version  # should output at least 3.8
    ```

=== "Windows"

    ```shell
    # In PowerShell
    python --version  # should output at least 3.8
    ```

!!! note

    Some systems will alias `python` to `python3`, but macOS's bundled
    interpreter does not. Once we set up a virtual environment below, we'll use
    `python` to refer to the virtual environment's interpreter.

If you do not already have a Python interpreter on your system, then refer to
the instructions for your operating system below:

- [macOS](https://docs.python.org/3/using/mac.html)
    - Make sure `/usr/local/bin` is in your `$PATH`.
    - If it is not, then open `~/.zshrc` and add the following line:
      `export PATH=/usr/local/bin:$PATH`.
- [Windows](https://docs.python.org/3/using/windows.html#windows-store)
    - The easiest way to install Python on Windows is through the Microsoft Store.

## Set up lab environment

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
pytest tests  # should all pass
python manage.py runserver  # starts the API
```

At this point your tests should all be passing, and you should see `ok` when you
load the API at: [http://127.0.0.1:3000/status](http://127.0.0.1:3000/status)
