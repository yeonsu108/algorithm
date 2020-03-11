for i in range(input()):
    k = input()
    n = input()

    a = range(1, n + 1)
    for j in range(1, k + 1):
        a2 = [ sum(a[:i]) for i in range(1, n + 1) ]
        a = a2

    print a[n - 1]