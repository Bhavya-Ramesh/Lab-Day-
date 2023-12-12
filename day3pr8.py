def group_anagrams(strs):
    anagram_dict = {}
    for word in strs:
        key = tuple(sorted(word))
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = [word]

    result = list(anagram_dict.values())
    return result
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)
