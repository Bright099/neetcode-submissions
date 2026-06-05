class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for char in s:
            if char.isalnum():
                string += char.lower()
        check = -1
        for i in range(len(string)):
            if i == (len(string) - check):
                break
            else:
                if string[i] != string[check]:
                    return False
            check -= 1
        return True
        