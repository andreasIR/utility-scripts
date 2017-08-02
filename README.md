# utility-scripts

Output Description for Users:


The output DPKG difference refers to the mismatched system packages between a fresh Ubuntu installation and the current Ubuntu system.
These mismatched packages are separated into updates and installed packages along with a simple counter for user conveniance.

The associated pip differences refers to the mismatched python packages from a fresh pip installation to the current Ubuntu system.













Input Description for Programmers:


This script compares DPKG files and pip files that each include a list of packages
the output of this file is the difference of the initial list to the second list passed as uargs

The pipdiff function is a simple package comparison, whereas the dpkgdiff func is more complex, extracting essential information only.


Expected usage command: python3 filediff.py preupdatefile.txt postupdatefile.txt
