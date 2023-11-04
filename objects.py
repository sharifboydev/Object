class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

    def set_bosqich(self, bosqich):
        self.bosqich = bosqich

    def get_update(self):
        self.bosqich += 1

    def get_name(self):
        return self.ism

    def get_lastname(self):
        return self.familiya

    def get_fullname(self):
        return f"{self.ism} {self.familiya}"

    def get_age(self,yil):
        return yil-self.tyil


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_name(self):
        return self.nomi

    def get_students(self):
        return [x.get_info for x in self.talabalar]

    def get_students_num(self):
        return self.talabalar_soni

    # def get_stdents(self):
# return [talaba1.get_info() for talaba in self.talabalar]


# matematika = Fan("Oliy matematika")
# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# talaba2 = Talaba("Hasan", "Alimov", 2001)
# talaba3 = Talaba("Akrom", "Boriyev", 2002)
#
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

mat_talabalar = matematika.get_stdents()
print(mat_talabalar)

# print(matematika.talabalar_soni)
# print(matematika.talabalar)


# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# talaba1.get_update()
# print(talaba1.get_info())
#
# talaba1.get_update()
# print(talaba1.get_info())
#
# talaba1.get_update()
# print(talaba1.get_info())
#
# # talaba1.set_bosqich(3)
# # print(talaba1.get_info())
#
# # talaba1.bosqich = 2
# # print(talaba1.bosqich)
