def write_log(file, content):
	with open(file, 'w', encoding="utf-8") as log_file:
		log_file.write(content)

