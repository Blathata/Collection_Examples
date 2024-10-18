def count(s: str):
    if not s:
        return 0
    max_substr = 0
    left_pos = 0
    unique_set = set()#  хранятся символы из уникальной подстроки
    for right_pos in range(len(s)):
        while s[right_pos] in unique_set: #проверяем есть ли уникальный символ  в подстроке
            unique_set.remove(s[left_pos])
            left_pos += 1
        unique_set.add(s[right_pos])
        max_substr = max(max_substr, right_pos - left_pos + 1)

    return max_substr

s = 'qweraaasdf'
print(count(s))