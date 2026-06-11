"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
def longest_palindrome(filename):
    longest_length = 0
    longest_words = []

    with open(filename, "r") as file:
        for word in file:
            word = word.strip().lower()
            if word == word[::-1]:
                length = len(word)

                if length > longest_length:
                    longest_length = length
                    longest_words = [word]

                elif length == longest_length:
                    longest_words.append(word)

    print("Longest palindrome length:", longest_length)

    for word in longest_words:
        print(word)

longest_palindrome("sowpods.txt")
