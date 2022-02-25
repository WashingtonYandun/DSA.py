# Names scores
'''
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

'''
initial idea
total = 0
for i in range(0, len(names), 1):
    for j in names[i]:
        total = total + abc[j]*(i+1)

print(total)  # 324536 -> NO 
# 871198282
'''


# Maybe this could be solved by using ascii
abc = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}


def from_txt_to_list(p):
    with open(p) as fl:
        names = fl.read()
    # names = names.strip().split('\',\'') -> no useful
    names = names.strip().split(',')
    names = [x[1:-1] for x in names]  # delete ' '
    names.sort()  # important
    return names


def names_scores(arr):
    total = 0
    for i in range(0, len(arr), 1):
        for j in arr[i]:
            total = total + abc[j]*(i+1)
    return total


names = from_txt_to_list('Algo\project_euler\p022_names.txt')
print(names_scores(names))  # 871198282
