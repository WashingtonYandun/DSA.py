# Special Pythagorean triplet
'''
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def pythagorean_triplet(target):
    tripletArr = []
    for a in range(1, target, 1):
        # this implicates that b is bigger than a: b = a + 1
        for b in range(a + 1, target):
            c = target - a - b
            if a**2 + b**2 == c**2:
                tripletArr.append(["a", a])
                tripletArr.append(["b", b])
                tripletArr.append(["c", c])
                # only for view the triplet
                print(tripletArr)
                return tripletArr[0][1]*tripletArr[1][1]*tripletArr[2][1]
    return tripletArr


print(pythagorean_triplet(1000))  # 31875000
# print(pythagorean_triplet(12))  # 60
# print(pythagorean_triplet(100))  # []
