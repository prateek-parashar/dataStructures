def is_valid(path):
    stack = []
    for i in path:
        if i == "(":
            stack.append(i)
        elif i == ")":
            stack.pop()
    return len(stack) == 0

print(is_valid([")"]))
print(is_valid(["(", ")"]))
print(is_valid(["(", ")", "(", ")"]))