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

  def fieldsToMethods(self):
    res = ''
    first_method = True
    for method in self.field_list:
      res += ('  ' if first_method == True else '\n  ')+method.getGetter()
      first_method = False
    return res

  def toClass(self):
    return "public class "+self.name+"{\n"+self.fieldsToMethods()+"\n}\n"
