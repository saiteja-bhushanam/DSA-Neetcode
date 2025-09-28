def palindrome(s:str):
    len_s = len(s)
    start = 0
    end = len_s - 1
    while start < end:
        if not s[start].isalnum():
            start += 1
            continue
        if not s[end].isalnum():
            end -= 1
            continue
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True

print(palindrome("racecar"))
print(palindrome("hello"))
print(palindrome("A man, a plan, a canal: Panama"))
print(palindrome("No 'x' in Nixon"))
print(palindrome("12321"))