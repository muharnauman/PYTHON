#his function use cheack the file is avilible or not
def file_cheacker(fname):    
    try:
        with open(fname ) as opner :
          op=opner.write()
         
    except:
        print("file not found") 
    else:
        print(len(op)  )  
fname=['new.txt','new.py']
for fnames in fname:
  file_cheacker(fnames)