from os import listdir
from os.path import isfile, join

ignoreList = [".DS_Store", "log.lammps"]
class Simulation:
	def __init__(self, name, inputScript, folder, title, description, tags, thumbnails = [], files = []):
		self.name = name
		self.inputScript = inputScript
		self.folder = folder
		self.files = files
		self.title = title
		self.description = description
		self.tags = tags
		self.thumbnails = thumbnails
		if len(self.files) == 0:
			self.findFiles()

	def findFiles(self):
		for f in listdir(self.folder):
			if isfile(join(self.folder, f)):
				if f in ignoreList: continue
				if f.lower().endswith(('.png', '.jpg', '.jpeg')):
					self.thumbnails.append(f)
				self.files.append(f)
