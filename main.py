from random import randint
from Lib.Constant import Constant as C

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def menu():
    choice = None
    #loop while user choice is not in defined CHOICES list
    while choice not in C.CHOICES:
        print("------------------------------------")
        print("-------------- Debug ---------------")
        print("------------------------------------")
        print(C.CHOICE_ADD,". Add ")
        print(C.CHOICE_SUB,". Sub ")
        print(C.CHOICE_MUL,". Mul ")
        print(C.CHOICE_DIVIDE,". Divide")
        print(C.CHOICE_EXIT,". Exit")
        try:
            choice = int(input("Select your choice: "))
        except ValueError:#Error if user not enter a number
            print(f"Invalid input. Please enter your choice {C.CHOICES}.")      
    return choice

choice = None
while (choice:=menu())!=C.CHOICE_EXIT:
    #get index
    indexN1 = randint(0,len(C.numberListA))
    indexN2 = randint(0,len(C.numberListB))

    print(f"indexN1 : {indexN1} -- indexN2 : {indexN2}")

    match(choice):
        case 1:#C.CHOICE_ADD
            print(f"\n{C.numberListA[indexN1]}+{C.numberListB[indexN2]}={add(C.numberListA[indexN1],C.numberListB[indexN2])}\n")
        case 2:#C.CHOICE_SUB 
            print(f"\n{C.numberListA[indexN1]}-{C.numberListB[indexN2]}={sub(C.numberListA[indexN1],C.numberListB[indexN2])}\n")
        case 3:#C.CHOICE_MUL
            print(f"\n{C.numberListA[indexN1]}*{C.numberListB[indexN2]}={mul(C.numberListA[indexN1],C.numberListB[indexN2])}\n")
        case 4:#C.CHOICE_DIVIDE
            print(f"\n{C.numberListA[indexN1]}/{C.numberListB[indexN2]}={div(C.numberListA[indexN1],C.numberListB[indexN2])}\n")
        case _:
            print("No choice to match")



