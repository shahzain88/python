class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if(PlayerCharacter.membership):
            self.name = name
            self.age = age

    def shout(self):
        print(f'My name is {self.name}.')
        return ""


player1 = PlayerCharacter('Jasica', 23)
player2 = PlayerCharacter('jhon', 46)

print(player1.name)
print(player2.name)
