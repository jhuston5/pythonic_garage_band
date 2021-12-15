from re import M

class Band:
    def __init__(self, name="Unknown", members=[]):
        self.name = name
        self.members = members
    # play_solos():
    # def to_list():

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician(Band):
  # def play_solo
    pass

class Guitarist(Musician):
    def __init__(self, name='Unknown'):
      self.name = name

    def __str__(self):
      return f'My name is {self.name} and I play guitar'

    def __repr__(self):
      return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
      return 'guitar'

    def play_solo(self):
      return 'face melting guitar solo'
    pass

class Drummer(Musician):
    def __init__(self, name="Unknown"):
      self.name = name
    
    def __str__(self):
      return f'My name is {self.name} and I play drums'
    
    def __repr__(self):
      return f'Drummer instance. Name = {self.name}'

    def get_instrument(self):
      return 'drums'

    def play_solo(self):
      return 'rattle boom crash'
    pass

class Bassist(Musician):
    def __init__(self, name="Unknown"):
      self.name = name
    
    def __str__(self):
      return f'My name is {self.name} and I play bass'

    def __repr__(self):
      return f'Bassist instance. Name = {self.name}'

    def get_instrument(self):
      return 'bass'

    def play_solo(self):
      return 'bom bom buh bom'
    pass