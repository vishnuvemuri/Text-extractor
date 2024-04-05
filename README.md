# Text_extractor
Using 
OCR-PDF-Converter

This Flask application allows users to upload a PDF file, convert it into images, perform OCR (Optical Character Recognition) on each image, and display the extracted text. The application uses Tesseract for OCR and supports PDF conversion using pdf2image.

Prerequisites
Before running the application, make sure you have the following installed:

Python 3.x
Flask
pytesseract
OpenCV (cv2)
pdf2image
Tesseract OCR


#Installation
Install dependencies:


**pip install Flask pytesseract opencv-python pdf2image**

Install Tesseract OCR: Follow the instructions here to install Tesseract OCR on your system. Make sure to set the Tesseract executable path correctly in the pytesseract.tesseract_cmd variable in the code.

Install Poppler: Download and install Poppler from here. Set the Poppler binary path in the pdf_to_images function if needed.
Make sure to replace the placeholder texts like [Tesseract OCR installation instructions](https://github.com/tesseract-ocr/tesseract) and [Poppler download link](https://poppler.freedesktop.org/) with the actual links to the relevant resources.


**How to Use**
1. Access the web application at http://localhost:5000/.
2. Upload a PDF file using the provided form.
3. Click the "Submit" button.
4. Wait for the OCR process to complete.
5. View the extracted text on the result page.

**Folder Structure**
uploads/: Folder to store uploaded PDF files.
templates/: HTML templates for the web application.
app.py: Main Flask application file.


**Acknowledgments**
Flask: Web framework for Python.
pytesseract: Python wrapper for Tesseract OCR.
pdf2image: Convert PDF to images using Python.



