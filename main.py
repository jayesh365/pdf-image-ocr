from ocr import ocr
from pageConverter import crop
from pdfConverter import pdfToImage


def main():
    pdfToImage('assets/pdfs/form.pdf')
    image = "assets/images/page.jpg"
    crop(image, (95, 634, 1557, 708), 'assets/images/date.jpg')
    crop(image, (99, 776, 1557, 1008), 'assets/images/comments.jpg')
    print(ocr('assets/images/date.jpg'))
    print(ocr('assets/images/comments.jpg'))


if __name__ == '__main__':
    main()
