#!/usr/bin/python3
import sys

try:
   # open file stream
   file = open("tmp.txt", "w")

except IOError:
   print ("There was an error writing to", file_name)
   sys.exit()

file_finish = "tmp_file_finish.txt"
print ("Enter", file_finish, end=" ")
print ("When finished")
file_text = input("Enter text: ")
while file_text != file_finish:
   file_text = input("Enter text: ")
   if file_text == file_finish:
      # close the file
      file.close()
      break
   file.write(file_text)
   file.write("\n")
file.close()
file_name = input("Enter filename: ")
if len(file_name) == 0:
   print ("Next time please enter something")
   sys.exit()

try:
   file = open(file_name, "r")

except IOError:
   print ("There was an error reading file")
   sys.exit()
file_text = file.read()
file.close()
print (file_text)
