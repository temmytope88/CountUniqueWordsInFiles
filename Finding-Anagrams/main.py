# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    list1 = word.strip()
    word1 = sorted(list1)
    list2 = anagram.strip(" ")
    word2 = sorted(list2.replace(" ", ""))
    print (word1)
    print (word2)
    
    return print(word1 == word2)
    
    
find_anagrams("hello\n", "llo heii")

find_anagrams("maize", "madam")

 

