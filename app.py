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

def late(x,y):
    students = y
    waiting = 0 
    next = y + students
    while next < 999:
        for i in (6): 
            if x[i] == "take":
                students == students + 1 and waiting == waiting + 1
            elif x[i] == "serve":
                waiting == waiting - 1
            elif x[i] == "close":
                print(f"{students, waiting, next}")
late(["take", "take", "serve", "take", "serve", "serve"], 23)

