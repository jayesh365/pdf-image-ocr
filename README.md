# pdf-image-ocr
Program to find text fields in pdfs and convert to images for OCR to read.

To use the program, place your desired pdf into `assests/pdf`.

Now in `main.py` change the coordinates in line 9, 10 (x1, y1, x2, y2). You can always add more fields to parse.

Finally type the command in your terminal: `python main.py`.

Dependencies: &nbsp;**pdf2image** [![pdf2image](https://badge.fury.io/py/pdf2image.svg)](https://pypi.org/project/pdf2image/1.5.4/)
&nbsp;**pytesseract** [![pytesseract](https://img.shields.io/pypi/v/pytesseract.svg)](https://pypi.org/project/pytesseract/)
&nbsp;**pillow** [![pillow](https://img.shields.io/pypi/v/pillow.svg)](https://pypi.org/project/Pillow/)
