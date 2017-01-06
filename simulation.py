from os import listdir
from os.path import isfile, join

ignoreList = [".DS_Store", "log.lammps"]
class Simulation:
        def __init__(self, objectId, inputScript, folder, name, description, tags, thumbnails = None, files = None):
                self.objectId = objectId
		self.inputScript = inputScript
		self.folder = folder
		self.files = files
                self.name = name
		self.description = description
		self.tags = tags
		self.thumbnails = thumbnails
                print self.objectId
		print "Files now: ", self.files
		if self.thumbnails is None:
			self.thumbnails = []
		if self.files is None:
			self.files = []
			self.findFiles()
		

	def findFiles(self):
		print "Finding files for folder: ", self.folder
		for f in listdir(self.folder):
			if isfile(join(self.folder, f)):
				print "Checking files: ", f
				if f in ignoreList: continue
				if f.lower().endswith(('.png', '.jpg', '.jpeg')):
					self.thumbnails.append(f)
				self.files.append(f)
