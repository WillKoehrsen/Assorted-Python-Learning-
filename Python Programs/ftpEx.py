from ftplib import FTP


ftp = FTP('domainname.com')
ftp.login(user='username', password='password')

# Current working directory
ftp.cwd('/specificdomain-or-location/')

# send or recieve a file
# grabbing a file from the remote server

def grabFile():
	# specify the name of the file
	filename = 'filename.txt'
	# local file on computer
	localfile = open(filename,'wb' )
	# retrieve the file and then specify what to do to the local file, buffer : how fast to transfer the information
	ftp.retrbinary('RETR' + filename, localfile.write, 1024)

	ftp.quit()

	# close the file
	locafile.close()


def placeFile():
	filename = 'fileName.txt'
	# stor in binary, rb: read binary
	ftp.storbinary('STOR' + filename, open(filename,'rb'))

	ftp.quit()