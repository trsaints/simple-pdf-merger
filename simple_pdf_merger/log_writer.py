def open_log(file_path):
	try:
		return open(file_path, "w", encoding = "utf-8")
	except Exception as e:
		print(e.with_traceback())

def write_log(log, content):
	log.write(f"{content}\n")

