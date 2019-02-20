#Activity 11. Writting a programm that reads 'mynotes' file and add some information in the end of the mynotes.txt file

#For the first part we can use the same as on the previous exercise:
NAME = 'mynotes'
myfile = open(NAME, 'r')

print("File opened: {}".format(myfile))

#Now the file is opened.
#Let´s read it:

file_contents = myfile.read()
print("File contents: {}".format(file_contents))
print("This is the end")

#We must close the file after reading it.
myfile.close()

#Now we must open it again but in an other way so that e¡we can edit ( add content) the file.
myfile1 = open(NAME, 'a')
myfile1.write("Hey, this is just what I want to add to my notes.\n")
myfile1.close()
print("End.")
