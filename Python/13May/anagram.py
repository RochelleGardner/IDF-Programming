#! /usr/bin/env python3
'''
    Rochelle Gardner
    13 May 2019
    Anagrams
        Write a function that checks whether two words are anagrams. 
    Two words are anagrams if they contain the same letters. For 
    example, silent and listen are anagrams. Write a test program 
    that prompts the user to enter two strings and if they are 
    anagrams, display "is an anagram" otherwise, "is not an anagram"
'''

def isAanagram(string1, string2):
    s1 = sorted(string1)
    s2 = sorted(string2)
    if s1 == s2:
        print("Those are anagrams.")
    else:
        print("Those are not anagrams.")

def main():
    string1 = input("Enter the first word: ")
    string2 = input("Enter the second word: ")
    isAanagram(string1, string2)

main()
