read = lambda: map(int, input().split())

P = 10**9 + 7

def mul(a, b):
    return ((a[0] * b[0] - a[1] * b[1]) % P, (a[0] * b[1] + a[1] * b[0]) % P)

def my_pow(a, b):
    ret = (1, 0)
    while b > 0:
        if (b & 1) == 1:
            ret = mul(ret, a)
        a = mul(a, a)
        b >>= 1
    return ret

n, = read()
for _ in range(n):
    p, q, n = read()
    a = my_pow((q, p), n)
    print(a[1] * pow(a[0], P - 2, P) % P)
# question: value of tan(na) when tan a is given
# hackerrank.com/challenges/simple-one/problem
