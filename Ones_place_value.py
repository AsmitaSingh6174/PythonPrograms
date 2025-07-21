#Program to print a digit at one's place
num=int(input("Enter A Number"))
ones_place_value=num%10
print("The Value At One's Place is : \t",+ones_place_value)

# or

num=int(input("Enter A Number"))
ones_place_value=str(num%10)
print("The Value At One's Place is : \t"+ones_place_value)
