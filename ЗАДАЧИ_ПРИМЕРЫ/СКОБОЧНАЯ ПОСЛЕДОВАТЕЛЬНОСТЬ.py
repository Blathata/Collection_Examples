def is_correct_bracket_seq(res: str):
    while '()' in res or '{}' in res or '[]' in res:
        res = res.replace('()', '')
        res = res.replace('{}', '')
        res = res.replace('[]', '')
    return not bool(res)
        
     
res = '({[]})'
print(is_correct_bracket_seq(res))