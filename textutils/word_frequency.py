from collections import Counter
"""
Solution inspired from https://www.geeksforgeeks.org/python/find-frequency-of-each-word-in-a-string-in-python/
"""
def word_frequency(s):
    """
    word_frequency() takes a string and returns the frequency of words in it
    """
    words = s.split()
    freq = Counter(words)
    dict = {}
    for w, c in freq.items():
        dict[w] = c
    return dict

#usage exemple    
print(word_frequency("hello hello there"))
