import gates
from DigitaLogicSimulaotr import DLS
import circuits


def exit():
    DLS()

def continue_():
    print("\nDo you want  to continue ?")
    ans=input("Yes-y , No-n (please input your option) : ").capitalize()
    if ans=='Y':
        menu()
    elif ans=="N":
        exit()
    else:
        print("Please enter a valid option")
        continue_() 
    

def Truth_table(gate_name,gate):
    print("\n\n+-----------------------+----------------------------+") 
    print("| %s Truth Table      | Result |"%gate_name) 
    print(" A = False, B = False | A %s B ="%gate_name,gate('0','0')," | ") 
    print(" A = False, B = True  | A %s B ="%gate_name,gate('0','1')," | ") 
    print(" A = True , B = False | A %s B ="%gate_name,gate('1','0')," | ") 
    print(" A = True , B = True  | A %s B ="%gate_name,gate('1','1')," | ")
    continue_() 


def special_NOT(): #special case for not gate bcz only one input is accepted.
    
    print("\nGATE : <<<<<<<< NOT >>>>>>>")
    a=input("\nEnter the  value of a for NOT gate (0 or 1) : ")
    if a in ['0','1']:
        print("\nFinal output of  NOT(%s) is :  "%(a),gates.NOT(a))
        circuits.not_circ_view(a)
        print("\nDo you want  to see the truth table ?")
        ans=input("Yes-y , No-n (please input your option) : ").capitalize()
        if ans=="Y": 
            print("+---------------+----------------+") 
            print(" | NOT Truth Table | Result |") 
            print(" A = False |  NOT A =",gates.NOT('0')," | ") 
            print(" A = True |  NOT A =",gates.NOT('1')," | ") 
            continue_()
        elif ans=='N':
            continue_()
        else:
            print("Please enter a valid option")
            menu()
    else:
        print(" ! ! ! ! !\na can have only two values (1 or 0) ie True and False :")
        continue_()

def menu(): 
    print("\n\tSimulation for Logic gates")
    print("\nMenu")
    print("\nPlease select the number of Gate you want to operate : ")
    print("\n1.AND\n2.NAND\n3.OR\n4.NOR\n5.NOT\n6.XOR\n7.XNOR\n\n8.Exit\n9.!Info!")
    opt = int(input("Enter your option : ")) 
    select(opt)
    

def input_(gate_name,gate):
    if gate_name!='NOT': #special case for not
        print("\nGATE : <<<<<<<< %s >>>>>>>"%gate_name)
        a=input("\nEnter the  value of a for %s gate (0 or 1) : "%gate_name)
        b=input("\nEnter the value of b for %s gate (0 or 1) : "%gate_name)
        if checker(a,b):
            output(a,b,gate_name,gate)
        else:
            print("\t\t ! ! ! ! !\na and b can have only two values (1 or 0) ie True and False \n")
            continue_()
    else:
        special_NOT()
    

def output(a,b,gate_name,gate):
    if checker(a,b):
        print("\nFinal output of %s(%s,%s) is :  "%(gate_name,a,b),gate(a, b))
        circuits.circ_view(a,b,gate_name)
    else:
        print(" ! ! ! ! !\na and b can have only two values (1 or 0) ie True and False :")
        continue_()


def checker(a,b):
    if a and b in ['0','1']:
        return True
    else:
        return False

def select(entry):
    
    if entry==1:
        try:
            input_('AND',gates.AND)
        except ValueError: # If value is not an integer
            print('\nPlease enterSORRY SOME ERROR OCCURRED')
    elif entry==2:
        try:
            input_('NAND',gates.NAND)
        except ValueError: # If value is not an integer
            print('\nSORRY SOME ERROR OCCURRED')
    elif entry==3:
        try:
            input_('OR',gates.OR)
        except ValueError: # If value is not an integer
            print('\nSORRY SOME ERROR OCCURRED')
    elif entry==4:
        try:
            input_('NOR',gates.NOR)
        except ValueError: # If value is not an integer
            print('\nSORRY SOME ERROR OCCURRED')
    elif entry==5:
        try:
            input_('NOT',gates.NOT)
        except ValueError: # If value is not an integer
            print('\nSORRY SOME ERROR OCCURRED')
    elif entry==6:
        try:
            input_('XOR',gates.XOR)
        except ValueError: # If value is not an integer
            print('\nSORRY SOME ERROR OCCURRED')
    elif entry==7:
        try:
            input_('XNOR',gates.XNOR)
        except ValueError: # If value is not an integer
            print('\nSORRY SOME ERROR OCCURRED')
    elif entry==8:
        try:
             return None
        except ValueError: # If value is not an integer
            print('\nSORRY SOME ERROR OCCURED')
    elif entry==9:
        try:
            print("\nCreated by : \n1.Hamza Khalid Baig\t2.Khan Aaftab Aalam\t3.Mohammed ZiyaulHaq\t4.Kazi Uzair")
            continue_()
        except ValueError: # If value is not an integer
            print('\nSORRY SOME ERROR OCCURED')

menu()