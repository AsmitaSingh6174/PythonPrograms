#Random Number : Python does not have a random function to random number, but it has built-in
#module called random
import random as ra
print(ra.randrange(1,100))
print(ra.randint(1,100))
print(ra.uniform(20,60))
print(ra.triangular(20,60,30))

#shuffle a list 1 
mylist = ["Apple","Banana","Cherry"]
# ra.shuffle(mylist)
print(mylist)
print(ra.choice(mylist)) #Randomly select an item from the list
print(ra.choices(mylist,weights=[10,1,1],k=5))



