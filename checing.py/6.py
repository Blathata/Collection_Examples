from random import randint


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars 
        self.max_length = max_length
        self.min_length = min_length

        
    def __call__(self, *args, **kwds):
        n = randint(self.min_length, self.max_length)
        return "".join(self.psw_chars[randint(0, len(self.psw_chars) - 1)] for _ in range(n))

lp = RandomPassword ("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [lp(), lp(), lp()]
print(lst_pass)