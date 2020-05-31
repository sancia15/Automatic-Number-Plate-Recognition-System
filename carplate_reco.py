import numpy as np
import cv2
import imutils
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read the image file(Original image)
image = cv2.imread('Car1.jpg')

# Resize the image - change width to 500 using imutils
image = imutils.resize(image, width=500)

# Display the original image
cv2.imshow("1:Original Image", image)
cv2.waitKey(0)

# RGB to Gray scale conversion
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("2: Grayscale Conversion", gray)
cv2.waitKey(0)

# Noise removal with iterative bilateral filter(removes noise along with edges marked)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("3:  Bilateral Filter", gray)
cv2.waitKey(0)

# Find Edges of the grayscale image
edged = cv2.Canny(gray, 170, 200)
cv2.imshow("4: Canny Edges", edged)
cv2.waitKey(0)

# Find contours based on Edges detected
cnts, new  = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Create copy of original image to draw all contours
img1 = image.copy()
cv2.drawContours(img1, cnts, -1, (0,255,0), 3)
cv2.imshow("5: All Contours", img1)
cv2.waitKey(0)

#sort contours based on their area keeping minimum required area as '20' (anything smaller than this will not be considered)
cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:20]
NumberPlateCnt = None #we currently have no Number plate contour
# Top 20 Contours to find number plate
img2 = image.copy()
cv2.drawContours(img2, cnts, -1, (0,255,0), 3)
cv2.imshow("6: Top 20 Contours", img2)
cv2.waitKey(0)

# loop over our contours to find the best possible approximate contour of number plate
#To find the topmost area that is rectangular and that area is the largest of all areas with rectangular in shape
count = 0
increment =7
for c in cnts:
        perimeter = cv2.arcLength(c, True) #Getting perimeter of each contour
        approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)
        if len(approx) == 4:  # Select the contour with 4 corners
            NumberPlateCnt = approx #This is our approx Number Plate Contour
            break


# Drawing the selected contour on the original image
#print(NumberPlateCnt)
cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 3)
cv2.imshow("7: Final Image With Number Plate Detected", image)
cv2.waitKey(0)

#Masking entire image except the plate , convert it into zeros array
masked = np.zeros(gray.shape,np.uint8)
new_image = cv2.drawContours(masked,[NumberPlateCnt],0,255,-1)
new_image = cv2.bitwise_and(image,image,mask=masked)
#new_img= Image.open('plate.jpg')
cv2.imshow("8: Final_output",new_image)     #The final image showing only the number plate.
cv2.waitKey(0)


# Use tesseract to covert image into string
#thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,85,11)
config=('-l eng --oem 1 --psm 3')# 3 is default
text= pytesseract.image_to_string(new_image,config= config)
print("Plate_Number:", text)
cv2.waitKey(0)
cv2.destroyAllWindows()
