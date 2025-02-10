class GFG:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return str((self.a, self.b))
gfg = [GFG("geeks", 1),
       GFG("computer", 3),
       GFG("for", 2),
       GFG("geeks", 4),
       GFG("science", 3)]


print(sorted(gfg, key=lambda x: x.b))
