#**********************DigitaLogicSimulator*****************#
from exp1 import *
from exp2 import *
from exp3 import *
from exp4 import *
from exp5 import *
from exp6 import *
from exp7 import *

def exit():
    return None

def continue_():
    ans = input("\n\n\tDo you want  to continue?(y/n):").capitalize()
    if ans == 'Y':
        DLS()
    elif ans == "N":
        exit()
    else:
        print("Please enter a valid option.")
        continue_()


def DLS():
    print("\n\n\t/--------------------------------\ ")
    print("\t\tNAME OF EXPERIMENTS")
    print("\t\--------------------------------/")

    print("\n\t1] To verify the truth table of various logic gates \n\t2] Concatenation of two Logic Gates \n\t3] To realize half adder and full adder\n\t4] To implement logic operations using MUX")
    print("\t5] To realize the gates using Universal gates\n\t6] To implement Ripple Carry Adder\n\t7] To implement Booths Algorithm\n\n\t8]Exit\t\t9]About Us")
    print('\n\tNOTE:"Inputs for All the Experiments MUST be in "BINARY" formate (except Experiment 7 [Decimal])."')
    print("________________________________________________________________________________________________________________________")
    a = input("\n\tEnter The Experiment Number Which You want to simulate:: ")
    print("\n")
    
    if a=='1':
        selector1()

    elif a=='2':
        selector2()

    elif a=='3':
        selector3()

    elif a=='4':
        selector4()

    elif a=='5':
        selector5()

    elif a=='6':
        selector6()

    elif a =='7':
        selector7()

    elif a=='8':
        exit()

    elif a=='9':
        print("\t\t\t\t\t/-------------------------\ ")
        print("\t\t\t\t\t       TEAM MEMBERS")
        print("\t\t\t\t\t\-------------------------/ ")
        print("\n\t\t\t\tGuide: Prof. Shaikh Abdussalam")
        print("\n\t\t\t\tMembers:")
        print("\t\t\t\t\t1. Baig Hamzah Khalid [19CO20]")
        print("\t\t\t\t\t2. Kazi Uzair Shahid [19CO22]")
        print("\t\t\t\t\t3. Khan Aaftabaalam Harun [19CO23]")
        print("\t\t\t\t\t4. Mohammad Ziya-Ul-Haq [19CO37]")
        print("_________________________________________________________________________________________________________________________")
        print("\n\n")
        print("\t\t\t\t\t/----------------------------\ ")
        print("\n\t\t\t\t\t\t  THANK YOU")
        print("\n\t\t\t\t\t\----------------------------/ ")
        continue_()
    else:
        print("Plese select a valid Experiment number")
        continue_()

if __name__ == "__main__":
    DLS()

        