def genPrimes():
    """
    Yield: the next possible prime number
    """
    primes_found = [2]
    current = 2
    yield 2
    while True:
        is_prime = True

        current += 1

        # If the number can be divided by any other prime number,
        # it cannot be prime itself
        for number in primes_found:
            if current % number == 0:
                is_prime = False

        # If the number is prime
        if is_prime:
            primes_found.append(current)
            yield current

"""
Used for running, do not include when submitting to grader
"""
primes = genPrimes()

for i in range(200):
    print(primes.__next__())
