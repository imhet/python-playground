# 找出字符串中的最长不重复子串


def lengthOfLongestSubstring(s):
    result, temp = [], []
    for i in range(len(s)):
        if s[i] in result:
            if len(result) >= len(temp):
                temp = result
            result = result[result.index(s[i]) + 1:]

        result.append(s[i])

    return max(len(result), len(temp))


a = 'abcabcbbcadae'
b = 'bbbbb'
c = 'pwwkew'

print(lengthOfLongestSubstring(a))
print(lengthOfLongestSubstring(b))
print(lengthOfLongestSubstring(c))
