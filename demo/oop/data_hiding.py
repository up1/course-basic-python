class Hello:
    __counter_hiding = 0

    def count(self):
        self.__counter_hiding += 1
        return self.__counter_hiding

h = Hello()
print(h.count())

# print(h.__counter_hiding)
print(h._Hello__counter_hiding)
