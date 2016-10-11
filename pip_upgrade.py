"""
Version for python 2.7
For python 3.5 on linux change 'pip' to 'pip3'
"""

import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
