import sys

class Field:
  name=''
  type=''

  def __init__(self, name, type):
    self.name = name
    self.type = type

  def getGetter(self):
    return 'public String get'+self.name+'(){ return this.'+self.name+'; }'

class Table:
  field_list=[]
  name=''

  def __init__(self, name):
    self.name = name

  def addField(self, field):
    self.field_list.append(field)

  def setFields(self, field_list):
    fields = field_list

  def fieldsToMethods(self):
    res = ''
    for method in self.field_list:
      res += '\n'+method.getGetter()
    return res

  def toClass(self):
    return "public class "+self.name+"{\n"+self.fieldsToMethods()+"\n}\n"



def getClassBegin(class_name):
  return "public class "+class_name+"{"

def getMethod(field_name, field_type):
  field_name_camel_case='c'+field_name+'c'
  if(field_type=="'VARCHAR2'"):
    return '  public String get'+field_name_camel_case+'(){\n    return this.'+field_name+';\n  }'
  elif(field_type=="'NUMBER'"):
    return '  public long get'+field_name_camel_case+'(){\n    return this.'+field_name+';\n  }'
  return ''

def getClassEnd():
  return "}"

debug = True

INPUT_NUMBER_OF_COLUMNS = 2

COLUMN_INDEX_TABLE_NAME = 0
COLUMN_INDEX_FIELD_NAME = 1
COLUMN_INDEX_FIELD_TYPE = 2

if(len(sys.argv) == 1):
  print "no input file path specified."
  exit(0)

input_file_path=sys.argv[1]

input_file = open(input_file_path, "r")


current_table_name = ''
first_class = True

line_count = 1

table_list = []

a_table = Table('')

for line in input_file:
  if( len(line.strip()) < INPUT_NUMBER_OF_COLUMNS ):
    print "each line should have 3 columns. line "+str(line_count)+" skipped."
  else:
    csv_columns = line.strip().split(",")

    table_name = csv_columns[COLUMN_INDEX_TABLE_NAME]
    field_name = csv_columns[COLUMN_INDEX_FIELD_NAME]
    field_type = csv_columns[COLUMN_INDEX_FIELD_TYPE]

    if(current_table_name != table_name):
      if(not first_class):
        table_list.append(a_table)
      a_table = Table(table_name)

    a_table.addField(Field(field_name, field_type))

    if(first_class):
      current_table_name = table_name
      first_class = False

    table_list.append(a_table)
    a_table = Table('')

  line_count += 1

print "Tables collected: "+str(len(table_list))

for tab in table_list:
  print tab.toClass()
