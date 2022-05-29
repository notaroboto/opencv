import cv2 as cv
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"E:\Apps\Tesseract-OCR\tesseract.exe"
# https://projectgurukul.org/python-text-detection-extraction-opencv-ocr/ 
capture = cv.VideoCapture(0)

while True:
    ret,img = capture.read()

    # raw_data = pytesseract.image_to_data(img)

    # for count, data in enumerate(raw_data.splitlines()):
    #     if count > 0:
    #         data = data.split()
    #         if len(data) == 12:
    #             x, y, w, h, content = int(data[6]), int(data[7]), int(data[8]), int(data[9]), data[11]
    #             cv.rectangle(img, (x, y), (w+x, h+y), (255, 255, 0), thickness=2)

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lower = np.array([0, 0, 218])
    upper = np.array([157, 54, 255])
    mask = cv.inRange(hsv, lower, upper)
    ret, mask = cv.threshold(gray, 180, 255, cv.THRESH_BINARY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5,3))
    dilate = cv.dilate(mask, kernel, iterations=5)
    
    contours, hierarchies = cv.findContours(dilate, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # print(f'{len(contours)} contour(s) found!')

    for contour in contours:
        # get rectangle bounding contour
        [x, y, w, h] = cv.boundingRect(contour)

        # Don't plot small false positives that aren't text
        if w < 35 and h < 35:
            continue

        # draw rectangle around contour on original image
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)



    if ret:    
        cv.imshow('Video', img)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
