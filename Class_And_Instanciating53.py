class PlayerCharacter:
    def __init__(self, name, age, attack):
        self.name = name
        self.age = age
        self.attack = attack

    def run(self):
        print('run')


player1 = PlayerCharacter('Jasica', 23, 40)
player2 = PlayerCharacter('jhon', 46, 30)

print('your name is: ', player1.name)
print(f'{player1.name} is: ', player1.age, 'years old')
print(f'{player1.name} has the attack power of: ', player1.attack, '%')
# print(player1.run())

print('your name is: ', player2.name)
print(f'{player2.name} is: ', player2.age, 'years old')
print(f'{player2.name} has the attack power of: ', player2.attack, '%')
