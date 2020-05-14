from collections import Counter

def checkMagazine(magazine, note):
    '''
    Checks if ransom note can be made by cutting words from magazine.

    Solution: Use Hash Table to count frequency of words in each one 
    and compare them to see if it's possible or not.

    Time Complexity: O(N) where N is number of letters in note + magazine
                      (should we consider that hash of string is O(length))
    Space Complexity: O(M) where M is number of distinct words
    '''
    noteCounter = Counter(note)
    magazineCounter = Counter(magazine)

    for word in note:
        if noteCounter[word] > magazineCounter[word]:
            print('No')
            break
    else:
        print('Yes')