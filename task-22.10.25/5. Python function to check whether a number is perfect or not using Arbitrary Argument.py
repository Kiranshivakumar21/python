def perfect(*numbers):
    for n in numbers:
        total = 0
        for i in range(1, n):
            if n % i == 0:
                total += i
        if total == n:
            print(n, "is a Perfect number")
        else:
            print(n, "is not a Perfect number")
perfect(6, 28, 10)
