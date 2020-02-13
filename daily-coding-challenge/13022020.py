"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.
"""

def solution(words):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    dict = {}
    for i in range(26):
        dict[alphabet[i]] = morse[i]
    # dict.items()
    decodes = []
    unique = []
    unique_set = set(unique)
    for word in words:
        decode = "" 
        for letter in str(word):
            decode += dict[letter]
        decodes.append(decode)
        if not word in unique_set:
            unique.append(decode)
            unique_set = set(unique)
    
    return len(unique_set)

words = ["gin", "zen", "gig", "msg"]
print(solution(words))