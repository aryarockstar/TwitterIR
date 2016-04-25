fp = open('javascript1')
f = open('new3.html','w')
for line in fp:
	print line
	if  len( line.strip() ) != 0:
		#f.write( line )
		f.write( 'print ' + '"' )
		for char in line[0:len(line) - 1]:
			if char == '"':
				f.write('\\')
			f.write(char)
		f.write('"' + '\n')


f.close()
f = open("new3.html", 'r')
for line in f:
	print line
