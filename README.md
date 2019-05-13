# pdf-image-ocr

[![pdf2image](https://img.shields.io/badge/pdf2image-pypi-blue.svg)](https://pypi.org/project/pdf2image/1.5.4/)
[![pytesseract](https://img.shields.io/badge/pytesseract-pypi-red.svg)](https://pypi.org/project/pytesseract/)
[![pillow](https://img.shields.io/badge/pillow-pypi-orange.svg)](https://pypi.org/project/Pillow/)
[![poppler](https://img.shields.io/badge/poppler-src-yellowgreen.svg)](http://blog.alivate.com.au/poppler-windows/)

Program to find text fields in pdfs and convert to images for OCR to read.

To use the program, place your desired pdf into `assests/pdf`.

Now in `main.py` change the coordinates in line 9, 10 (x1, y1, x2, y2). You can always add more fields to parse.

Finally type the command in your terminal: `python main.py`.
