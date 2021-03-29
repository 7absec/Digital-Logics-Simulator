
from exp2Gates import *
from cv2 import cv2
import DigitaLogicSimulator

def exit():
    DigitaLogicSimulator.DLS()

def continue_():
    ans=input("Do you want to continue(y/n)? : ").capitalize()
    if ans=='Y':
        selector2()
    elif ans=="N":
        exit()
    else:
        print("Please enter a valid option.")
        continue_() 


def none_to_str(a,b,gate):    #this to convert none varable to string
    if  gate(a,b)==True:
        return "1"
    elif gate(a,b)==False:
        return "0"
    else:
        print("error")
    continue_()
    
def not_add(a,b,gate):                           #OR gate 
    
    if  gate=='1':
        STR1= none_to_str(a,b,OR)
        print("OR(%s,%s)=%s"%(a,b,OR(a,b)))
        print("NOT(result of OR(%s,%s))=%s"%(a,b,NOT(STR1)))
        continue_()

    elif gate=='2':                             #AND gate
        str1 = none_to_str(a,b,AND) 
        print('AND(%s,%s) = %s'%(a,b,AND(a,b)))
        print('NOT( result of AND(%s,%s) ) = %s'%(a,b,NOT(str1)))
        continue_()

    elif gate=='3':
        return None

    else:
        print("\n pls select proper option")
        continue_()


def selector2():
    print("\t\t\t\t/------------------------------\ ")
    print("\t\t\t\t      EXPERIMENT NUMBER: 2  ")
    print("\t\t\t\t\------------------------------/")
    print("\n\t\t\tImplementing NOR gate & NAND gate using NOT gate")
    print("\t\t\__________________________________________________________/")
    print("\n\t /----------\ ")
    print("\t    MENU")
    print("\t \----------/")
    print("\n\tplease select the gate : \n\t\t1.OR\t\t2.AND\t\t3.Exit")        #can be canceled(just selector)
    entry=input("\n\tEnter the option: ")
    if  entry in ['1','2']:
        a=input("\n\t\tenter value of a: ")
        b=input("\t\tenter value of b: ")
        if  a and b in ['1','0']:
            print ("final output is:")
            print(not_add(a,b,entry))
        else:
            print("pls select correct value of a and b")
            continue_()
    elif entry=='3':
        exit()

    else:
        print("Enter the correct option.")
    continue_()




























