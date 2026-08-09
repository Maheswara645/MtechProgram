t1=(1,2,3)
t2=("apple","banana","figs")

t3=list(t2)
t3.append('lemon')
print("List",t3)
t2 = tuple(t3)
print("Tuple",t2)