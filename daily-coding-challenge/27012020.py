""" Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""
k = 17
num = [10,15,3,7]

def check(k,num):
    pairsum = []
    for n1 in num:
        for n2 in num:
            pairsum.append(n1+n2)

    if k in pairsum:
        return True
    else:
        return False

check(k,num)
