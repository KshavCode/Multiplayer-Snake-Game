import time 
import random 

def generate(x,y) : 
    cat = random.randint(x,y)
    dog = random.randint(x,y)
    parrot = random.randint(x,y)

    return cat, dog, parrot

while True :    
    a = int(input("Enter the first range : "))
    b = int(input("Enter the second range : "))
    generate = generate(a,b)
    time.sleep(1)
    print(f"The random numbers printed are {generate}")
    break
