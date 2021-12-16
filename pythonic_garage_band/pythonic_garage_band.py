from re import M
class Band:
    # empty list of bands for storing instances called in init function
    bands = []
    count = 0
    def __init__(self, name="", members=[]):
        self.name = name
        self.members = members
        Band.count += 1
        # check if band is already in the bands list, if not, then append the band name
        if name not in Band.bands:
          Band.bands.append(name)


    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        print(type(self.members))
        return f"Band instance. name={self.name}, members={self.members}"


    def play_solos(self):
      musician_solo = []
      for i in self.members:
        print(i, 'No type error')
        musician_solo.append(str(i.play_solo()))
      print(musician_solo)
      return(musician_solo)


    @classmethod
    def to_list(cls):
      print(cls.bands)
      return cls.bands


class Musician(Band):
  # def play_solo
  pass


# Instances of Musician
class Guitarist(Musician):
    def __init__(self, name="Unknown"):
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