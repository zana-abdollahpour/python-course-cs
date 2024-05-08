class User:
    race = "human"
    active_users = 0

    @classmethod
    def display_active_users(cls): print(cls.active_users)

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self): return f"{self.first} {self.last} of age {self.age}."

    def full_name(self): return f"{self.first} {self.likes}"

    def initials(self): return f"{self.first[0]}.{self.last[0]}."

    def is_senior(self): return self.age > 64


joe = User("Joe", "Atkinson", 44)
rebecca = User("Rebecca", "Atkinson", 44)


print(rebecca.first)
print(joe.initials())
print(User.race is joe.race)
User.display_active_users()
