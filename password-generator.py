import random

l_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
u_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','+',')','(']

print('Welcome to Password Generator!')

n_l_letters = int(input('How many lower letter you want in your password?\n'))
n_u_letters = int(input('How many upper letter you want in your password?\n'))
n_numbers = int(input('How many numbers you want in your password?\n'))
n_symbols = int(input('How many symbols you want in your password?\n'))
n_passwords = int(input('How many possword you want'))

for i in range(1,n_passwords+1):

    password_list = []

    for i in range(1,n_l_letters+1):
        char = random.choice(l_letters)
        password_list += char

    for i in range(1,n_u_letters+1):
        char = random.choice(u_letters)
        password_list += char

    for i in range(1,n_numbers+1):
        char1 = random.choice(numbers)
        password_list += char1

    for i in range(1,n_symbols+1):
        char2 = random.choice(symbols)
        password_list += char2

    random.shuffle(password_list)

    password = ''

    for ch in password_list:
        password += ch

    print(password)

print()