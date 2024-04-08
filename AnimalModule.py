class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def animal_name(self):
        return f"Животное зовут {self.name}"

    def animal_type(self):
        return f"Животное принадлежит к виду {self.type}"