class ABC:
    var=10      #Class Variable
    def display(self):
        print("In Class Method")
obj=ABC()
print(obj.var)
obj.display()


