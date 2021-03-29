'''
    Gates for the Concatenatio of gate (concat.py) programme
'''
def AND (a, b):
    if a == '1' and b == '1':
        return '1'
    else:
        return '0'

def NAND (a, b):
    if a == '1' and b == '1':
        return '0'
    else:
        return '1'

def OR(a, b):
    if a == '1' or b == '1':
        return '1'
    else:
        return '0'

def NOR(a, b):
    if(a == '0') and (b == '0'):
        return '1'
    else:
        return '0'

def NOT(a):
    if(a == '0'):
        return '1'
    elif(a == '1'):
        return '0'

def XOR (a, b):
    if a != b:
        return '1'
    else:
        return '0'

def XNOR(a,b):
    if(a == b):
        return '1'
    else:
        return '0'



