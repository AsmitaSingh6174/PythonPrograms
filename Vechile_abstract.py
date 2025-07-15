''' Write an abstract class vechiles derived three classes Car , Motorcycle and Truck from it. Define appropriate
    Methods and print the details of the methods.'''
class Vechiles():
    def Name():
        raise NotImplementedError()
    def color():
        raise NotImplementedError()
    def Model():
        raise NotImplementedError()
    def Company():
        raise NotImplementedError()
    def display():
        raise NotImplementedError()
    
class Car(Vechiles):
    def Name(self):
        return "Sedan"
    def Color(self):
        return "Red"
    def Model(self):
        return "Civic"
    def Company(self):
        return "Honda"
    def display(self):
        print("_____________________Car Details_____________________")
        print("Name:", self.Name())
        print("Color:", self.Color())
        print("Model:", self.Model())
        print("Company:", self.Company())
        print()

class Motorcycle(Vechiles):
    def Name(self):
        return "Sport Bike"
    def Color(self):
        return "Black"
    def Model(self):
        return "R15"
    def Company(self):
        return "Yamaha"
    def display(self):
        print("_____________________Motorcycle Details_____________________")
        print("Name:", self.Name())
        print("Color:", self.Color())
        print("Model:", self.Model())
        print("Company:", self.Company())
        print()

class Truck(Vechiles):
    def Name(self):
        return "Freightliner"
    def Color(self):
        return "Blue"
    def Model(self):
        return "Cascadia"

    def Company(self):
        return "Mercedes-Benz"

    def display(self):
        print("_____________________Truck Details_____________________")
        print("Name:", self.Name())
        print("Color:", self.Color())
        print("Model:", self.Model())
        print("Company:", self.Company())
        print()

c = Car()
m = Motorcycle()
t = Truck()

c.display()
m.display()
t.display()
