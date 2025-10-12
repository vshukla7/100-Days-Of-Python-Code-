# day 37
# try except ke alawa ab finnaly ko padhana hai jo err aaye ya nahi execute hoga hi 


# try:
#     l = [1, 2, 3, 4, 5]
#     i = int (input("enter the index :"))
#     print(l[i])
# except:
#     print(" error occured ")

# finally:
#     print("mai to execute hounga hi chahe try aur except ho ya nahi " \
#     "kyunki mai finally hu")


def func():
    try:
        l = [1, 2, 3, 4, 5]
        i = int (input("enter the index :"))
        print(l[i])
        return 1
    except:
        print(" error occured ")
        return 0
    finally:
        print("mai to execute hounga hi chahe try aur except ho ya nahi " \
        "kyunki mai finally hu")


x = func()
print(x)


# -- ye to functtion me bhi run hoga bhale hi koi return startement laga hai manaega nahi ye run hoga hi bilkul badki didi ki tarah 😂😂