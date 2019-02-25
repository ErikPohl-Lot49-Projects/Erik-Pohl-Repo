import string
class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        return ''.join([x.lower() for x in s if x in string.ascii_letters+string.digits])[0:len(''.join([x.lower() for x in s if x in string.ascii_letters+string.digits]))//2] == ''.join([x.lower() for x in s if x in string.ascii_letters+string.digits])[len(''.join([x.lower() for x in s if x in string.ascii_letters+string.digits]))//2*2:len(''.join([x.lower() for x in s if x in string.ascii_letters+string.digits]))//2-abs(1-len(''.join([x.lower() for x in s if x in string.ascii_letters+string.digits]))% 2):-1]
