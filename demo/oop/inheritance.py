class Base:
    def say_hi(self):
        print("From base")


class Child(Base):
    def say_hi(self):
        print("From child")


Base().say_hi()
Child().say_hi()
