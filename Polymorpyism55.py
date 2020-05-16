class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return "logged in"


class Wizerd(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        # super()is the mother class {User}
        super().__init__(email)
        self._name = name
        self._power = power

    def attack(self):

        return print(f"Attacking with the power of: {self._power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        return print(f"Attacking with arrow:the arrow left:{self._num_arrows}")


wizerd1 = Wizerd("mick", 60, "mick@gmail.com")
print(wizerd1.email)
