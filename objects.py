class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich} bosqich talabasi"


talaba1 = Talaba("Alijon", "Valiyev", 2000)
print(talaba1.get_info())
