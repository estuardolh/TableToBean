class Table:
  field_list=[]
  name=''

  def __init__(self, name):
    self.name = name
    self.field_list = []

  def addField(self, field):
    self.field_list.append(field)

  def setFields(self, field_list):
    fields = field_list

  def getGlobalVars(self):
    res = ''
    first_declare = True
    for field in self.field_list:
      res += ('  ' if first_declare == True else '\n  ')+field.getDeclare()
      first_declare = False
    return res

  def getInitializerConstructor(self):
    res = ''
    res += '  public '+self.name+'('
    field_count = 1
    field_list_lenght = len(self.field_list)
    for field in self.field_list:
      res += field.type+' '+field.name+(',' if field_list_lenght > 1 and field_count < field_list_lenght else '){\n')
      field_count += 1
    res += '\n  }'
    return res

  def getFieldsToMethods(self):
    res = ''
    first_method = True
    for field in self.field_list:
      res += ('  ' if first_method == True else '\n  ')+field.getGetter()
      res += '\n  '+field.getSetter()

      first_method = False
    return res

  def toClass(self):
    return "public class "+self.name+" {\n"+self.getGlobalVars()+'\n\n'+self.getInitializerConstructor()+'\n\n'+self.getFieldsToMethods()+"\n}\n"
