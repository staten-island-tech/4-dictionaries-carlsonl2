Store = [{
    "Name" : "Airpods",
    "Price" : 199.99,
    "Store" : "Apple"
},

{
    "Name" : "IPhone",
    "Price" : 1199.99,
    "Store" : "Apple"
},

{
    "Name" : "IPad",
    "Price" : 799.99,
    "Store" : "Apple"
}]


print("Welcome to the Store!")
for index, item in enumerate(Store):
   print(f"{index} : {item['Name']}, ${item['Price']}, {item['Store']}")



    #the f string allows the code to output multiple values in a dictionary of a list of dictionaries
cart = []
subtotal = 0
done = False

while done == False:
    choose = input("What would you like to buy?")
    for item in range(Store):
        if choose == Store[item]["Name"]:
            cart.append(Store[item]["Name"])
            subtotal = subtotal + Store[item]['Price']
    print(cart)
    



'''def late(x, y):
    late = 0
    waiting = 0
    for i in range(7):
        if y[i] == "take":
            waiting = waiting + 1
            late = late + 1
        elif y[i] == "serve":
            waiting = waiting - 1
        elif y[i] == "close":
            nextnumber = x + late
            print(late, waiting, nextnumber)
late(23, ["take", "take", "serve", "take", "serve", "serve", "close"])'''
        
