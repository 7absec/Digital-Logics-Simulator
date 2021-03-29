
#************* GATES ***************
def NAND (a, b):
    if a == '1' and b == '1':
        return '0'
    else:
        return '1'

def NOR(a, b):
    if(a == '0') and (b == '0'):
        return '1'
    else:
        return '0'

