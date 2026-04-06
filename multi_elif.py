prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
var=True
while  True:
    massage=input(prompt)
    if massage=="quit":
     #print("game is over")
     
     var=False

    elif massage=="nauman":
        print("user")
        
    else:
        print("wrong")
        #continue
    if var==False:
        exit    



 