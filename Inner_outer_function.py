def outer_fun():
    outer_var=10
    def inner_fun():
        inner_var=20
        print("Outer Variable : ",outer_var)
        print("Inner Variable : ",inner_var)
    inner_fun()
    print("Outer Variable : ",outer_var)
  #  print("Inner Variable : ",inner_var)
outer_fun()              #function call  
