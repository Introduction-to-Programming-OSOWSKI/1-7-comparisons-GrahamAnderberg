def greaterThan(x, y):
    if int(x > y):
        return True
    else:
        return False

def lessThan(x, y):
    if int(x < y):
        return True
    else:
        return False

def equalTo(x, y):
    if int(x == y):
        return True
    else:
        return False

def greaterOrEqual(x, y):
    if int(x >= y):
        return True
    else:
        return False
    
def lessOrEqual(x, y):
    if int(x <= y):
        return True
    else:
        return False

print(greaterThan(120, 119))
print(lessThan(119, 120))
print(equalTo(120, 120))
print(greaterOrEqual(121, 120))
print(lessOrEqual(120, 121))