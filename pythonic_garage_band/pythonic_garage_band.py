from re import M

class Band:
    def __init__(self, name="Unknown", members=[]):
        self.name = name
        self.members = members

    # def play_solos():
    # def to_list():

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician:
  # def get_instrument()
  # def play_solo
    pass

class Guitarist:
    pass

class Bassist:
    pass

class Drummer:
    pass