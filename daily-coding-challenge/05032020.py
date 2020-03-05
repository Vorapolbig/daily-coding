"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.
"""

def solution(ransomNote,magazine):
    ransomNote = list(ransomNote)
    magazine = list(magazine)
    ransom = ransomNote.copy()
    for i in ransom:
        if i in set(magazine):
            ransomNote.remove(i)
            magazine.remove(i)
        else:
            return False
    return True

ransomNote,magazine = "aa", "aab"
print(solution(ransomNote,magazine))