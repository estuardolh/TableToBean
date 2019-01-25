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

  def getGlobalVars(self, initialize_global_variables):
    res = ''
    first_declare = True
    for field in self.field_list:
      res += ('  ' if first_declare == True else '\n  ')+field.getDeclare(initialize_global_variables)
      first_declare = False
    return res

  def getInitializerConstructor(self):
    res = ''
    res += '  public '+self.name+'('
    field_count = 1
    field_list_lenght = len(self.field_list)
    constructor_parameters = ''
    constructor_inits = ''
    for field in self.field_list:
      constructor_parameters += field.type+' '+field.name+(', ' if field_list_lenght > 1 and field_count < field_list_lenght else '){')
      constructor_inits += '    this.'+field.name+' = '+field.name+';'+('\n' if field_list_lenght > 1 and field_count < field_list_lenght else '')
      field_count += 1

    res += constructor_parameters
    res += '\n'+constructor_inits
    res += '\n  }'
    return res

  def getFieldsToMethods(self):
    res = ''
    first_method = True
    for field in self.field_list:
      res += ('  ' if first_method == True else '\n\n  ')+field.getGetter()
      res += '\n\n  '+field.getSetter()

      first_method = False
    return res

  def toClass(self, initialize_global_variables):
    return "public class "+self.name+" {\n"+self.getGlobalVars(initialize_global_variables)+'\n\n'+self.getInitializerConstructor()+'\n\n'+self.getFieldsToMethods()+"\n}\n"

  def getTableName(self):
    return self.name
