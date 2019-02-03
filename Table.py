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

  def getEmptyConstructor(self, identation):
    res = ''
    res += identation + 'public '+self.name+'(){\n'
    res += identation + '}'
    return res

  def getConstructorInitializer(self, identation):
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

  def getFieldsToMethods(self, identation, show_getter_comment, show_setter_comment):
    res = ''
    first_method = True
    for field in self.field_list:
      res += ('' if first_method == True else '\n\n')
      res += identation + field.getJavaComment(identation) if show_getter_comment else ''
      res += identation + field.getGetter(identation)

      res += '\n\n'
      res += identation + field.getJavaComment(identation) if show_setter_comment else ''
      res += identation + field.getSetter(identation)

      first_method = False
    return res

  def toClass(self, initialize_global_variables, identation, show_getter_comment, show_setter_comment, generate_empty_constructor, generate_constructor_initializer):
    a_class = "public class "+self.name+(" extends "+self.parent_class if len(self.parent_class) > 0 else "")
    a_class += " {\n"+self.getGlobalVars(initialize_global_variables, identation)
    a_class += '\n\n'+self.getEmptyConstructor(identation) if generate_empty_constructor else ''
    a_class += '\n\n'+self.getConstructorInitializer(identation) if generate_constructor_initializer else ''
    a_class += '\n\n'+self.getFieldsToMethods(identation, show_getter_comment, show_setter_comment)+"\n}\n"

    return a_class

  def getTableName(self):
    return self.name

  def setParentClass(self, parent_class):
    self.parent_class = parent_class
