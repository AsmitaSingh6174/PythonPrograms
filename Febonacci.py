def febonacci(n):
    if(n<2):
        return 1
    else:
        return(febonacci(n-1)+febonacci(n-2))
n=int(input("Enter a Number of terms : "))
for i in range(n):
    print("Febonacci(",i,")=",febonacci(i))

# Function to print Fibonacci series
def fibonacci_series(n):
    a = 0
    b = 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=' ')
        temp = a
        a = b
        b = temp + b
terms = int(input("Enter the number of terms: "))
fibonacci_series(terms)
