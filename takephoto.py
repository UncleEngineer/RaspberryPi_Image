import cv2
from datetime import datetime
import time
# Windows dependencies
# - Python 2.7.6: http://www.python.org/download/
# - OpenCV: http://opencv.org/
# - Numpy -- get numpy from here because the official builds don't support x64:
#   http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

# Mac Dependencies
# - brew install python
# - pip install numpy
# - brew tap homebrew/science
# - brew install opencv

cap = cv2.VideoCapture(0)
cap.set(3,1024) #width=640
cap.set(4,786)

time.sleep(2)

ret, frame = cap.read()
cv2.imshow("test", frame)
time.sleep(3)
dt = datetime.now().strftime('%Y%m%d %H%M%S')
out = cv2.imwrite('Photo-%s.jpg'%(dt), frame)

cap.release()
print 'Done'