#Lambda Function: It is a small anonymous function
#It can take any number of arguments , but can only have one expression.
#Syntax : Lambda Agruments : expression

#Add 10 number in the given argument 'a' and return the result
x= lambda a:a + 10
print(x(5))

#Add 10 number in given arguments 'a' and 'b' and return the result
x= lambda a,b:a*b
print(x(2,4))

'''Why use lambda function :the power of the lambda function is better shown when use then as a
anonymous function inside another function'''
def uselambda_fun(n):
    return lambda a:a*n
fun=uselambda_fun(10)#n is 10
print(fun(5))


def uselambda(n):
    return lambda a:a*n
double=uselambda(2)#n is 10
triple=uselambda(3)
print(double(5))
print(triple(5)) 



