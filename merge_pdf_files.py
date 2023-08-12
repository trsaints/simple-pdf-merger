from os import walk
from string import Template
import fitz

def initialize():
	pdfs = get_files()
	pdf_name = ""
	current_file_group = []
   	
	pdf_name = set_name(pdfs)
	current_file_group.append(pdfs[0])

	for current_pdf in pdfs:
		current_index = pdfs.index(current_pdf)
		next_index = current_index + 1
    
		if next_index >= len(pdfs): 
			print(Template("Merging the following files: ${files}").substitute(files = current_file_group))
			
			merge_pdfs(current_file_group, pdf_name)
			
			break

		next_pdf = pdfs[next_index]

		if next_pdf.startswith(pdf_name):
			current_file_group.append(next_pdf)
		else:	
			print(Template("Merging the following files: ${files}").substitute(files = current_file_group))

			merge_pdfs(current_file_group, pdf_name)

			current_file_group = []
			current_file_group.append(next_pdf)

			pdf_name = set_name(current_file_group)

def get_files():
	files = []
	pdfs = []

	for (dirpath, dirnames, filenames) in walk("./"):
		files.extend(filenames)

		break

	for current_file in files:
		if current_file.endswith(".pdf"):
			pdfs.append(current_file)

	if len(pdfs) == 0:
		print("There are no PDF files to process in the current directory. Operation finished")

		exit()

	pdfs.sort(key=lambda x: x.replace(".pdf", ""))
	return pdfs

def set_name(files):
	return files[0].replace(".pdf", "")

def merge_pdfs(files, pdf_name):
	result = fitz.open()
		
	for pdf in files:
		with fitz.open(pdf) as mfile:
			result.insert_pdf(mfile)

	result.save(Template("./results/${name}.pdf").substitute(name = pdf_name)) 				

initialize()
