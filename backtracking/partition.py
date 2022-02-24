def partition(s):
    result = []
    helper(s, 0, [], result)
    return result

def helper(s, index, path, result):
    if index == len(s):
        result.append(list(path))
    else:
        for i in range(index, len(s)):
            path.append(s[index : i + 1])
            helper(s, i + 1, path, result)
            path.pop()


def isPalindrome(s, left, right):
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True


print(partition("abc"))