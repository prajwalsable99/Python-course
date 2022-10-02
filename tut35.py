# multiple inheritance

class landanimal:
    a="i can live on land "

class aquaticanimal:
    b ="i can live in water "


class amphibian(landanimal,aquaticanimal):
    def amphi(self):
        return f"{self.a} and {self.b} , so i am amphibian "


frog=amphibian()
print(frog.amphi())

