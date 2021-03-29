'''
This is a program to read all images related to logic gates in the circ1 file..
The path variable can be changed according to the path of the img files on the device.
'''

from cv2 import cv2
import numpy

path=r'C:\Users\aaftab khan\Desktop\minipro\gt_imgs\%s%s%s.png'
path_not=r'C:\Users\aaftab khan\Desktop\minipro\gt_imgs\NOT%s.png'

def circ_view(a,b,gate_name):
    img = cv2.imread(path%(gate_name,a,b),1)
    cv2.imshow('%s'%gate_name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def not_circ_view(a):
    img = cv2.imread(path_not%(a),1)
    cv2.imshow('NOT',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



