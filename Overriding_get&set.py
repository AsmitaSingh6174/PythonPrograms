class myList:
    def __init__(self,List):
        self.List=List
    def __getitem__(self,index):
        return self.List[index]
    def __setitem__(self,index,num):
        self.List[index]=num
    def __len__(self):
         return len(self.List)
    def display(self):
        print(self.List)
L = myList([1,2,3,4,5,6,7])
print("List is:")
L.display()
index=int(input("Enter the index of the list you want to access : "))
print(L[index])
index=int(input("Enter the index at which you want to modify : "))
num=int(input("Enter the correct number : "))
L[index]=num
L.display()
print("Length of the list ",L.len(L))