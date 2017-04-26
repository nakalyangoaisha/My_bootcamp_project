from app.person import Person


class Fellow(Person):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.person_name = name
        position = 'Fellow'
