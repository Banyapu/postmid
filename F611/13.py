t = 0
n = 2561
while n > 0:
    t *= 10
    t += n % 10
    n //= 10
print(t)
