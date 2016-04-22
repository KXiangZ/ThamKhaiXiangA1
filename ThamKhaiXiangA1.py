"""
Tham Khai Xiang 14/4/2016
This is a program taht allow for hiring or returning multiple item.
github link:https://github.com/KXiangZ/ThamKhaiXiangA1
"""

def load_item():
    show = ''
    counter = 0
    input_file = open('inventory.csv', 'r+')
    for data in input_file:
        storage = data.split(',')
        storage[-1] = storage[-1].strip()
        if storage[3] == "in":
            storage[3] = ""
        elif storage[3] == "out":
            storage[3] = "*"
        show+=("{:3} - {}({}){:20}= $ {:.2f} {}\n ".format(counter,storage[0],storage[1],"",float(storage[2]),storage[3]))
        counter+=1
    return (show)
    input_file.close()

def hire_item():
    show=""
    counter = 0
    record = ""
    hiring=""
    input_file = open('inventory.csv', 'r+')
    for data in input_file:
        storage = data.split(',')
        storage[-1] = storage[-1].strip()
        if storage[3] == "in":
            storage[3] = ""
        elif storage[3] == "out":
            storage[3] = "*"
        if storage[3]=="":
            show += ("{:3} - {}({}){:30}= $ {:.2f} \n ".format(counter, storage[0], storage[1],"", float(storage[2])))
            if record=="":
                record+=str(counter)
            else:
                record+=","+str(counter)
        counter+=1
    input_file.close()
    print(show)
    while hiring=="":
        try:
            hiring =int((input("Enter the number of an item to hire\n")))
        except(ValueError):
            print("Invalid item number")
    for i in record.split(','):
        if hiring == int(i):
            num=0
            hired=""
            input_file = open('inventory.csv', 'r+')
            for data in input_file:
                storage = data.split(',')
                storage[-1] = storage[-1].strip()
                if num ==hiring:
                    hired=("{} hired for ${:.2f}".format(storage[0], float(storage[2])))
                num+=1

            print(hired)
            input_file.close()
    input_file = open('inventory.csv', 'r+')
    count=0
    store=""
    for data in input_file:
        if count== hiring:
            storage=data.split(',')
            store+=("{},{},{},out\n".format(storage[0],storage[1],storage[2]))
            count+=1
        else:
            store+=data
            count+=1
    input_file.close()
    input_file=open("inventory.csv","w")
    input_file.write(store)
    input_file.close()

def return_item():
    show = ""
    counter = 0
    record = ""
    reitem=""
    input_file = open('inventory.csv', 'r+')
    for data in input_file:
        storage = data.split(',')
        storage[-1] = storage[-1].strip()
        if storage[3] == "in":
            storage[3] = ""
        elif storage[3] == "out":
            storage[3] = "*"
        if storage[3] == "*":
            show += ("{:3} - {}({}){:30}= $ {:.2f} \n ".format(counter, storage[0], storage[1],"", float(storage[2])))
            if record == "":
                record += str(counter)
            else:
                record += "," + str(counter)
        counter += 1
    input_file.close()
    print(show)
    while reitem == "":
        try:
            reitem = int(input("Enter the number of an item to return\n"))
        except(ValueError):
            print("Invalid item number")

    for i in record.split(','):
        if reitem == int(i):
            num = 0
            ret = ""
            input_file = open('inventory.csv', 'r+')
            for data in input_file:
                storage = data.split(',')
                storage[-1] = storage[-1].strip()
                if num == reitem:
                    ret = ("{} returned".format(storage[0]))
                num += 1
            print(ret)
            input_file.close()
    input_file = open('inventory.csv', 'r+')
    count = 0
    store = ""
    for data in input_file:
        if count == reitem:
            storage = data.split(',')
            store += ("{},{},{},in\n".format(storage[0], storage[1], storage[2]))
            count += 1
        else:
            store += data
            count += 1
    input_file.close()
    input_file = open('inventory.csv', 'w')
    input_file.write(store)
    input_file.close()

def add_item():
    name_input=input("Item name: ")
    description_input=input("Description: ")
    price_input=input("Price per day: $")
    input_file = open('inventory.csv', 'a+')
    input_file.write("\n{},{},{},in".format(name_input,description_input,price_input))
    print("{}({}),${} now available for hire".format(name_input,description_input,price_input))
    input_file.close()

input_file=open('inventory.csv','r+')
counter=0
for data in input_file:
    counter+=1

#Welcome message
print("""Items for Hire - by Tham Khai Xiang
{} items loaded from items.csv""".format(str(counter)))
user_input=input("""Menu:
(L)ist all items
(H)ire an item
(R)eturn an item
(A)dd new item to stock
(Q)uit\n""").lower()
while True:
    while user_input=="l" or user_input=="h" or user_input=="r" or user_input=="a" or user_input=="q":
        if user_input=="l":
            print(load_item())
            user_input = input("""Menu:
(L)ist all items
(H)ire an item
(R)eturn an item
(A)dd new item to stock
(Q)uit\n""").lower()
        elif user_input=="h":
            print(hire_item())
            user_input = input("""Menu:
(L)ist all items
(H)ire an item
(R)eturn an item
(A)dd new item to stock
(Q)uit\n""").lower()
        elif user_input=="r":
            print(return_item())
            user_input = input("""Menu:
(L)ist all items
(H)ire an item
(R)eturn an item
(A)dd new item to stock
(Q)uit\n""").lower()
        elif user_input=="a":
            print(add_item())
            user_input = input("""Menu:
(L)ist all items
(H)ire an item
(R)eturn an item
(A)dd new item to stock
(Q)uit\n""").lower()
        elif user_input=="q":
            quit()

    while user_input!="l" and user_input!="h" and user_input!="r" and user_input!="a" and user_input!="q":
        print("Invalid menu choice")
        user_input = input("""Menu:
(L)ist all items
(H)ire an item
(R)eturn an item
(A)dd new item to stock
(Q)uit\n""").lower()