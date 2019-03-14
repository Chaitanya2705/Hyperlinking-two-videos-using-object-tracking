import cv2
import numpy as np
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('USCTwo.mp4', fourcc,20.0,(352,288))
for i in range (1,9001):
    img=cv2.imread("D:\CS576\Project\Sample1\\" +str(i)+".jpg")
    out.write(img)
    cv2.imshow('Display',img)
      
    k= cv2.waitKey(1) & 0xff
    if k==27:
        cv2.destroyAllWindows()
out.release()
