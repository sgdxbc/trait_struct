from trait_struct import trait, trait_, struct


@trait_
class ExcitedSwitch:
    def __init__(self):
        self.is_excited: bool


@trait(ExcitedSwitch)
class Greetings:
    def greetings(self) -> str:
        if self.is_excited:
            return "Hello!"
        else:
            return "Hello."


@trait_
class AlwaysExcited(ExcitedSwitch):
    def __init__(self):
        self.is_excited = True
        super().__init__()


@struct
class ExcitedPerson(AlwaysExcited, Greetings):
    def __init__(self, name):
        self.name = name
        super().__init__()


cowsay = ExcitedPerson("cowsay")
print(cowsay.greetings())
