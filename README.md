# PDF_OCR
 
This project discovers PDF files in a folder and turns them into text. 

The initial approach for this project was reading the text layer in the PDF files, ultimately this did not work out very well as the quality of the text was generally low. A new approach was taken of first extracting each page to a high resolution JPEG, and then using an OCR library to find any text in the images and export it. Although this approach takes longer, the results seem to be better and was worth the tradeoff in terms of processing time and temp file size.