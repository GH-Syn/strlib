class InvalidCharacter(Exception):
    def __init__(self, char):
        super().__init__(char)
        self.char = char
