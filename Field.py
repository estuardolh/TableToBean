from FieldFormat import FieldFormat

class Field:
  TYPE_JAVA_STRING = 'String'
  TYPE_JAVA_LONG = 'long'

  name=''
  type=''

  def __init__(self, name, type):
    self.name = name
    self.type = type

  def getGetter(self):
    return 'public '+self.type+' get'+FieldFormat.getCamelCase(self.name, True)+'(){\n    return this.'+self.name+';\n  }'

  def getSetter(self):
    return 'public void set'+FieldFormat.getCamelCase(self.name, True)+'('+self.type+' '+self.name+'){\n    this.'+self.name+' = '+self.name+';\n  }'

  def getInitValueByJavaType(self, type):
    res = ''
    if(type == Field.TYPE_JAVA_STRING):
      res = '""'
    elif (type == Field.TYPE_JAVA_LONG):
      res = '0'
    return res

  def getDeclare(self):
    return 'private '+self.type+' '+self.name+' = '+self.getInitValueByJavaType(self.type)+';'
