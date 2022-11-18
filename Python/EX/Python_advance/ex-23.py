class Dog():

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def calculate_human_age(self):
        return self.age * 7


dog_1 = Dog("Hans", "German Shepherd", 7)

print(dog_1.age)
print(dog_1.calculate_human_age())
