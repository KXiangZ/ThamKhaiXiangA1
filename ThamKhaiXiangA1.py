"""
Tham Khai Xiang 14/4/2016
This is a program taht allow for hiring or returning multiple item.
github link:https://github.com/KXiangZ/ThamKhaiXiangA1
"""


#Welcome message
print('Items for Hire - by Tham Khai Xiang')
storage = []
num = 0

def read_item():
    input_file=open('inventory.csv','r+')
    for data in input_file:
        storage= data.split(',')
        storage[-1]=storage[-1].strip()
        print(storage)
    input_file.close()

def load_item():
    show=''
    num=0
    input_file = open('inventory.csv', 'r+')
    for data in input_file:
        storage = data.split(',')
        storage[-1] = storage[-1].strip()
        if storage[3]=="in":
            storage[3]=""
        elif storage[3]=="out":
            storage[3]="*"
        show+=("{} - {}({})\t\t\t\t= $ {:.2f} {}\n ".format(num,storage[0],storage[1],float(storage[2]),storage[3]))
        num+=1
    return (show)

    input_file.close()
#def hire_item():


#3 items loaded from items.csv
#user_input=input("""Menu:
#(L)ist all items
#(H)ire an item
#(R)eturn an item
#(A)dd new item to stock
#(Q)uit""")
print (load_item())