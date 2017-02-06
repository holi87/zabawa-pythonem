import sys

# poczatek mojego

from collections import deque


class Solution:
    # Write your code here
    def __init__(self):
        self.stos = []
        self.kolejka = deque()

    def pushCharacter(self, litera):
        self.stos.append(litera)

    def enqueueCharacter(self, litera):
        self.kolejka.append(litera)

    def popCharacter(self):
        return self.stos.pop()

    def dequeueCharacter(self):
        return self.kolejka.popleft()


# koniec mojego
# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")