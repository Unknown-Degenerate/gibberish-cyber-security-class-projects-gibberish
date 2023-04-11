
import numpy as np
import matplotlib.pyplot as plt #importing matplotlib
import cv2
# load image
img = cv2.imread("test.png")
# say RGB values
print(img)

# cv2.imshow('imagem',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
histr = cv2.calcHist([img],[0],None,[256],[0,256])

# images : it is the source image represented as “[img]”.
# channels : it is the index of channel for which we calculate histogram. For grayscale image, its value is [0] and color image, you can pass [0], [1] or [2] for blue, green or red respectively. # The fact that it isn't RGB irritates me
# mask : mask image. To find histogram of full image, it is given as “None”.
# histSize : this represents our BIN count. For full scale, we pass [256].
# ranges : this is our RANGE. Normally, it is [0,256].


plt.plot(histr) #plotar o histograma
plt.show()  


