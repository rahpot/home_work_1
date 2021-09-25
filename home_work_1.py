n = int(input())
print(n // 3600 % 24, n % 3600 // 60, n % 3600 % 60, sep=':')
