a = ["amala","akshaya","arya","roshna"]
count=0
for x in a:
    j=x
    for x in range(0,len(j)):
        if(j[x]=="a"):
            count=count+1
            
print("count of occurrences of a :"+str(count))