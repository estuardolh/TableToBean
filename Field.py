class Field:
  name=''
  type=''

  def __init__(self, name, type):
    self.name = name
    self.type = type

  def getGetter(self):
    return 'public String get'+self.name+'(){\n    return this.'+self.name+';\n  }'
