
from cv2 import COLOR_BGR2GRAY
import numpy as np
import math
import cv2

def vec_gaussian(img: np.ndarray, variance: float) -> np.ndarray:
    # For applying gaussian function for each element in matrix.
    sigma = math.sqrt(variance)
    cons = 1 / (sigma * math.sqrt(2 * math.pi))
    return cons * np.exp(-((img / sigma) ** 2) * 0.5)

def get_gauss_kernel(kernel_size: int, spatial_variance: float) -> np.ndarray:
    # Creates a gaussian kernel of given dimension.
    arr = np.zeros((kernel_size, kernel_size))
    for i in range(0, kernel_size):
        for j in range(0, kernel_size):
            arr[i, j] = math.sqrt(
                abs(i - kernel_size // 2) ** 2 + abs(j - kernel_size // 2) ** 2
            )
    return vec_gaussian(arr, spatial_variance)

def get_slice(img: np.ndarray, x: int, y: int, kernel_size: int) -> np.ndarray:
    # convolutions accross the image
    half = kernel_size // 2
    return img[x - half : x + half + 1, y - half : y + half + 1]

def bilateral_filter(
    img: np.ndarray,
    spatial_variance: float,
    intensity_variance: float,
    kernel_size: int,
) -> np.ndarray:
    img2 = np.zeros(img.shape)
    gaussKer = get_gauss_kernel(kernel_size, spatial_variance)
    sizeX, sizeY = img.shape
    for i in range(kernel_size // 2, sizeX - kernel_size // 2):
        for j in range(kernel_size // 2, sizeY - kernel_size // 2):
            imgS = get_slice(img, i, j, kernel_size) # image window
            imgI = imgS - imgS[kernel_size // 2, kernel_size // 2] # Ip-Iq  substract intensity 
            imgIG = vec_gaussian(imgI, intensity_variance) # G sigma(r) G(Ip-Tq) compute gaussian distribution for neighboring pixel intensities
            weights = np.multiply(gaussKer, imgIG) #  weighted avg of pixels Gaussina spactial distribution and gaussian intensity distribution
            vals = np.multiply(imgS, weights)  # weighted of combination of both the gaussian distributions 
            val = np.sum(vals) / np.sum(weights) # divide by Wp
            img2[i, j] = val
    return img2


image = cv2.imread('../Resources/Photos/park.jpg')

cv2.imshow("park",image)
gray = cv2.cvtColor(image,COLOR_BGR2GRAY)
gray_input = gray/255
gray_input = gray_input.astype("float32")
bilateral_blur = bilateral_filter(gray_input,10,15,25)
bilateral_blur = bilateral_blur*255
out = np.uint8(bilateral_blur)
cv2.imshow("bilateral",out)

bilateral_blur_cv2 = cv2.bilateralFilter(gray,10,15,25)
cv2.imshow("cv2 bilateral filter",bilateral_blur_cv2)

cv2.waitKey(0)