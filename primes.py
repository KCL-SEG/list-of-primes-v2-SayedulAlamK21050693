"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if(number_of_primes <= 0):
        raise ValueError

    i = 2
    if i == 2:
        list.append(i)
        i+=1
    x = 1

    while x <  number_of_primes:
        for j in range(2, i):
            if i%j==0:
                break

        if i == j+1:
            list.append(i)
            x+=1

        i=i+1
    return list

listy = primes(10)
print(listy)
