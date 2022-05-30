from cv2 import COLOR_BGR2GRAY
import numpy as np
import cv2
import math


def gaussianBlur(sigma, kernel_size):
    gaussian_filter = np.zeros((kernel_size,kernel_size),np.float32)
    m = kernel_size//2
    n = kernel_size//2
    
    for x in range(-m,m+1):
        for y in range(-n,n+1):
            # gaussian formula 
            x1 = 2*np.pi*(sigma**2)
            x2 = math.exp(-(x**2+y**2)/(2*sigma**2)) # center pixel has greater intensity (hence -m to m+1 range)

            gaussian_filter[x+m,y+n]=(1/x1)*x2
    
    return gaussian_filter    

def convolution(img,kernel):
    k_x,k_y = kernel.shape
    img_pad = np.pad(img,pad_width=((k_y//2,k_x//2),(k_x//2,k_y//2)),mode='constant',constant_values=0).astype(np.float32)
    image_conv = np.zeros(img.shape)
    for i in range (0,img_pad.shape[0]-k_x+1):
        for j in range (0,img_pad.shape[1]-k_y+1):
            x = img_pad[i:i+k_x,j:j+k_y]
            x = x.flatten() * kernel.flatten()
            image_conv[i,j] = x.sum()/kernel.sum()
    
    return image_conv.astype(np.uint8)


# array = np.array([[1,3,4,2,1],[3,3,5,4,1],[1,4,2,3,7],[8,3,2,4,1],[2,6,3,7,2]])
# kernel = np.array([[1,2,1],[2,4,2],[1,2,1]])

# convolution(array,kernel)

image = cv2.imread('../Resources/Photos/park.jpg')
print(image.shape)
cv2.imshow("park",image)
gaussian_filter = gaussianBlur(3,9)

gray = cv2.cvtColor(image,COLOR_BGR2GRAY)
print(gray.shape)
filter_image = np.zeros(gray.shape)
filter_image = convolution(gray,gaussian_filter)
cv2.imshow("filtered park",filter_image)

# filter_image_cv2 = cv2.filter2D(gray,ddepth=-1,kernel=gaussian_filter)
# cv2.imshow("filtered park cv2",filter_image_cv2)
gaussian_filter_cv2 = cv2.GaussianBlur(gray,(9,9),3)
cv2.imshow("gaussian filter",gaussian_filter_cv2)


cv2.waitKey(0)
