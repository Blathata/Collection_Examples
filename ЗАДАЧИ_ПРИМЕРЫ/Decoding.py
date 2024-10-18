"""Method 1: Using Recursion"""

def decodeString(s):
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            decoded_string = ''
            while stack and stack[-1] != '[':
                decoded_string = stack.pop() + decoded_string
            stack.pop()  # Pop the '['
            num = ''
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            stack.append(int(num) * decoded_string)
    return ''.join(stack)

"""Method 2: Using Stack"""


def decodeString(s):
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            decoded_string = ''
            while stack[-1] != '[':
                decoded_string = stack.pop() + decoded_string
            stack.pop()  # Pop the '['
            num = ''
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            stack.append(int(num) * decoded_string)
    return ''.join(stack)

"""Method 3: Using Regular Expressions"""

import re
def decodeString(s):
    pattern = r'(\d+)\[([a-zA-Z]+)\]'
    while re.search(pattern, s):
        s = re.sub(pattern, lambda m: int(m.group(1)) * m.group(2), s)
    return s


"""Method 4: Using a Recursive Approach (Alternative) Использование рекурсивного подхода"""

def decodeString(s):
    def helper(s, i):
        decoded_string = ''
        num = ''
        while i < len(s):
            if s[i].isdigit():
                num += s[i]
            elif s[i] == '[':
                inner_decoded_string, i = helper(s, i + 1)
                decoded_string += int(num) * inner_decoded_string
                num = ''
            elif s[i] == ']':
                return decoded_string, i
            else:
                decoded_string += s[i]
            i += 1
        return decoded_string
    return helper(s, 0)


"""Method 5: Using a Stack and Iterative Approach"""

def decodeString(s):
    stack = []
    current_num = 0
    current_string = ''
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_string, current_num))
            current_string = ''
            current_num = 0
        elif char == ']':
            prev_string, num = stack.pop()
            current_string = prev_string + num * current_string
        else:
            current_string += char
    return current_string


"""Method 6: Using a Recursive Approach with Pointer"""

def decodeString(s):
    def helper(s, pointer):
        decoded_string = ''
        num = ''
        
        while pointer < len(s):
            if s[pointer].isdigit():
                num += s[pointer]
            elif s[pointer] == '[':
                inner_decoded_string, pointer = helper(s, pointer + 1)
                decoded_string += int(num) * inner_decoded_string
                num = ''
            elif s[pointer] == ']':
                return decoded_string, pointer
            else:
                decoded_string += s[pointer]
            pointer += 1
        return decoded_string, pointer
    return helper(s, 0)[0]


"""Method 7: Using a Stack with Improved Efficiency"""

def decodeString(s):
    stack = []
    decoded_string = ''
    num = 0
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '[':
            stack.append((decoded_string, num))
            decoded_string = ''
            num = 0
        elif char == ']':
            prev_string, prev_num = stack.pop()
            decoded_string = prev_string + prev_num * decoded_string
        else:
            decoded_string += char
    return decoded_string