# Import libraries
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import glob

#build a list of all PDFS in the directory
#this will look foe all PDFs in the local folder and can be modified to work with subfolders
pdfs = glob.glob(r"*.pdf")

for pdf_path in pdfs:

	# Path of the pdf
	PDF_file = f"{pdf_path}"

	print("Part #1 : Converting PDF to images for",PDF_file)

	# Store all the pages of the PDF in a variable
	pages = convert_from_path(PDF_file, 500)

	# Counter to store images of each page of PDF to image
	image_counter = 1

	# Iterate through all the pages stored above
	for page in pages:

		# Declaring filename for each page of PDF as JPG
		# For each page, filename will be:
		# PDF page 1 -> page_1.jpg
		# ....
		# PDF page n -> page_n.jpg
		filename = f"page_"+str(image_counter)+".jpg"
		
		# Save the image of the page in system
		page.save(filename, 'JPEG')

		# Increment the counter to update filename
		image_counter = image_counter + 1


	print("Part #2 - Recognizing text from the images using OCR for",PDF_file)


	# Variable to get count of total number of pages
	filelimit = image_counter-1

	# Creating a text file to write the output
	outfile = f"{PDF_file}-output.txt"

	# Open the file in append mode so that
	# All contents of all images are added to the same file
	f = open(outfile, "a")

	print(f"Iterate from 1 to total number of pages {filelimit + 1}")
	for i in range(1, filelimit + 1):

		# Set filename to recognize text from
		# Again, these files will be:
		# page_1.jpg
		# page_2.jpg
		# ....
		# page_n.jpg
		filename = "page_"+str(i)+".jpg"
			
		#Recognize the text as string in image using pytesserct
		text = str(((pytesseract.image_to_string(Image.open(filename)))))

		# The recognized text is stored in variable text
		# Any string processing may be applied on text
		# Here, basic formatting has been done:
		# In many PDFs, at line ending, if a word can't
		# be written fully, a 'hyphen' is added.
		# The rest of the word is written in the next line
		# Eg: This is a sample text this word here GeeksF-
		# orGeeks is half on first line, remaining on next.
		# To remove this, we replace every '-\n' to ''.
		text = text.replace('-\n', '')	

		#Finally, write the processed text to the file.
		f.write(text)
		print(f"{i} of {filelimit + 1} complete - {PDF_file}")

	# Close the file after writing all the text.
	f.close()
	print("File closed")

	#log file data name, pages
	print(f"Log file appended - {PDF_file},{filelimit + 1}")
	logfile = open("logfile.txt", "a")
	file_info = f'{PDF_file},{filelimit + 1},{len(text)}\n'
	logfile.write(file_info)
	logfile.close()

	#Find and delete all jpg files in the directory
	print("Delete temp jpg files")
	jpgs = glob.glob(r"*.jpg")
	for jpg_file in jpgs:
		try:
			print(f"Removed {jpg_file}",end=" ")
			os.remove(jpg_file)
		except:
			print(f"\nError with {jpg_file}\n")
			pass

	print(f"Finished with {outfile}\n")

#https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/
#https://www.techiedelight.com/delete-all-files-directory-python/
#https://stackoverflow.com/questions/45480280/convert-scanned-pdf-to-text-python
#https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/
