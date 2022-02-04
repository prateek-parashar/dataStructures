def is_anagram(s1, s2):
    x = set(s1)
    result = True
    for i in s2:
        if i not in x:
            result = False

    return result

    
