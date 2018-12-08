from random import randint
to_sort=[]
unsorted=1
for i in range(0,50):
    to_sort.append(randint(0,1000))
while unsorted:
    iteration=0
    for i in range(1,50):
        if to_sort[i] < to_sort[i-1]:
            x=to_sort[i]
            to_sort[i]=to_sort[i-1]
            to_sort[i-1]=x
        else:
            iteration+=1
    if iteration==len(to_sort)-1:
        unsorted=0

print(to_sort)
