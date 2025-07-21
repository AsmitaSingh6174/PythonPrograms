#To calculate the bill amount for an give =n quantity,sold,value,discount and tax

Quantity=float(input("Enter The Quantity Of Items Sold : \t"))
Value=float(input("Enter Product Value : \t"))
Discount=float(input("Enter the discount percent : \t"))
tax=float(input("Enter Tax : \t"))
ttl_amount= Quantity*Value
Dis_amount=(ttl_amount*Discount)/100
Bill_amount=ttl_amount-Dis_amount
tax_amount=(Bill_amount*tax)/100
Total=ttl_amount+tax_amount
print("----- Bill -----")
print("Quantity Sold |\t",Quantity)
print("Price Per Item |\t",Value)
print("\n \t \t _______________")
print("Total Amount |\t",ttl_amount)
print("Discount |\t",Discount)
print("\n \t \t _______________")
print("Discount Amount |\t",Bill_amount)
print("Tax |\t",tax_amount)
print("\n \t \t _______________")
print("Total Amount To be Paid |\t",Total)
