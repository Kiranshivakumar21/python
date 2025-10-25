def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def armstrong(n):
    num = n
    power = len(str(n))
    return sum(int(digit) ** power for digit in str(n)) == num
