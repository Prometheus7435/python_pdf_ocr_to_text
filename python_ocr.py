# Let's try a boilerplate script I found, and modified, at
# https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/

import os
# from PIL import Image
import pytesseract
from pdf2image import convert_from_path


def save_pages(pdf, pages):
    for i, page in enumerate(pages):
        page.save(os.path.basename(pdf[:-4]) +
                  "_page_" + str(i + 1) + ".jpg", 'JPEG')


def pdf_parse(pdf):
    """
    The recognized text is stored in variable text
    Any string processing may be applied on text
    Here, basic formatting has been done:
    In many PDFs, at line ending, if a word can't
    be written fully, a 'hyphen' is added.
    The rest of the word is written in the next line
    Eg: This is a sample text this word here GeeksF-
    orGeeks is half on first line, remaining on next.
    To remove this, we replace every '-\n' to ''
    """
    pages = convert_from_path(pdf, 500)

    outfile = pdf[:-3] + 'txt'

    # you can save the pages as images but it is not neccessary in order for the script to work
    # for i, page in enumerate(pages):
    #     page.save(os.path.basename(pdf[:-4]) +
    #               "_page_" + str(i + 1) + ".jpg", 'JPEG')

    with open(outfile, 'a') as text_results:

        for i in pages:
            # for i in range(len(pages)):
            # filename = os.path.basename(
            # pdf[:-4]) + "_page_" + str(i + 1) + ".jpg"

            # Recognize the text as string in image using pytesserct
            text = str(((pytesseract.image_to_string(i))))
            # text = str(((pytesseract.image_to_string(Image.open(filename)))))

            text = text.replace('-\n', '')

            text_results.write(text)


if __name__ == '__main__':
    # DOC_FOLDER = input("Where are the pdf's you want to scrub?\n")
    DOC_FOLDER = r'/home/zach/Coding/python_ocr/'
    PDFS = [os.path.join(DOC_FOLDER,
                         pdf) for pdf in os.listdir(
        DOC_FOLDER) if pdf.endswith('.pdf')]
    for pdf in PDFS:
        pdf_parse(pdf)
