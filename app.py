'''Store = [{
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
    for item in Store:
        if choose == [item]['Name']:
            cart.append([item]['Name'])
            subtotal = subtotal + Store[item]['Price']
    print(f"{cart}")
    print(subtotal)'''

'''def late(y):
    waiting = 0 
    late = 0
    students = y + late
    set = ["take", "take", "serve", "take", "serve", "serve", "close"]
    while students < 999:
        for i in range(7): 
            if set[i] == "take":
                waiting == waiting + 1 and late == late + 1
            elif set[i] == "serve":
                waiting == waiting - 1
            elif set[i] == "close":
                print(f"{late, waiting, students}")
late(23)'''

'''set = ["take", "take", "serve", "take", "serve", "serve", "close"]
for i in range(6):
    print(set[i])'''

def late_students(x,y):
    waiting = 0
    late = 0
    while x < 999:
        for i in range(7):
            if y[i] == "take":
                waiting = waiting + 1 
                late = late + 1
            elif y[1] == "serve":
                waiting = waiting - 1
            elif y[i] == "close":
                nextnumber = x + late
                break
        print(f"{late, waiting, nextnumber}")
        
late_students(23, ["take", "take", "serve", "take", "serve", "serve", "close"])
