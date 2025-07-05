#A Menu driven Program that keeps record of books and jounral
class Book:
    def __init__(self):                                       #Constructor of class Book
        self.title = " "
        self.author = " "
        self.price = 0

    def read(self):                                               #class method function
        print("\n📚 Enter Book Details")
        self.title = input("🔸 Title  : ")
        self.author = input("🔸 Author : ")
        self.price = float(input("Enter book Price :  "))
        
    def display(self):                                          
        print("────────────────────────────────────")
        print("📖 Title  : ",self.title)
        print("✍  Author : ",self.author)
        print("💰 Price  : ₹",self.price)
        print("────────────────────────────────────\n")


my_books = []                         #List 
print("\n📚📘 Welcome to the Library Management System 📘📚")
ch='y'
while(ch == 'y'):
    print('''
          1. Add new Book
          2. Display Books
          ''')
    choice = int(input("Enter a Choice : "))
    if(choice==1):
        book = Book()                                                #book is object and Book is class
        book.read()
        my_books.append(book)                             #append : Add new values and don't replace the previous values
    elif(choice==2):
        for i in my_books:
            i.display()
    else:
        print("Invalid Choice")
    ch=input("Do you want to Continue...")
print("Bye !!")

        
