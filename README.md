OpenCV 

Installation and Usage
If you have previous/other manually installed (= not installed via pip) version of OpenCV installed (e.g. cv2 module in the root of Python's site-packages), remove it before installation to avoid conflicts.
Select the correct package for your environment:

Packages for standard desktop environments (Windows, macOS, almost any GNU/Linux distribution)

Option 1 - Main modules package: pip install opencv-python
Option 2 - Full package (contains both main modules and contrib/extra modules): pip install opencv-contrib-python (check contrib/extra modules listing from OpenCV documentation)
Import the package:

import cv2

All packages contain Haar cascade files. cv2.data.haarcascades can be used as a shortcut to the data folder. For example:

