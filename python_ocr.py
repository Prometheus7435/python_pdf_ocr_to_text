# Let's try a boilerplate script I found, and modified, at
# https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/

import os
import sys
# from PIL import Image
import pytesseract
from pdf2image import convert_from_path


def save_pages(pdf, pages):
    for i, page in enumerate(pages):
        page.save(os.path.basename(pdf[:-4]) +
                  "_page_" + str(i + 1) + ".jpg", 'JPEG')


def text_parser(txt):
    """
    If you wanted to incorporate some kind of text parsing based on the results
    from the pdf_parse.
    """
    for line in txt:
        print(line)


def pdf_parse(pdf):
    """
    Documentation from original script this is based on:

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

    # most printers use dpi of 300. Using this, I think, is a good starting point
    # for resolution. The smaller you go, the faster it will run but, potentially,
    # the less accurate it becomes
    pages = convert_from_path(pdf, dpi=300)

    outfile = pdf[:-3] + 'txt'

    # you can save the pages as images but it is not neccessary in order for the script to work
    # save_pages(pdf, pages)

    with open(outfile, 'a') as text_results:

        for i in pages:
            # Recognize the text as string in image using pytesserct
            text = str(((pytesseract.image_to_string(i))))

            text = text.replace('-\n', '')

            text_results.write(text)


if __name__ == '__main__':
    # if you want to run in one command
    DOC_FOLDER = sys.argv[1]

    # interactive with user
    # DOC_FOLDER = input("Where are the pdf's you want to scrub?\n")

    # for testing
    # DOC_FOLDER = r'/home/zach/Coding/python_pdf_ocr_to_text/'

    PDFS = [os.path.join(DOC_FOLDER, pdf)
            for pdf in os.listdir(DOC_FOLDER) if pdf.endswith('.pdf')]

    for pdf_to_parse in PDFS:
        pdf_parse(pdf_to_parse)
