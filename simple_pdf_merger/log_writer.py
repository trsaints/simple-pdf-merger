def open_log(file):
	try:
		return open(file, "w", encoding = "utf-8")
	except:
		print(sys.exception())

def write_log(log, content):
	log.write(content)

