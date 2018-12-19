# ChiPy 2018 *Welcome to CircuitPython* Workshop
Content for Chicago Linux User's Group Project Night Workshop, 20 December 2018.

The following instructions walk through setup needed to complete this workshop. 

## Setup
For this workshop, participants will want to install Mu editor.

## To install Mu editor on Mac or Windows:
Windows users may install Mu from [here](https://codewith.mu/en/download).

Mac users may install Mu from [here](https://codewith.mu/en/download).

## To install Mu editor on Linux x86:
Linux users must be running Python 3.6 or newer. Install by running `sudo apt install python3`.
Then, install `pip3` by running `sudo apt install python3-pip`.

Next, create a virtual environment: `python3 -m venv .muenv`. Follow the instructions to
install `venv` if it is not already installed. To activate the virtual environment, run
`source .muenv/bin/activate`. Once inside the virtual environment `(.muenv)`, install Mu
by running `pip3 install mu-editor`.

Linux users must add their user to the `dialout` group to access the serial console output. From
the command line, run `nano /etc/group`. Find the line with `dialout:` and add your user to the
end of the line, after a comma with no space, i.e. `dialout:foo,your_user`. Then, log out of the
user and log back in for the change to take affect.

## Running Mu editor
To run Mu on Windows, double-click the icon.

To run Mu on Mac, double-click the icon in the Applications folder.

To run Mu on Linux, from inside the virtual environment, type `python3 -m mu` or `mu-editor` 
into the command line.

## Inside Mu editor
Once Mu is opened, it will present a list of options. For this workshop, choose "Adafruit
CircuitPython".

If there is no CircuitPython compatible board plugged in when the editor is opened, there will
be a dialog box that starts with "Could not find an attached Adafruit CircuitPython device".
This is normal.

## Content for Workshop
This repo contains all the content used in the workshop. To access it during the workshop,
you may view it on the web as you follow along. You may wish to have the files available
locally. To do this, you can clone the repo using `git`, visit the repo on the web and 
click on the "Clone or download" button and choose "Download ZIP", or use the [zip download
link](https://github.com/kattni/ChiPy_2018/archive/master.zip).
