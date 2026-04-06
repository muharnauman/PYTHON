filename = 'new.py'
with open(filename) as file_object:
 lines = file_object.readlines()

pi_string = ''
for line in lines:
 pi_string += line.strip()
 if "k" in pi_string[:100]:
  
 #print(pi_string[:100] + "...")
  print(len(pi_string))
  print("nauman")
  print(line)

 