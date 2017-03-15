text = '\nsample text to save\nNew Line!'

saveFile = open('exampleFile.txt', 'a')

saveFile.write(text)

saveFile.close()