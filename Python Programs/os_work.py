import os
import time
curDir = os.getcwd()
os.rmdir('newDir2')
os.mkdir('newDir')


time.sleep(5)


os.rename('newDir', 'newDir2')

print(curDir)

print('This was helpful')
