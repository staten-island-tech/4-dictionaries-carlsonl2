Store = [
{
    "Name" : "Airpods",
    "Price" : 199.99,
    "Store" : "Apple"
},

{   
    "Name" : "IPad",
    "Price" : 799.99,
    "Store" : "Apple"
    
},

{
    "Name" : "IPhone",
    "Price" : 1199.99,
    "Store" : "Apple"
},
        ]


print("Welcome to the Store!")
for index, item in enumerate(Store):
   print(f"{index} : {item['Name']}, ${item['Price']}, {item['Store']}")



    #the f string allows the code to output multiple values in a dictionary of a list of dictionaries
'''x = index + 1
for i in range(x):
   print(f"{Store[i]['Name']}")'''
done = False 
subtotal = 0
tax = 1.08875

cart = []

while done == False:
    choose = input("Would you like to buy anything? If so, put the number of the item you would like to purchase.")
    x = index + 1
    for item in range(x):
        if choose == Store[item]['Name']:
            cart.append(choose)
            subtotal = subtotal + Store[item]['Price']
            print(f"here are the items you purchased {cart}")
            
                  
    KeepShopping = input("Would you like to keep shopping? (Yes/No)")
            
    if KeepShopping == "No":
        total = subtotal * tax
        done = True
        print(f"Here are all of the titems that you have bought. {cart}")
        print(f"${round(total, 2)}")
              
                
        
        
        
        


           
    



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
        
