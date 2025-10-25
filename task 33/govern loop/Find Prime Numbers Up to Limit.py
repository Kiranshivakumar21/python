limit = int(input("Enter limit: "))
primes = []
for num in range(2, limit+1):
    if all(num % i for i in range(2, int(num**0.5)+1)):
        primes.append(num)
print("Primes:", primes)

