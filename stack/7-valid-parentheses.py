# https://leetcode.com/problems/valid-parentheses/submissions/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def matches(top, closing):
    if top == '{' and closing == '}': return True
    if top == '[' and closing == ']': return True
    if top == '(' and closing == ')': return True
    return False

def isValid(s):
    stack = []
    opening_brackets = {'{', '(', '['}
    closing_brackets = {'}', ')', ']'}
    for bracket in s:
        if bracket in opening_brackets:
            stack.append(bracket)
        if bracket in closing_brackets:
            if len(stack) == 0:
                return False
            top = stack[len(stack) - 1]
            if matches(top, bracket):
                stack.pop()
            else:
                return False

    if len(stack) > 0:
        return False
    return True

print(isValid('([{]})'))

# ()[]{}
# ([{}])
# ([{]})
# ()]

# stack # [{[]
# iterate
#   if opening; add
#   if closing; check if matches top of stack
#       matches; pop stack
#       doesn't match/stack is empty -> invalid -> false
# stack is empty; valid -> true

