#**************Full Adder*********************

from cv2 import cv2
from exp3Gates import *
import DigitaLogicSimulator

def exit():
    DigitaLogicSimulator.DLS()


def image1(Img1):
    if Img1 == 'Y':
        img = cv2.imread('image\HalfAdder.png')
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        continue_()
    else:
        continue_()

def image2(Img2):
    if Img2 == 'Y':
        img = cv2.imread('image\FullAdder.png')
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        continue_()
    else:
        continue_()

def continue_():
    ans = input("\nDo you want to continue(y/n)? : ").capitalize()
    if ans == 'Y':
        selector3()
    elif ans == "N":
        exit()
    else:
        print("Please enter a valid option.")
        continue_()

def fullAdder(a,b,c):
    op1 = XOR(a,b)
    op2 = AND(a,b)
    op3 = XOR(op1,c)
    op4 = AND(c,op1)
    op5 = OR(op2,op4)
    return op3,op5

def halfAdder(a,b):
    x = XOR(a, b)
    a = AND(a, b)
    sum   = x
    carry = a
    return sum,carry


def selector3():
    print("\t\t\t\t/------------------------------\ ")
    print("\t\t\t\t      EXPERIMENT NUMBER: 3  ")
    print("\t\t\t\t\------------------------------/")
    print("\n\t\t\t   To realize half adder and Full Adder")
    print("\t\t\__________________________________________________________/")
    print("\n\t /----------\ ")
    print("\t    MENU")
    print("\t \----------/")
    print("\n\t(1) HALF ADDER \n\t(2) FULL ADDER\n")
    z = input ("Please selcet the Adder: ")
    if z =='1':
        print("\n\t\t/----------------------\ ")
        print("\t\t\tHALF ADDER")
        print("\t\t\----------------------/ ")
        print("\n\tPlease enter the inputs(1/0):")
        a = input("\n\t\t\t input A: ")
        b = input("\t\t\t input B: ")
        if a and b in ['1', '0']:
            print("\n\t Half Adder Output:")
            print("\n\t\tSum =",halfAdder(a,b)[0])
            print("\t\tCarry=", halfAdder(a,b)[1])
            Img1 = input("\n\n\tWould you like to see picture of halfAdder(y/n)? : ").capitalize()
            image1(Img1)
        else:
            print("pls select correct value of a and b.")
            continue_()
    elif z =='2':
        print("\n\t\t/----------------------\ ")
        print("\t\t\tFULL ADDER")
        print("\t\t\----------------------/ ")
        print("\n\tPlease enter the inputs(1/0):")
        a = input("\n\t\t\t input A: ")
        b = input("\t\t\t input B: ")
        c = input("\t\t\t Carry input C: ")
        if a and b and c in ['1', '0']:
            print("\n\t FullAdder Output:")
            print("\n\t\tSum =", fullAdder(a,b,c)[0])
            print("\t\tCarry=", fullAdder(a,b,c)[1])
            Img2 = input("\n\n\tWould you like to see picture of halfAdder(y/n)? : ").capitalize()
            image2(Img2)
        else:
            print("pls select correct value of a and b.")
            continue_()
        continue_()