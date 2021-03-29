
def AND (a, b, c):
    if a == '1' and b == '1' and c == '1':
        return '1'
    else:
        return '0'

def OR(a, b, c ,d):
    if a == '1'or b == '1' or c == '1' or d == '1':
        return '1'
    else:
        return '0'

def NOT(a):
    if a == '1' :
        return '0'
    else:
        return '1'

