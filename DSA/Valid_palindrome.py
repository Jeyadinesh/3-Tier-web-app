def isPalindrome(self, s: str) -> bool:
    newStr=''
    for c in s:
        if c.isalnum():
            newStr+=c
    if newStr.lower() == newStr[::-1].lower():
        return True
    else:
         return False
