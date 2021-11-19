# Values and settings in PasswordConfig.json

from random import choice, randint
import string, json

Charpool = []
a = 0
with open('PasswordConfig.json') as f:f = json.load(f)
if f['Lowercase'] == True:
    a += 1
    Charpool.append([])
    for lower in string.ascii_lowercase:Charpool[0].append(lower)
if f['Uppercase'] == True:
    a += 1
    Charpool.append([])
    for upper in string.ascii_uppercase:Charpool[1].append(upper)
if f['Numbers'] == True:
    a += 1
    Charpool.append([])
    for number in range(0, 9):Charpool[2].append(str(number))
if f['SpecialChars'] == True:
    a += 1
    Charpool.append([])
    for char in string.punctuation:Charpool[3].append(char)

# Generate password
def GeneratePassword():
    Password = []
    length = int(input('Password length: '))
    if length >= f['MinLength'] and length <= f['MaxLength']:
        for i in range(length):Password.append(choice(Charpool[randint(0, a-1)]))
    else:
        print(f'Password cannot be less than {f["MinLength"]} and more than {f["MaxLength"]} characters')
        GeneratePassword()
    Password = ''.join(Password)
    print(f'Password: {Password}')

GeneratePassword()

