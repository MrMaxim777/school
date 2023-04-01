def bintodec(n):
    def f2to10(n, r):
        if n == 0:
            return 0
        return n % 10 * 2**r + f2to10(n // 10, r + 1)
    print(f2to10(n, 0))


bintodec(1010)
