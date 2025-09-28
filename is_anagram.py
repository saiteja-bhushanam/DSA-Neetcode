def is_anagram(s: str, t: str) -> bool:
    arr = [0]*26

    for i in s:
        arr[ord(i)-ord('a')] += 1
    for i in t:
        arr[ord(i) % 97] -= 1
    for i in arr:
        if i != 0:
            return False
    else:
        return True

print(is_anagram("racecar","carrace"))