import gates
import circuits
import DigitaLogicSimulator

def exit():
    DigitaLogicSimulator.DLS()

def continue_():
    ans = input("\nDo you want to continue(y/n) ?").capitalize()
    if ans=='Y':
        selector1()
    elif ans=="N":
        exit()
    else:
        print("Please enter a valid option")
        continue_() 
    

def Truth_table(gate_name,gate):
    ans = input("\tDo you want to see the Truth Table(y/n)? : ").capitalize()
    if ans == 'Y':
        print("\n\n+-----------------------+----------------------------+")
        print("  | %s Truth Table          | Result |" % gate_name)
        print("   A = False, B = False | A %s B =" % gate_name, gate('0', '0'), " | ")
        print("   A = False, B = True  | A %s B =" % gate_name, gate('0', '1'), " | ")
        print("   A = True , B = False | A %s B =" % gate_name, gate('1', '0'), " | ")
        print("   A = True , B = True  | A %s B =" % gate_name, gate('1', '1'), " | ")
        continue_()

    elif ans == "N":
        continue_()
    else:
        print("Please enter a valid option")
        selector1()


def special_NOT(): #special case for not gate bcz only one input is accepted.
    
    print("\nGATE : <<<<<<<< NOT >>>>>>>")
    a=input("\nEnter the  value of a for NOT gate (0 or 1) : ")
    if a in ['0','1']:
        print("\nFinal output of  NOT(%s) is :  "%(a),gates.NOT(a))
        circuits.not_circ_view(a)
        ans=input("\nDo you want  to see truth table(y/n)?").capitalize()
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
            continue_()
    else:
        print(" ! ! ! ! !\na can have only two values (1 or 0) ie True and False :")
        continue_()


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
        print("\nFinal output of %s(%s,%s) is :  "%(gate_name,a,b),int(gate(a, b)))
        circuits.circ_view(a,b,gate_name)
        Truth_table(gate_name,gate)

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
            print('\nSORRY SOME ERROR OCCURRED')
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
            print('\nSORRY SOME ERROR  OCCURED')

def selector1():
    print("\t\t\t\t/------------------------------\ ")
    print("\t\t\t\t      EXPERIMENT NUMBER: 1  ")
    print("\t\t\t\t\------------------------------/")
    print("\n\t\t\tVerify the TRUTH TABLE of various Logic Gates")
    print("\t\t\__________________________________________________________/")
    print("\n\t /----------\ ")
    print("\t    MENU")
    print("\t \----------/")
    print("\nPlease select the number of Gate you want to operate : ")
    print("\n\t1.AND\t\t2.NAND\t\t3.OR\t\t4.NOR\n\t5.NOT\t\t6.XOR\t\t7.XNOR\t\t8.Exit")
    entry = int(input("\nEnter the number of Gate : "))
    select(entry)
    continue_()