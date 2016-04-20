"""
Tham Khai Xiang 14/4/2016
This is a program taht allow for hiring or returning multiple item.
github link:https://github.com/KXiangZ/ThamKhaiXiangA1
"""


#Welcome message
print('Items for Hire - by Tham Khai Xiang')



def load_item():
    show=''
    counter=0
    input_file = open('inventory.csv', 'r+')
    for data in input_file:
        storage = data.split(',')
        storage[-1] = storage[-1].strip()
        if storage[3]=="in":
            storage[3]=""
        elif storage[3]=="out":
            storage[3]="*"
        show+=("{} - {}({})\t\t\t\t= $ {:.2f} {}\n ".format(counter,storage[0],storage[1],float(storage[2]),storage[3]))
        counter+=1
    return (show)

    input_file.close()

def hire_item():
    show=""
    counter = 0
    record = ""
    input_file = open('inventory.csv', 'r+')
    for data in input_file:
        storage = data.split(',')
        storage[-1] = storage[-1].strip()
        if storage[3] == "in":
            storage[3] = ""
        elif storage[3] == "out":
            storage[3] = "*"
        if storage[3]=="":
            show += ("{} - {}({})\t\t\t\t= $ {:.2f} {}\n ".format(counter, storage[0], storage[1], float(storage[2]), storage[3]))
            if record=="":
                record+=str(counter)
            else:
                record+=","+str(counter)
        counter+=1
    input_file.close()
    print(show)
    hiring = (input("Enter the number of an item to hire\n"))
    for i in record.split(','):
        if hiring == i:
            num=0
            hired=""
            input_file = open('inventory.csv', 'r+')
            for data in input_file:
                storage = data.split(',')
                storage[-1] = storage[-1].strip()
                if num ==int(hiring):
                    hired=("{} hired for ${:.2f}".format(storage[0], float(storage[2])))
                num+=1
            print(hired)
            input_file.close()

def return_item():
    show = ""
    counter = 0
    record = ""
    input_file = open('inventory.csv', 'r+')
    for data in input_file:
        storage = data.split(',')
        storage[-1] = storage[-1].strip()
        if storage[3] == "in":
            storage[3] = ""
        elif storage[3] == "out":
            storage[3] = "*"
        if storage[3] == "*":
            show += ("{} - {}({})\t\t\t\t= $ {:.2f} {}\n ".format(counter, storage[0], storage[1], float(storage[2]),storage[3]))
            if record == "":
                record += str(counter)
            else:
                record += "," + str(counter)
        counter += 1
    input_file.close()
    print(show)
    reitem = (input("Enter the number of an item to return\n"))
    for i in record.split(','):
        if reitem == i:
            num = 0
            ret = ""
            input_file = open('inventory.csv', 'r+')
            for data in input_file:
                storage = data.split(',')
                storage[-1] = storage[-1].strip()
                if num == int(reitem):
                    ret = ("{} returned".format(storage[0]))
                num += 1
            print(ret)
            input_file.close()
#3 items loaded from items.csv
#user_input=input("""Menu:
#(L)ist all items
#(H)ire an item
#(R)eturn an item
#(A)dd new item to stock
#(Q)uit""")
print (return_item())
