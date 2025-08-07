def length_of_longest_substring(s):
    longest = 0
    current = ""

    for char in s:
        if char in current:
            index = current.index(char)
            current = current[index + 1:]
        current += char
        if len(current) > longest:
            longest = len(current)

    return longest

print(length_of_longest_substring("bcbbb"))     
print(length_of_longest_substring("pwwkew"))    
print(length_of_longest_substring("abcabcbb"))  
print(length_of_longest_substring("dvdf"))      
print(length_of_longest_substring("aab"))       
print(length_of_longest_substring("tmmzuxt"))   