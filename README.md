# Texture Analysis
A project made based on the concepts of Content Based Image Retrieval(CBIR) and Local Binary Pattern(LBP). There are some pre-requisites for running this project on your system. These are as follows:

## System Requirements(Basic)
It goes without saying you would require a python version installed in your system. I have written this using python 3.7. So that is the prefered version.And to run from the terminal you would need to set your Environment variables for your system(use google please).

These following import statements are necessary to run the main file `lbp_test.py`
```python
import cv2 # for the image reading purposes, this is opencv-python module
import numpy as np # for number related operations with entire array of data
import matplotlib.pyplot as plt # for data visualization
import pandas as pd # for dataset manipulations
```
So corresponding libraries must be installed. You can find the command-prompt commands online from [PyPi.org](https://pypi.org/). For easy access I provide them below in the above stated order:

```bash
pip install opencv-python
pip install numpy
pip install matplotlib
pip install pandas
```
## System Requirements(Optional)
These should be enough to run the LBP file. But if you want to run the web scrapper and download the brodatz dataset images you will need the following

```bash
pip install requests
pip install beautifulsoup4
```

## Executing
The basic lbp_test.py file requires the following command to run from the terminal
