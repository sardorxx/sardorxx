class Animal:
    def __init__(self, _speacies, _type, _name, __age):
        self._speacies = _speacies
        self._type = _type
        self._name = _name
        self.__age = __age

    def count_animal_num(self):
        count = 0
        for i in self._type:
            count += 1
            return count


class Cat:
    def __init__(self, speacie, gender, a, b):
        self.gender = gender
        self.speacie = speacie
        self.a = a
        self.b = b

    def get_gender(self):
        return self.gender

    def adds(self):
        return self.a + self.b

animal = Animal('Mam', 'Monkey, Cow, Cat', 'John', 9)
animals = Cat('Meal', 'Male', 4, 9)
print(animal._speacies)
print(animal._type)
print(animal._name)
# print(animal.__age)
print(animal.count_animal_num())
print(animals.gender)
print(animals.adds())
