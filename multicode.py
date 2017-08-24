#DEFINE_TYPE_CODE#py
#sDEFINE_TYPE_CODE#py
# -*- coding: utf-8 -*-

def main():
	fullPathFile = raw_input("File's path :")
	pathFileNoExt = fullPathFile.split('.')[0]
	nameFileNoExt = pathFileNoExt.split('\\')[-1]
	pathFile = '/'.join(pathFileNoExt.split('\\')[:-1]) + '/'
	if pathFile == []:
		pathFile = '/'.join(pathFileNoExt.split('/')[:-1]) + '/'
		nameFileNoExt = pahtFileNoExt.split('/')[-1]
	newF = None
	fileClosed = True
	totNewFile = 0
	fullPathNewFiles = []
	pathNewFile = pathFile
	nameNewFile = None
	fullPathNewFile = None
	with open(fullPathFile, 'r') as f:
		for line in f:
			define = line.split('#')
			if fileClosed:
				last_word = define[-1]
				last_word = last_word.split('\n')
				del define[-1]
				define += last_word
			for word in define:
				if word == 'DEFINE_PATH_TYPE_CODE' and len(define) >= define.index(word)+2:
					if nameNewFile == None:
						nameCode = '.' + str(define[define.index(word)+1])
						nameNewFile = nameFileNoExt + nameCode
					pathNewFile = str(define[define.index(word)+2])
					fullPathNewFile = pathNewFile + nameNewFile
				if word == 'DEFINE_NAME_FILE_TYPE_CODE' and len(define) >= define.index(word)+2:
					nameCode = '.' + str(define[define.index(word)+1])
					nameNewFile = str(define[define.index(word)+2]) + nameCode
					fullPathNewFile = pathNewFile + nameNewFile
				if word == 'DEFINE_TYPE_CODE' and len(define) > define.index(word):
					if fullPathNewFile == None:
						if nameNewFile == None:
							nameCode = '.' + str(define[define.index(word)+1])
							nameNewFile = nameFileNoExt + nameCode
							pathNewFile = pathFile
						fullPathNewFile = pathNewFile + nameNewFile
					newF = open(fullPathNewFile, 'w')
					totNewFile += 1
					fullPathNewFiles.append(fullPathNewFile)
					fileClosed = False
					firstLine = True
				if word == 'END_DEFINE_TYPE_CODE' and len(define) > define.index(word):
					if not fileClosed:
						newF.close()
						nameCode = None
						fileClosed = True
						pathNewFile = pathFile
						nameNewFile = None
						fullPathNewFile = None
			if newF != None and not fileClosed:
				if not firstLine:
					newF.write(line)
				else:
					firstLine = False
		print('New files :', totNewFile)
		for fullPathNewFile in fullPathNewFiles:
			print(fullPathNewFile)
main()
#sEND_DEFINE_TYPE_CODE#py
#END_DEFINE_TYPE_CODE#py
