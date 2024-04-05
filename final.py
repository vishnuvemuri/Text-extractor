from flask import Flask, render_template, request, redirect
import pytesseract
import traceback
import cv2
from pdf2image import convert_from_path

app = Flask(__name__)
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)


def pdf_to_images(pdf_path):
    images = convert_from_path(
        pdf_path, 500, poppler_path="C://Program Files//poppler-23.11.0//Library//bin"
    )
    return images


def ocr_on_pdf(pdf_path):
    images = pdf_to_images(pdf_path)
    extracted_text = []
    k = 0
    for image in images:
        j = "C://Users//arjun//Desktop//final//page" + str(k) + ".jpg"
        img = cv2.imread(r"" + j)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        text = pytesseract.image_to_string(image)
        extracted_text.append(text)
        k = k + 1
    return extracted_text


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            if "file" not in request.files:
                return redirect(request.url)

            file = request.files["file"]
            if file.filename == "":
                return redirect(request.url)

            if file:
                file_path = "uploads/sample.pdf"
                file.save(file_path)
                result = ocr_on_pdf(file_path)
                return render_template("result.html", result=result)

        return render_template("index.html")

    except Exception as e:
        # Print the traceback for debugging
        traceback.print_exc()
        return render_template("error.html", error_message=str(e)), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
