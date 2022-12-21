# class ShoppingCart():
#     '''ShoppingCart will have items as an attribute
#         -items: expected to be a list
#     '''
#     def __init__(self, items):
#         self.items = items

#     def showShoppingCart(self):
#             print("Here are the items in your cart!")
#             for item in self.items:
#                 print(item)
    
#     def addToCart(self):
#         new_item = input('What would you like to add?: ')
#         self.items.append(new_item)

#     def removeFromCart(self):
#         print(self.items)
#         remove_item = input('What item would you like to remove?: ')
#         self.items.remove(remove_item)

# my_cart = ShoppingCart([])

# def run():
#     while True:
#         response = input('What would you like to do with your shopping cart: add/remove/show/quit ')

#         if response.lower() == 'quit':
#             my_cart.showShoppingCart()
#             print('Please proceed to checkout!')
#             break
#         elif response.lower() == 'show':
#             my_cart.showShoppingCart()
#         elif response.lower() == 'add':
#             my_cart.addToCart()
#         elif response.lower() == 'remove':
#             my_cart.removeFromCart()
#         else:
#             print('Try a different command')

# run()


# class StringFun():
#     def get_String(self):
#         self.inputstring = input('Gimme a string: ')
    
#     def print_String(self):
#         print(f'Here is your wonderful string: {self.inputstring}')

# my_string = StringFun()

# def run():
#     my_string.get_String()
#     my_string.print_String()

# run()