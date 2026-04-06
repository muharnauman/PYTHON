class cars():
    def __init__(self,name,color,model,ma):
            self.name=name
            self.color=color
            self.model=model
            self.ma=ma
    def input(self):            
              self.name1= str (input("   enter you wants to update name then press \'N\' "))
              if self.name1.capitalize()=="N": 
                 self.name=input("enter the name")
              self.color1= str (input("   enter you wants to update color then press \'C\' "))
              if self.color1.capitalize()=="N": 
                 self.color=input("enter the color")     
              self.model1= str (input("   enter you wants to update model then press \'M\' ")) 
              if self.model1.capitalize()=="N":    
                 self.model=input("enter the  model ")                               
    def geting_values(self):
            long_list=self.name+"   "+self.color+"     "  
            print (long_list.title(),self.model)
    #def update(self) :
object=cars("new","blasck",2023,"nauma")
old=input("enter for old value")
if old.capitalize()=="O":
        object.geting_values()
update=input("enter for further steps") 
if update.capitalize()=="U":       
 testing_update =input("enter     \"yes\" if you wants to update")
 
 if testing_update.capitalize()=="YES":
         
  object.input()
 
 else:
         print("YOU GOT OLD ONE") 
 testing_output=input("enter \' yes \' for cheaking over all ")
 if testing_output.capitalize()=="QUALITIES":
  object.geting_values()
