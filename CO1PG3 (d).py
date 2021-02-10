myinput=input("Message : ")

mylist =list(myinput) 

for character in mylist:
    mylist[character]+=ord(mylist[character])+1
print(character)