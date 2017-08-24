#DEFINE_TYPE_CODE#py
#sDEFINE_TYPE_CODE#py
# -*- coding: utf-8 -*-

def main():
	nameFile = raw_input('Name file :')
	nameFileNoExt = nameFile.split('.')[0]
	newF = None
	fileClosed = True
	totNewFile = 0
	pathNewFiles = []
	pathNewFile = None
	nameNewFile = None
	with open(nameFile, 'r') as f:
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
					pathNewFile = str(define[define.index(word)+2]) + nameNewFile
				if word == 'DEFINE_NAME_FILE_TYPE_CODE' and len(define) >= define.index(word)+2:
					nameCode = '.' + str(define[define.index(word)+1])
					nameNewFile = str(define[define.index(word)+2]) + nameCode
				if word == 'DEFINE_TYPE_CODE' and len(define) > define.index(word):
					if pathNewFile == None:
						if nameNewFile == None:
							nameCode = '.' + str(define[define.index(word)+1])
							nameNewFile = nameFileNoExt + nameCode
						pathNewFile = nameNewFile
					newF = open(pathNewFile, 'w')
					totNewFile += 1
					pathNewFiles.append(pathNewFile)
					fileClosed = False
					firstLine = True
				if word == 'END_DEFINE_TYPE_CODE' and len(define) > define.index(word):
					if not fileClosed:
						newF.close()
						nameCode = None
						fileClosed = True
						pathNewFile = None
						nameNewFile = None
			if newF != None and not fileClosed:
				if not firstLine:
					newF.write(line)
				else:
					firstLine = False
		print('New files :', totNewFile)
		for pathNewFile in pathNewFiles:
			print(pathNewFile)
main()
#sEND_DEFINE_TYPE_CODE#py
#END_DEFINE_TYPE_CODE#py
