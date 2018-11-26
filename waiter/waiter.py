#!/bin/python3


def generate_primes(n):
    num = 3
    primes = [2]

    while len(primes) < n:
        add_prime = 1
        for prime in primes:
            if num % prime == 0:
                add_prime = 0
                break
        if add_prime:
            primes.append(num)
        num += 2

    return primes


def waiter(number, q):
    B = []
    A_new = []
    A_cur = number

    primes = generate_primes(q)
    for i in range(q):
        B.append([])
        for _ in range(len(A_cur)):
            num = A_cur.pop()
            if num % primes[i] == 0:
                B[i].append(num)
            else:
                A_new.append(num)
        A_cur, A_new = A_new, A_cur

    res = []
    B.append(A_cur)
    for stack in B:
        res.extend(stack[::-1])
    return res


if __name__ == '__main__':
    nq = input().split()
    n = int(nq[0])
    q = int(nq[1])
    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)
    print('\n'.join(map(str, result)))
