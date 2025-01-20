a = int(input("enter a number :- "))
b = int(input("enter 2nd numbert :- "))
print("\t\t1. addition\n\t\t2. subtraction\n\t\t3. Multiply\n\\t\t4. division\n\t\t5. floor division\n\t\t6. power")
choice = int(input("Enter choice : "))
if(choice == 1):
    c = a+b
    print("Sum : ",c)
elif(choice == 2):
    d = a-b
    print("Difference : ",d)
elif(choice == 3):
    e = a*b
    print("Multiplication : ",e)
elif(choice == 4):
    f = a/b
    print("Division : ",f)
elif(choice == 5):
    g = a//b
    print("Floor division: ",g)
elif(choice==6):
    i = a**b
    print("Power a^b : ",i)
else:
    print("Invalid choice!!")
