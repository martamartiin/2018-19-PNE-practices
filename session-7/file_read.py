# Activity 8. A program for reading 'mynotes' file.

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
