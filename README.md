# pecan.py

pecan.py is a python program written for the purpose of simplifying the annoying task of checking 100s of machines for the latest Windows patches,
a large enterprise "fleet" of Windows PCs can easily go too long unmaintained, because Windows versions before Windows 10 made it very easy for the 
user to always refuse to apply updates.

To solve this problem, the idea is to install this program on each machine, and run it with it's sole dependency, python3.

The program is still in development, but the goal is to have a program which is capable of reporting maintenance issues on systems to a master server, which does not have control over the servers it is the "master" of, but instead has the control over certain commands.

The master cannot eval or run anything apart from the predefined commands, but if it can, you're free to report any security issue in the GitHub issue tracker.

This program will be given to the intended deployment when it's done, but you can use it and modify it as you wish under the terms of the 
AGPLv3 license. This program is not really that useful unless you're managing an extreme ammount of machines, 
and the task of checking each computer for updates via Windows update would simply take too long to call efficient.
