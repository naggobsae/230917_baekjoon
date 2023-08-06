def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
c, d = map(int, input().split())

mother = int(b * d / gcd(b, d))
son = int(mother * a / b + mother * c / d)

if gcd(mother, son) != 1:
    mother, son = int(mother / gcd(mother, son)), int(son / gcd(mother, son))

print("{0} {1}".format(son, mother))
