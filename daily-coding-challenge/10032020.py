"""
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

"""

def solution(str1,str2):
    if str1[0] != str2[0]:
        return ""
    if len(str1)>len(str2):
        s1, s2 = str1, str2
    else: 
        s2, s1 = str1, str2
    m,n = len(s1),len(s2)
    cd = gcd(m,n)
    if s2[:cd] * int(m/cd) == s1:
        return s2[:cd]
    else:
        return ""

def gcd(m,n):
    while n != 0:
        (m,n) = (n,m % n)
    return m

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
print(solution(str1,str2))