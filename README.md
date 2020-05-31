# Automatic-Number-Plate-Recognition-System

An automatic number plate recognition system using opencv and tesseract-OCR

Flow:
1. Reading the original image
2. Resizing the image using imutils
3. Grayscale conversion
4. Noise removal with iterative bilateral filter
5. Canny edge detection
6. Drawing and selection of contours
7. Masking the entire image except the plate
8. Conversion of image into string using tesseract

Requirements:

Pytesseract:0.3.4

tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe (64 bit) resp.(0.3.4)

Link: https://github.com/UB-Mannheim/tesseract/wiki

imutils:0.5.3

Opencv:4.2.0

Numpy:1.18.1



