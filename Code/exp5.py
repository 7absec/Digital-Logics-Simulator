

#**************** UNIVERSAL GATES ****************
from exp5Gates import *
from cv2 import cv2
import DigitaLogicSimulator

def exit():
    DigitaLogicSimulator.DLS()


#*************** CONTINUE *****************
def continue_():
    ans = input("\nDo you want to continue(y/n)? : ").capitalize()
    if ans == 'Y':
        selector5()
    elif ans == "N":
        exit()
    else:
        print("Please enter a valid option.")
        continue_()


#*************** UNIVAESAL NAND GATE ****************
def nandToNot(a):
    op = NAND(a,a)
    return op

def nandToAnd(a,b):
    op1 = NAND(a,b)
    op2 = NAND(op1,op1)
    return op2

def nandToOr(a,b):
    op1 = NAND(a,a)
    op2 = NAND(b,b)
    op3 = NAND(op1,op2)
    return op3

def nandToNor(a,b):
    op1 = NAND(a, a)
    op2 = NAND(b, b)
    op3 = NAND(op1, op2)
    op4 = NAND(op3,op3)
    return op4

def nandToXor(a,b):
    op1 = NAND(a,b)
    op2 = NAND(a,op1)
    op3 = NAND(b,op1)
    op4 = NAND(op2,op3)
    return op4

def nandToXnor(a,b):
    op1 = NAND(a, b)
    op2 = NAND(a, op1)
    op3 = NAND(b, op1)
    op4 = NAND(op2, op3)
    op5 = NAND(op4,op4)
    return op5

#************** UNIVERSAL NOR GATE ****************
def norToNot(a):
    op = NOR(a,a)
    return op

def norToOr(a,b):
    op1 = NOR(a,b)
    op2 = NOR(op1,op1)
    return op2

def norToAnd(a,b):
    op1 = NOR(a,a)
    op2 = NOR(b,b)
    op3 = NOR(op1,op2)
    return op3

def norToNand(a,b):
    op1 = NOR(a,a)
    op2 = NOR(b,b)
    op3 = NOR(op1,op2)
    op4 = NOR(op3,op3)
    return op4

def norToXor(a,b):
    op1 = NOR(a,a)
    op2 = NOR(b,b)
    op3 = NOR(op1,op2)
    op4 = NOR(a,b)
    op5 = NOR(op3,op4)
    return op5

def norToXnor(a,b):
    op1 = NOR(a,b)
    op2 = NOR(a,op1)
    op3 = NOR(b,op1)
    op4 = NOR(op2,op3)
    return op4


def selector5():
    print("\t\t\t\t/------------------------------\ ")
    print("\t\t\t\t      EXPERIMENT NUMBER: 5  ")
    print("\t\t\t\t\------------------------------/")
    print("\n\t\t\tTo reslize the Logic Gates Using Universal gates")
    print("\t\t  \__________________________________________________________/")
    print("\n\t /----------\ ")
    print("\t    MENU")
    print("\t \----------/")
    print("\nSelect the Universal Gate.")
    print("\n\t1.NAND_GATE\n\t2.NOR_GATE")
    GATE = input("\nplease select the Gate:")
    if GATE == '1':
        print("\tselect conversion:")
        print("\n\t1.Nand_To_Not.\n\t2.Nand_To_And.\n\t3.Nand_To_Or.\n\t4.Nand_To_Nor.\n\t5.Nand_To_Xor.\n\t6.Nand_To_Xnor.")
        entry = input("\nEnter your choice:")

#************ ENTRY FOR NAND GATE **************
        if entry == '1':
            print("\n\t\t NAND TO NOT")
            print("\nEnter the inputs(1/0):")
            a = input("\n\t\t\t input A:")
            if a in ['1', '0']:
                print("\n\t\tOutput =",nandToNot(a))
            else:
                print("pls select correct value of a")
            continue_()

        elif entry == '2':
            print("\n\t\t NAND TO NAD")
            print("\nEnter the inputs(1/0):")
            a = input("\n\t\t\tinput A:")
            b = input("\n\t\t\tinput B:")
            if a and b in ['1', '0']:
                print("\n\t\tOutput =",nandToAnd(a,b))
            else:
                print("pls select correct value of a/b")
            continue_()

        elif entry == '3':
            print("\n\t\t NAND TO OR")
            print("\nEnter the inputs(1/0):")
            a = input("\n\t\t\tinput A:")
            b = input("\n\t\t\tinput B:")
            if a and b in ['1', '0']:
                print("\n\t\tOutput =",nandToOr(a,b))
            else:
                print("pls select correct value of a/b")
            continue_()

        elif entry == '4':
            print("\n\t\t NAND TO NOR")
            print("\nEnter the inputs(1/0):")
            a = input("\n\t\t\tinput A:")
            b = input("\n\t\t\tinput B:")
            if a and b in ['1', '0']:
                print("\n\t\tOutput =",nandToNor(a,b))
            else:
                print("pls select correct value of a/b")
            continue_()

        elif entry == '5':
            print("\n\t\t NAND TO XOR")
            print("\nEnter the inputs(1/0):")
            a = input("\n\t\t\tinput A:")
            b = input("\n\t\t\tinput B:")
            if a and b in ['1', '0']:
                print("\n\t\tOutput =",nandToXor(a,b))
            else:
                print("pls select correct value of a/b")
            continue_()

        elif entry == '6':
            print("\n\t\t NAND TO XNOR")
            print("\nEnter the inputs(1/0):")
            a = input("\n\t\t\tinput A:")
            b = input("\n\t\t\tinput B:")
            if a and b in ['1', '0']:
                print("\n\t\tOutput =",nandToXnor(a,b))
            else:
                print("pls select correct value of a/b")
            continue_()

        else:
            print("Select correct one.")
        continue_()
#*************** ENTRY FOR NOR GATE *****************
    elif GATE == '2':
        print("select conversion:")
        print("\n\t1.norToNot.\n\t2.norToAnd.\n\t3.norToOr.\n\t4.norToNand.\n\t5.norToXor.\n\t6.norToXnor.")
        entry = input("\nEnter your choice:")
        if entry == '1':
            print("\n\t\t NOR TO NOT")
            print("\n\tEnter the inputs(1/0):")
            a = input("\n\t\t\tinput A:")
            if a in ['1', '0']:
                print("\n\t\tOutput =", norToNot(a))
            else:
                print("pls select correct value of a")
            continue_()

        elif entry == '2':
            print("\n\t\t NOR TO AND")
            print("\nEnter the inputs(1/0):")
            a = input("\n\t\t\tinput A:")
            b = input("\n\t\t\tinput B:")
            if a and b in ['1', '0']:
                print("\n\t\tOutput =", norToAnd(a, b))
            else:
                print("pls select correct value of a/b")
            continue_()

        elif entry == '3':
            print("\n\t\t NOR TO OR")
            print("\nEnter the inputs(1/0):")
            a = input("\n\t\t\tinput A:")
            b = input("\n\t\t\tinput B:")
            if a and b in ['1', '0']:
                print("\n\t\tOutput =", norToOr(a, b))
            else:
                print("pls select correct value of a/b")
            continue_()

        elif entry == '4':
            print("\n\t\t NOR TO NAND")
            print("\nEnter the inputs(1/0):")
            a = input("\n\t\t\tinput A:")
            b = input("\n\t\t\tinput B:")
            if a and b in ['1', '0']:
                print("\n\t\tOutput =", norToNand(a,b))
            else:
                print("pls select correct value of a/b")
            continue_()

        elif entry == '5':
            print("\n\t\t NOR TO XOR")
            print("\nEnter the inputs(1/0):")
            a = input("\n\t\t\tinput A:")
            b = input("\n\t\t\tinput B:")
            if a and b in ['1', '0']:
                print("\n\t\tOutput =", norToXor(a, b))
            else:
                print("pls select correct value of a/b")
            continue_()

        elif entry == '6':
            print("\n\t\t NOR TO XNOR")
            print("\nEnter the inputs(1/0):")
            a = input("\n\t\t\tinput A:")
            b = input("\n\t\t\tinput B:")
            if a and b in ['1', '0']:
                print("\n\t\tOutput =", norToXnor(a, b))
            else:
                print("pls select correct value of a/b")
            continue_()

        else:
            print("Select correct one.")
        continue_()
    else:
        print("Please enter correct option. ")
        continue_()
    continue_()