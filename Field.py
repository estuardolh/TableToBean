from FieldFormat import FieldFormat

class Field:
  TYPE_JAVA_STRING = 'String'
  TYPE_JAVA_LONG = 'long'

  name=''
  type=''
  size=0
  comment=''

  def __init__(self, name, type, size, comment):
    self.name = name
    self.type = type
    self.size = size
    self.comment = comment

  def getJavaComment(self, identation):
    a_comment = '/**\n'
    a_comment += identation+' * '+self.comment+'\n'
    a_comment += identation+' */\n'
    return a_comment

  def getGetter(self, identation):
    return 'public '+self.type+' get'+FieldFormat.getCamelCase(self.name, True)+'(){\n'+identation+identation+'return this.'+self.name+';\n'+identation+'}'

  def getSetter(self, identation):
    return 'public void set'+FieldFormat.getCamelCase(self.name, True)+'('+self.type+' '+self.name+'){\n'+identation+identation+'this.'+self.name+' = '+self.name+';\n'+identation+'}'

  def getInitValueByJavaType(self, type):
    res = ''
    if(type == Field.TYPE_JAVA_STRING):
      res = '""'
    elif (type == Field.TYPE_JAVA_LONG):
      res = '0'
    return res

  def getDeclare(self, initialize_global_variables):
    return 'private '+self.type+' '+self.name+(' = '+self.getInitValueByJavaType(self.type) if initialize_global_variables == True else '')+';'
