import random

def suffle(string):
    temfile=list(string)
    random.shuffle(temfile)
    return ''.join(temfile)

upperclass1=chr(random.randint(40,90)) #generate random passward
upperclass2=chr(random.randint(50,90)) #generate random passward

password=upperclass1+upperclass2

password=suffle(password)

print(password)
