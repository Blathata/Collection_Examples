# primer 1
time_start = float(input('primer 1. Введите текущее время: '))
green: int = 3
red: int = 2 
one_cicle = green + red
quentity_cicle = time_start / 5
variable_cicle = time_start - (one_cicle * int(quentity_cicle))

if 0 <= variable_cicle <= 2.9:
    print(f"green")
else:
    print(f"red")

# primer 2
print('green' if 0 <= float(input('primer 2. Введите текущее время: ')) % 5 <= 3 else 'red') 
