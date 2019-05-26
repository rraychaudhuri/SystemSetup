"""
To import all the following libraries by default everytime I start jupyter qtconsole, do the following
(https://stackoverflow.com/questions/35446211/configuring-jupyter-default-imports)

$ ipython profile create

This will create the necessary folders for keeeping the startup file.

$ cd ~/.ipython/profile_default/startup/

In this location create the .ipy file, also read the README 
MAKE SURE TO CREATE AN .ipy FILE SINCE IT HAS % notations

Also after this there may be an initial error in the command line ipython for the matplotlib line.
Use "jupyter console" instead
"""

import os
import sys
import requests as rq
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# excetions show up normally
%xmode plain

# plots show up inline
%matplotlib inline


# Jupyter notebook convert
# jupyter nbconvert my_notebook.ipynb --to markdown --output output.md
# jupyter nbconvert my_notebook.ipynb --to html --output output.html
# jupyter nbconvert my_notebook.ipynb --to html --template basic --output output.html