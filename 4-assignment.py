



def factoriyal(x):
    factoriyal=1
    i=0
    while x>0:
        factoriyal=factoriyal*x
        x=x-1
    print(factoriyal)
a=int(input("entr nbr:"))
factoriyal(a)

####method II

def factoriyal(x):
    factoriyal=1
    if x>0:
        for i in range(1,x+1):
            factoriyal=factoriyal*i
        print(x," is factoriyal",factoriyal)
    elif x<=0:
        print("factiriyal cant find negitive nbrs:")

a=int(input("entr nbr:"))
factoriyal(a)
