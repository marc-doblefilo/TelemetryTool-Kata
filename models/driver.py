class Driver:

    def __init__(self, name: str, number: int):

        self.name = name
        self.number = number

    def changeNumber(self, newNumber: int):
        self.number = newNumber
