"""A company has a minimum and maximum limit of the quantity of
products to be ordered. Allow the user to order from the company product list ( create a list of any ten products).
Apply proper constraints if user orders more than the quantity available with the company.
Based on the quantity generate the customer bill"""
import time
obj = time.gmtime()
epoch = time.asctime(obj)
#print("Order date:", epoch)

list1 = ["Water", "Papaye", "Mangue", "Orange", "Banana", "Pomme", "Tomate", "Carotte", "Pastèque", "Ananas"]
Name = input("Enter your name: ")

print("Welcome! "+Name+"\nWhat do you wish?" )
Min_quan = 1
Max_quan = 100
print(list1)
Amount = 20
product = input("Enter product from the list: ")
if product in list1:
    """print("Available")"""
    quantity = int(input("Enter the quantity: "))
    if quantity in range(Min_quan,Max_quan):
        print("Available")
        """print("Your order has been received")"""
    else:
        print("Quantity out of range")
else:
    print("Sorry!! Product out of Stock")

print("\n")

def bill():
    print("Name: "+ Name)
    line = "="*2*len(Name)
    print(line)
    print("Product ordered: "+product)
    line1 = "="*4*len(product)
    print(line1)
    print("Quantity ordered: ",quantity)
    line2 = "="*10*2
    print(line2)
    print("Price: ",Amount)
    print(line2)
    print("Total Amount: ",Amount * quantity)
    print(line2)
    print("Order date:", epoch)
    print(line2)
bill()
#print(bill())