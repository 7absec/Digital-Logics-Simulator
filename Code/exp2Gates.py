# ************* Concatenation of gates ****************


#Gates fucntions
def AND (a, b):
    if a == '1' and b == '1':
        return True
    else:
        return False

def NAND (a, b):
    if a == '1' and b == '1':
        return False
    else:
        return True

def OR(a, b):
    if a == '0' and b=='0':
        return False
    else:
        return True

def NOR(a, b):
   if a =='0' and b=='0':
       return True
   else:
       return False

def NOT(a):
    if(a == '0'):
        return True
    elif(a == '1'):
        return False

def XOR (a, b):
    if a != b:
        return True
    else:
        return False

def XNOR(a,b):
    if(a == b):
        return True
    else:
        return False
