class Table:
  field_list=[]
  name=''
  parent_class=''

  def __init__(self, name):
    self.name = name
    self.field_list = []

  def addField(self, field):
    self.field_list.append(field)

  def setFields(self, field_list):
    fields = field_list

  def getGlobalVars(self, initialize_global_variables, identation):
    res = ''
    first_declare = True
    for field in self.field_list:
      res += (identation if first_declare == True else '\n'+identation)+field.getDeclare(initialize_global_variables)
      first_declare = False
    return res

  def getInitializerConstructor(self, identation):
    res = ''
    res += identation+'public '+self.name+'('
    field_count = 1
    field_list_lenght = len(self.field_list)
    constructor_parameters = ''
    constructor_inits = ''
    for field in self.field_list:
      constructor_parameters += field.type+' '+field.name+(', ' if field_list_lenght > 1 and field_count < field_list_lenght else '){')
      constructor_inits += identation+identation+'this.'+field.name+' = '+field.name+';'+('\n' if field_list_lenght > 1 and field_count < field_list_lenght else '')
      field_count += 1

    res += constructor_parameters
    res += '\n'+constructor_inits
    res += '\n'+identation+'}'
    return res

  def getFieldsToMethods(self, identation):
    res = ''
    first_method = True
    for field in self.field_list:
      res += (identation if first_method == True else '\n\n'+identation)+field.getGetter(identation)
      res += '\n\n'+identation+field.getSetter(identation)

      first_method = False
    return res

  def toClass(self, initialize_global_variables, identation):
    return "public class "+self.name+(" extends "+self.parent_class if len(self.parent_class) > 0 else "")+" {\n"+self.getGlobalVars(initialize_global_variables, identation)+'\n\n'+self.getInitializerConstructor(identation)+'\n\n'+self.getFieldsToMethods(identation)+"\n}\n"

  def getTableName(self):
    return self.name

  def setParentClass(self, parent_class):
    self.parent_class = parent_class
