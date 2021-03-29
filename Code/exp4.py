
# *****************MUX*********************

from cv2 import cv2
from exp4Gates import *
import DigitaLogicSimulator

def exit():
    DigitaLogicSimulator.DLS()


def image(Img):
    if Img == 'Y':
        img = cv2.imread('image\Mux.png')
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        continue_()
    else:
        print("Please enter the corrct option.")
        continue_()

def continue_():
    ans = input("\nDo you want to continue(y/n)? : ").capitalize()
    if ans == 'Y':
        selector4()
    elif ans == "N":
        exit()
    else:
        print("Please enter a valid option.")
        Img = input("\n\n\tWould you like to see picture of Mux(y/n)? : ").capitalize()
        image(Img)
        continue_()

def Mux(s0,s1,d1,d2,d3,d4):
   not0 = NOT(s0)
   not2 = NOT(s1)
   and1 = AND(d1,not0,not2)
   and2 = AND(d2,not2,s0)
   and3 = AND(d3,s1,not0)
   and4 = AND(d4,s1,s0)
   or_gate = OR(and1,and2,and3,and4)
   return or_gate
def selectedInput(s0,s1,d1,d2,d3,d4):
    if s0=='0' and s1=='0':
        return 'D1'
    elif s0=='0' and s1=='1':
        return 'D2'
    elif s0=='1' and s1=='0':
        return 'D3'
    else:
        return 'D4'

def selector4():
    print("\t\t\t\t/------------------------------\ ")
    print("\t\t\t\t      EXPERIMENT NUMBER: 4  ")
    print("\t\t\t\t\------------------------------/")
    print("\n\t\t\t   To impliment Logic Operations Using MUX")
    print("\t\t   \__________________________________________________________/")
    print("\n\t/----------------\ ")
    print("\t   MULTIPLEXER")
    print("\t\----------------/")
    print("\n\tPlease enter the inputs(1/0):")
    s0 = input("\n\t\t\tinput S0:")
    s1 = input("\t\t\tinput S1:")
    d1 = input("\t\t\tinput D1:")
    d2 = input("\t\t\tinput D2:")
    d3 = input("\t\t\tinput D3:")
    d4 = input("\t\t\tinput D4:")
    if s0 and s1 and d1 and d2 and d3 and d4 in ['1', '0'] and len(s0)==1 and len(s1)==1 and len(d1)==1 and len(d2)==1 and len(d3)==1 and len(d4)==1:
        print("\n\t MUX Output:")
        print("\n\t\tOutput =",Mux(s0,s1,d1,d2,d3,d4))
        print("\n\t\tSelected Input =", selectedInput(s0,s1,d1,d2,d3,d4))
        Img = input("\n\n\tWould you like to see picture of Mux(y/n)? : ").capitalize()
        image(Img)
    else:
        print("please enter the correct values of s0,s1,d1,d2,d3 and d4.\n Only Single Digit Binary is accepted")
        continue_()
    continue_()