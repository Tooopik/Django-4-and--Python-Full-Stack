class Students():
    def __init__(self, names):
        self.names = names

    def __str__(self):
        return f"{self.names}"

    def __len__(self):
        return len(self.names)


studentList = ["Adrian", "Anna", "Łukasz", "Kacper", "Klaudiusz"]

x = Students(studentList)

print(x)
print(len(x))
