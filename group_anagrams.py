def group_anagrams(strs):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in strs:
        # Create a tuple of counts for each letter (assuming lowercase a-z)
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        print(count)
        key = tuple(count)
        print(key)
        anagrams[key].append(word)
    return list(anagrams.values())

strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(group_anagrams(strs))