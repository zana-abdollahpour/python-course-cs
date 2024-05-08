class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


c1 = Comment("Andrew", "LOL!", 4)
c2 = Comment("James", "Not Funny!", 14)

print(c1, c2)
