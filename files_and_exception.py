'''with open ('new.txt')as file:
    contents=file.read()
    print(contents.rstrip())'''

fname='new.jpg'

with open (fname)as kd:
 
   for line in kd:
      line = kd.readlines()
      print(line)