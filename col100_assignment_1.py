
#ASSIGNMENT1 PART1
#QUESTION 1

def xor(a,b):
    # The addition of two numbers.
#
# Parameters:
# a: boolean -- the first number
# b: boolean -- the second number
#
# Returns: boolean -- the addition of a and b


    return ((a or b)and not(a and b))
def hfadder(a,b):
    return ((a or b)and not(a and b), a and b)

def add(a,b,c):
    vv=(xor(xor(a,b),c),(a or b)and(b or c)and (a or c))
    #vv will return the value
    return vv

# QUESTION2

def add4(a0,a1,a2,a3,  b0,b1,b2,b3, c):
    # The addition of four bit .
#
# Parameters:
# a: boolean -- the first number
# b: boolean -- the second number
# c: boolean -- the third number
#
# Returns: boolean -- the addition of a,b,c

    return (add(a0,b0,c)[0],add(add(a0,b0,c)[1],a1,b1)[0],add(add(add(a0,b0,c)[1],a1,b1)[1],a2,b2)[0],add(add(add(add(a0,b0,c)[1],a1,b1)[1],a2,b2)[1],a3,b3)[0],add(add(add(add(a0,b0,c)[1],a1,b1)[1],a2,b2)[1],a3,b3)[1])
 

 #QUESTION3
def comp(a0,a1,a2,a3,  b0,b1,b2,b3):
    x=8*a3+4*a2+2*a1+a0
    y=8*b3+4*b2+2*b1+b0
    if x>y:
        return True
    else:
        return False


#QUESTION 4

def halfsub(l,m):
    return (xor(l,m) ,(not l)and m )


def sub3(a,b,borrow):
    return (xor(xor(a,b),borrow),(b and borrow)or((not a) and borrow) or ((not a) and b))

def sub4(a0,a1,a2,a3, b0,b1,b2,b3):
    #a3210-b3210
    if comp(a0,a1,a2,a3,  b0,b1,b2,b3) == True:

        return halfsub(a0,b0)[0], sub3(a1,b1,halfsub(a0,b0)[1])[0],sub3(a2,b2,sub3(a1,b1,halfsub(a0,b0)[1])[1])[0],sub3(a3,b3,sub3(a2,b2,sub3(a1,b1,halfsub(a0,b0)[1])[1])[1])[0] , False 
    else:
        return halfsub(b0,a0)[0], sub3(b1,a1,halfsub(b0,a0)[1])[0],sub3(b2,a2,sub3(b1,a1,halfsub(b0,a0)[1])[1])[0],sub3(b3,a3,sub3(b2,a2,sub3(b1,a1,halfsub(b0,a0)[1])[1])[1])[0] , True



#JUST CHECKING
#print (sub4(True,True,True,True, False,True,True,True))
# print(sub3(True,True,True))


#PART 2     QUESTUION (5)
def add8(a, b, c):
    (a0,a1,a2,a3,a4,a5,a6,a7) = a
    (b0,b1,b2,b3,b4,b5,b6,b7) = b
    #a76543210+b7543210
    
    
    
    (l5,l6,l7,l8,l9) =add4(a4,a5,a6,a7,  b4,b5,b6,b7 ,False)
    (l0,l1,l2,l3,l4)= add4(a0,a1,a2,a3,  b0,b1,b2,b3 ,False)


    (m0,m1,m2,m3,m4)= add4(l4,False,False,False, l5,l6,l7,l8 ,False)
        

    return (l0,l1,l2,l3,m0,m1,m2,m3),(m4 or l9)

#Part 2     QUESTION 6
#Multiply

def subx(a0,a1,a2,a3, b0,b1,b2,b3):
     return halfsub(a0,b0)[0], sub3(a1,b1,halfsub(a0,b0)[1])[0],sub3(a2,b2,sub3(a1,b1,halfsub(a0,b0)[1])[1])[0],sub3(a3,b3,sub3(a2,b2,sub3(a1,b1,halfsub(a0,b0)[1])[1])[1])[0]

def mul4(a0,a1,a2,a3, b0,b1,b2,b3):
    l=(b0,b1,b2,b3),
    if l==(False,False,False,False):
        return (False,False,False,False,False,False,False,False)

    else:
        return add8(a0,a1,a2,a3,False,False,False,False, mul4(a0,a1,a2,a3, subx(b0,b1,b2,b3, True,False,False,False)))

    
    #add8(a0,a1,a2,a3,False,False,False,False, mul4(a0,a1,a2,a3, sub4(b0,b1,b2,b3, True,False,False,False)))
    # x=8*a3+4*a2+2*a1+a0
    # y=8*b3+4*b2+2*b1+b0
    # def mul(x,y):
    #     if y==0:
    #         return 0

    #     else:
    #         return x+ mul(x,y-1)

    # return(bin(mul(x,y)))
            


# a=mul4(True,True,True,True, True,True,True,True)[9]
# b=mul4(True,True,True,True, True,True,True,True)[8]
# c=mul4(True,True,True,True, True,True,True,True)[7]
# d=mul4(True,True,True,True, True,True,True,True)[6]
# e=mul4(True,True,True,True, True,True,True,True)[5]
# f=mul4(True,True,True,True, True,True,True,True)[4]
# g=mul4(True,True,True,True, True,True,True,True)[3]
# h=mul4(True,True,True,True, True,True,True,True)[2]
# i=mul4(True,True,True,True, True,True,True,True)[1]
# j=mul4(True,True,True,True, True,True,True,True)[0]

#,True,True,True, True,True,True,True)[9]),(mul4(True,True,True,True, True,True,True,True))

# print((int (a),int (b),int (c),int (d),int (e),int (f),int(g),int (h)))





# print(max((False,False,True,True) ,( True,True,True,False)))


print(mul4(True,True,True,True, True,True,True,True))