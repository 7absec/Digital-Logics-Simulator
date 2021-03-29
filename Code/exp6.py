#******************RIPPLE CARRY ADDER********************
from exp6Gates import *
from cv2 import cv2
import numpy
import DigitaLogicSimulator

def exit():
    DigitaLogicSimulator.DLS()

def image1(Img1):
    if Img1 == 'Y':
        img = cv2.imread('image\RippleCarryAdder.PNG')
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        continue_()
    else:
        continue_()



def continue_():
    ans=input("\nDo you want to continue(y/n)? : ").capitalize()
    if ans=='Y':
        selector6()
    elif ans=="N":
        exit()
    else:
        print("Please enter a valid option")
        continue_()

def Fulladd(carry,s1,s2):
    out1 = XOR(s1,s2)
    SUM = XOR(out1,carry)
    out2 = AND(carry,out1)
    out3 = AND(s1,s2)
    CARRY = OR(out2,out3)
    return SUM , CARRY

def RippleCarryAdder(num1,num2):
    a=[] #declaring the global list for num1 a.k.a A
    b=[] #declaring the global list for num1 a.k.a B
    ans=[] #declaring the global list for FINAL answer a.k.a SUM & CARRY:
    n1=len(num1) #length of num1 and num2 for processing;
    n2=len(num2) #  """""""""""""""""""""""""""""""""""
    #a function to seperate all the string characters into a list for calculation
    def digit_sep(num1,num2):
        #let the number be in the following format : a[0].a[1].a[2].a[3]
        for i in range(0,n1):
            a.append(num1[i])
        for i in range(0,n2):
            b.append(num2[i])
    digit_sep(num1,num2)
    #a function to add zeros to thee msb
    def zero_adder():
        if n1<4:
            for i in range(0,(4-n1)):
                a.insert(i,'0')
        if n2<4:
            for i in range(0,(4-n2)):
                b.insert(i,'0')
    zero_adder()
    #a function to reverse the order of the lists:
    def reverse():
        a.reverse()
        b.reverse()
    reverse()
    #at this point a and b are reversed:
    #caltulation part: using pre-defined full adder function to carryout the add iterations:
    out1 = Fulladd('0',a[0],b[0])  #first default cary is 0
    out2 = Fulladd(out1[1],a[1],b[1])
    out3 = Fulladd(out2[1],a[2],b[2])
    out4 = Fulladd(out3[1],a[3],b[3])

    #a function will combine the output from a list to a string:
    def combiner():
        ans=[out1[0],out2[0],out3[0],out4[0]]
        ans.reverse() #to reverse ans to readable form
        ans_str=("%s%s%s%s"%(ans[0],ans[1],ans[2],ans[3])) #to connvert list to string:
        return ans_str
    final_ans=combiner()
    return final_ans,out4[1] #the final answer:

def checker(num):
    n = len(num)
    for i in range(0,n):
        if num[i] not in ['0','1'] or n>4:
            return False
    return True

#function for taking input of two binary 4-bit numbers:
def input_():
        print("Please enter the inpust in binary formate(eg. 0101)")
        num1 = input("\nEnter First value(A) : ")
        num2 = input("\nEnter the Second value(B) : ")
        if checker(num1) and checker(num2):
            output(num1,num2)
        else:
            print("\n\t\t ! ! ! ! ! ! ! !\n!! A and B can have only 4 bits binary values !! \n")
            continue_()

#a function to display output:
def output(num1,num2):
    print('The <SUM> of << %s + %s >> = %s and generated <CARRY> = %s'%(num1,num2,RippleCarryAdder(num1,num2)[0],RippleCarryAdder(num1,num2)[1]))
    Img1 = input("\n\n\tWould you like to see picture of Ripple Carry Adder(y/n)? : ").capitalize()
    image1(Img1)
    continue_()

#a function to select the diagram:
'''
def diagram_select():
    opt=input('\nEnter:\n\t1 : For Fulladder circuit.\n\t2 : For Ripple Carry Adder.\n')
    if opt=='1':
        circ_view(path_fulladder)
        continue_()
    elif opt=='2':
        circ_view(path_ripple)
        continue_()
    else:
        print("Please enter the correct option !!")
        continue_()
'''
def select(entry):
    if entry=='1':
        input_()
    else:
        print("Please enter the correct option !!")
        continue_()

#a function for the menu:
def selector6():
    print("\t\t\t\t/------------------------------\ ")
    print("\t\t\t\t      EXPERIMENT NUMBER: 6 ")
    print("\t\t\t\t\------------------------------/")
    print("\n\t\t\t\tTo impliment RIPPLE CARRY ADDER")
    print("\t\t  \__________________________________________________________/")
    print("\n\t /--------------------\ ")
    print("\t   RIPPLE CARRY ADDER ")
    print("\t \--------------------/")
    print("\n\tDescription : ")
    print("\nThis program will ->\n\t1) Accept two 4-bit binaries and perform their addition which\n\t   will result in a SUM & CARRY.")
    #-#starting the  program:
    input_()
    continue_()