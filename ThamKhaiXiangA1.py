"""
Tham Khai Xiang 14/4/2016
This is a program taht allow for hiring or returning multiple item.
github link:https://github.com/KXiangZ/ThamKhaiXiangA1
"""

#def loading_item():




#def hiring_item():

#Welcome message
print('Items for Hire - by Tham Khai Xiang')
storage = ""
num = 0
input_file=open('inventory.csv','r')
for line in input_file:
    if num==0:
        line1=(line.split(","))
        num+=1
        print(line1)
    elif num==1:
        line2 = (line.split(","))
        num+=1
        print(line2)
    elif num==2:
        line3 = (line.split(","))
        num+=1
        print(line3)
input_file.close()

def load_item():
    return("All items on file(*indicates item is currently out):\n"
           "0 -{} ({})\t= ${:.2f}\n".format(line1[0],line1[1],float(line1[2]))+
            "1 -{} ({})\t\t= ${:.2f}\n".format(line2[0],line2[1],float(line2[2]))+
            "2 - {}({})\t\t\t\t\t\t= ${:.2f}\n".format(line3[0],line3[1],float(line3[2])))

def hire_item():

#3 items loaded from items.csv
#user_input=input("""Menu:
#(L)ist all items
#(H)ire an item
#(R)eturn an item
#(A)dd new item to stock
#(Q)uit""")
print (load_item())