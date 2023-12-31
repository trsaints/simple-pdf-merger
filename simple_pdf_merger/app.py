class App():
	def __init__(self):
		self.title = ""
		self.origin_path = ""
		self.destination_path = "" 

	def set_path(self, target, path):	
		if target == "origin":
			self.origin_path = path
		elif target == "destination":
			self.destination_path = path
		else: raise Exception("No path name selected")
	
	def set_title(self, title):
		if len(title) < 1: raise Exception("No title was defined")

		self.title = title	
