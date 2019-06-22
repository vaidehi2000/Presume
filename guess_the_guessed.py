import random
def generate():
    num = ""
    for i in range(3):
        r = random.randint(0,1)
        if(i==0):
            n = random.randint(1,9)
        else:
            if((r==0 or n==9) and n!=1):
                n = random.randint(1,n-1)
            else:
                n = random.randint(n+1,9)
        num += str(n)
    return num

def check(a,b):
    r=0
    for i in range(3):
        if a[i]==b[i]:
            r=1
            break

    if(r==0):
        for i in range(3):
            for j in range(i,3):
                if(a[i]==b[j]):
                    r=2
                    break
    return r

c = generate()
d = str(input("Enter a 3 digit number with all different digits: "))
while(c!=d):
    r = check(c,d)
    if(r==0):
        print("NOPE")
    elif(r==1):
        print("MATCH")
    elif(r==2):
        print("CLOSE")

    d = str(input("Enter a 3 digit number with all different digits: "))
print("You found the number!!")
