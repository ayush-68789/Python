# Create a program that will keep track of items for a shopping list. 
#The program should keep asking for new items until nothing is entered 
#(no input followed by enter/return key). The program should then display the full shopping list.



shop = []
while True :
    item = input("ENTER ITEM")
    if item :
        shop.append(item)
    else:
        break
    
print("<<< SHOPPING LIST >>>")
for i in range(0,len(shop)) : 
    print("\t",shop[i])
