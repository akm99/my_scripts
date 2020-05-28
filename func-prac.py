def find_prime(x):
    for i in range(2,x):
        if (x%i) == 0:
             print("it is not prime")   
             break
    else:
        print("it is prime")
    
find_prime(113)
find_prime(120)


