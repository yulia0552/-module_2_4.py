numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []

for n in numbers :
    if n < 2:
        continue
    is_prime =True
    for div in range(2,n):
        if n % div == 0:
            not_primes.append(n)
            is_prime =False
            break
    if is_prime :
        primes.append(n)

print("Primes:" , primes)
print("Not_primes:", not_primes)











