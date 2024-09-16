menu = {
    'pizza':150,
    'pasta':50,
    'burger':60,
    'salad':40,
    'coffee':90,
    'chai':20,
    'ice-cream':70,
}
print("welcome to RAO Restaurant")
print("Pizza: Rs150\nPasta: Rs50\nBurger:Rs60\nSalad: Rs40\nCoffee: Rs90\nChai:Rs20\nIce-cream: Rs70\n")

order_total = 0

item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print("Ordered item {item_1} is not available yet!")
    
another_order = input("Do you want to add another item? (yes/no)=")
if another_order == "yes":
   item_2 = input ("Enter the name of second item=")
   if item_2 in menu:
       order_total +=  menu[item_2]
       print(f"Item {item_2} had been added to order")
   else:
       print(f"Ordered item {item_2} is not avialable!")
       
print(f"The total amount of item to pay is : Rs {order_total}")
