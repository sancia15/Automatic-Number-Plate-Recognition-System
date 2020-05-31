import cv2
import  pytesseract
import imutils
pytesseract. pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#read the image file
img = cv2.imread("car_4.jpg")

#Resizing the image making half width and height
img = cv2.resize(img,None,fx=0.5, fy= 0.5)
#converting into grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Putting the threshold
adaptive_threshold = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)
#config="--psm 3"
text = pytesseract.image_to_string(adaptive_threshold,lang='eng')#config=config
print(text)
#cv2.imshow("gray",gray)
cv2.imshow("adaptive_threshold",adaptive_threshold)
cv2.waitKey(0)
