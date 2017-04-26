from app.person import Person


class Staff(Person):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.name = name
        position = 'Staff'
