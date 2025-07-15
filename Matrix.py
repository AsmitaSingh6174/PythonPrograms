class Matrix:
    def __init__(self,List):                                                 #__init__() Initialize the Matrix
        self.List=List
    def display(self):
        print(self.List)            
    def __add__(self,M):                     
        Temp=Matrix([ ])                                
        for i in range (len(self.List)):                                    #Length (self.list) for number of rows = 2
            for j in range (len(self.List[0])):                          #Length (self.list[0]) for number of columns =2
                Temp.List.append(self.List[i][j]+M.List[i][j])
        return Temp
M1=Matrix([[1,2],[3,4]])
M2=Matrix([[3,4],[5,6]])
M3=Matrix([ ])
M3=M1+M2
print("Resultant Matrix")
M3.display()
