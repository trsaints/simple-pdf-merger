from datetime import datetime

def open_log(file):
	try:
		return open(file, "w", encoding = "utf-8")
	except:
		print(sys.exception())

def write_log(log, content):
	current_date = datetime.today()
	formatted_date = current_date.strftime("[%d/%m/%Y - %H:%M:%S]")
	log.write(f"{formatted_date} {content}\n")

