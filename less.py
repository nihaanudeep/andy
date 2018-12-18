
def lesser_twonumbers(x,y):
    if x%2==0 and y%2==0:
        if x<y:
            result= x
        else:
            result= y
    else:
        if x>y:
            result=x
        else:
            result=y
    return result
print(lesser_twonumbers(2,4))