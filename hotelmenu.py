#Define the menu item in hotel

menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80
}

#Greet
print('welcome to Python Restaurant')
print("pizza: RS40\npasta: RS50\nburger: RS60\nsalad: Rs70\ncoffee: Rs80")

order_total = 0

item1 = input('Enter the name of item you went to order =')

if item1 in menu:
    order_total += menu[item1]
    print(f'your item {item1} has been addad to your order')

else:
    print(f'ordered item {item1} is not avaialable')

another_order = input('do you want to add another item? (yes/no)')

if another_order == 'yes':
    item2 = input('Enter the name of second item you went to order =')
    if item2 in menu:
        order_total += menu[item2]
        print(f'your item {item2} has been addad to your order')

    else:
        print(f'ordered item {item2} is not avaialable')

print(f'Total amount of item to pay is {order_total}')