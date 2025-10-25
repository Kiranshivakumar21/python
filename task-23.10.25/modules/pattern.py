def rightriangle(n):
    return '\n'.join(['* ' * (i+1) for i in range(n)])

def lefttriangle(n):
    return '\n'.join([' ' * (n-i-1) + '* ' * (i+1) for i in range(n)])

def inverserightriangle(n):
    return '\n'.join(['* ' * (n-i) for i in range(n)])

def inverselefttriangle(n):
    return '\n'.join([' ' * i + '* ' * (n-i) for i in range(n)])
