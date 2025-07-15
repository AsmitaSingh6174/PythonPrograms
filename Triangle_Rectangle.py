#WAP to find area of Polygon , triangle and rectangle using Abstract class.
class Polygon():
    def get_data():
        raise NotImplementedError()
    def area():
        raise NotImplementedError()
class Rectangle(Polygon):
    def get_data(self):
        self.length=int(input("Enter the Length of Rectangle : "))
        self.breath=int(input("Enter the Breath of Rectangle : "))
    def area(self):
        return(self.length*self.breath)
class Triangle(Polygon):
    def get_data(self):
        self.height=int(input("Enter the height of the Triangle : "))
        self.base=int(input("Enter the base of the Triangle : "))
    def area(self):
        return(0.5*self.height*self.base)
R=Rectangle()
R.get_data()
print(R.area())
T=Triangle()
T.get_data()
print(T.area())
