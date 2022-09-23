class Dog ():

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog_1 = Dog(name="Hans", breed="German Shepherd")
dog_2 = Dog(name="Lou", breed="Labrador")

print(f'{dog_1.name} and {dog_2.name} are friends')
