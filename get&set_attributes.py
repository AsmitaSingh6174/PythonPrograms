class Numbers:
    def __init__(self,myList):
        self.myList = myList
    def __getitem__(self,index):                              #get the value of a index
        return self.myList[index]
    def __setitem__(self,index,val):
        self.myList[index] = val
NumList = Numbers([1,2,3,4,5,6,7,8,9,10])
print(NumList.myList)
print(NumList[5])
NumList[3] = 10
print(NumList.myList)

        
