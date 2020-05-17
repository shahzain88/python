class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {"name": "youki",
                        "has_pets": False
                        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 88

    def __call__(self):
        return "yess?"

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('Red', 0)

# These are the samethings
print(action_figure.__str__())
print(str(action_figure))
# you can only acces to the definition when Toy()is there
print(len(action_figure))
# But it dose not changs out side of class Toy()
print(len("hihhihihih"))

print(action_figure())

print(action_figure['name'])
