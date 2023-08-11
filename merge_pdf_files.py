from os import walk
import fitz

def merge_pdfs():
	files = []
	pdfs = []
	pdf_name = ""
	current_file_group = []

	for (dirpath, dirnames, filenames) in walk("./"):
		files.extend(filenames)
		break

	for current_file in files:
		if current_file.endswith(".pdf"):
			pdfs.append(current_file)

	if len(pdfs) == 0:
		return
   
	pdfs.sort(key=lambda x: x.replace(".pdf", ""))
	
	pdf_name = pdfs[0].replace(".pdf", "")
	current_file_group.append(pdfs[0])

	for current_pdf in pdfs:
		current_index = pdfs.index(current_pdf)
		next_index = current_index + 1
    
		if next_index >= len(pdfs):
			break

		next_pdf = pdfs[next_index]

		if next_pdf.startswith(pdf_name):
			current_file_group.append(next_pdf)
		else:
			current_file_group = []
			current_file_group.append(next_pdf)
			pdf_name = next_pdf.replace(".pdf", "")
	
		print(current_file_group)

	print(pdfs)

merge_pdfs()
