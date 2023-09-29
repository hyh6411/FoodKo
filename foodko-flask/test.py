class Base:
    def __init__(self):
        self.msg = 'create'


class AB(Base):

    def __init__(self):
        self.one = 'hello!'

    def print(self):
        # print(self.msg)
        print(self.one)


ab = AB()
ab.print()
