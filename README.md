# PDF_OCR
 
This project discovers PDF files in a folder and turns them into text. 

The initial approach for this project was reading the text layer in the PDF files, ultimately this did not work out very well as the quality of the text was generally low. A new approach was taken of first extracting each page to a high resolution JPEG, and then using an OCR library to find any text in the images and export it. Although this approach takes longer, the results seem to be better and was worth the tradeoff in terms of processing time and temp file size.

The program logs success and page count to a text file and lets you know what it is doing as it works, and is suited for conversion of a large number of PDF files that need to be converted and prepared for text analysis. 

Quite a few articles were consulted as things went wrong, these include:

https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/

https://www.techiedelight.com/delete-all-files-directory-python/

https://stackoverflow.com/questions/45480280/convert-scanned-pdf-to-text-python

https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/
