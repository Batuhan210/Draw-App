import random
import time


users = list()

def addUser(x):
    print("-" * 30)
    print("Welcome To The Addition User Screen")
    add = input("User: ")
    users.append(add)
    input("Press the enter to continue...")


def viewUser(x):
    count = 1
    print("-" * 30)
    for i in x:
        print(str(count) +".User Name: ", i)
        count+=1
        print("-" * 30)
    input("Press the enter to continue...")


def chooseRandom(x):
    print("-" * 30)
    count = 1
    choosePerson = int(input("How many people will you choose?: "))
    randomChoose = random.sample(x,choosePerson)

    for i in randomChoose:
        print(str(count) +".User Name: ", i)
        count+= 1
        print("A random person is being selected from the system...")
        time.sleep(3)
    print("-" * 30)
    input("Press the enter to continue...")

def shake(x):
    print("-" * 30)
    count = 1
    random.shuffle(x)
    for i in x:
        print(str(count) +".User Name: ", i)
        count+=1
        print("-" * 30)
    input("Press the enter to continue...")
                
while True:
    print("****Welcome To The Raffle****")
    choose = int(input("1-Add user\n2-View User\n3-Shuffle Users\n4-Choose Random\n5-Exit\n"))
    
    if choose == 1:
        addUser(users)
    elif choose == 2:
        viewUser(users)
    elif choose == 3:
        shake(users)
    elif choose == 4:
        print("Calculating person selection area...")
        time.sleep(2)
        chooseRandom(users)
    elif choose == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please choose a valid option")
