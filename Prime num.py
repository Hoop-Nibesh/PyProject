lastPrime = 2
current = 2
record = 0

while True:
    isPrime = True
    
    for i in range(current):
        if i > 1:
            if (current / i) < 2:
                break
            if current % i == 0:
                isPrime = False
                break

    if isPrime:
        diff = current - lastPrime
        if record < diff:
            print(diff)
            record = diff
        lastPrime = current

    current = current + 1