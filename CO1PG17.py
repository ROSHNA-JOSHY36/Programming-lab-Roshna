y={'a':10,'b':4,'c':6,'d':7,'e':8,'f':9}
print("Dictionary:",y)
l=list(y.items())
l.sort()
print('Descending order is',l)
l=list(y.items())
l.sort(reverse=True)
print('Descending order is',l)