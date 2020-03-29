import os
import sys
import configparser

from Table import Table
from Field import Field
from FieldFormat import FieldFormat

configuration = configparser.ConfigParser()
configuration.read('configuration.ini')

database_type_dictionary = configuration['main']['database_type_dictionary']
database_types = configuration[database_type_dictionary]

parent_class = configuration['main']['parent_class']
identation_string = configuration['main']['identation']

def createDirectoryIfNotExist(directory_name):
  if not os.path.exists(directory_name):
    os.mkdir(directory_name)

def removeSingleQuoteMark(text):
  return text.replace("'","")

def getJavaTypeByOracleFieldType(oracle_field_type):
  return database_types[oracle_field_type]

INPUT_NUMBER_OF_COLUMNS = 3

COLUMN_INDEX_TABLE_NAME = 0
COLUMN_INDEX_FIELD_NAME = 1
COLUMN_INDEX_FIELD_TYPE = 2
COLUMN_INDEX_FIELD_SIZE = 3
COLUMN_INDEX_FIELD_COMMENT = 4

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
  if isinstance(line, str):
    line = line.decode('ascii', 'ignore').encode('ascii')
  elif isinstance(line, unicode):
    line = line.encode('ascii', 'ignore')

  if( len(line.strip()) < INPUT_NUMBER_OF_COLUMNS ):
    print "each line should have 3 columns. line "+str(line_count)+" skipped."
  else:
    csv_columns = line.strip().split(",")

    table_name = FieldFormat.getCamelCase(removeSingleQuoteMark(csv_columns[COLUMN_INDEX_TABLE_NAME]), True)

    field_name = removeSingleQuoteMark(csv_columns[COLUMN_INDEX_FIELD_NAME])
    field_name_camel_case = FieldFormat.getCamelCase(field_name)
    field_name_lowercase = field_name.lower()

    if(True if configuration['main']['global_variables_camelcase'] == 'True' else False):
      field_name = field_name_camel_case
    else:
      field_name = field_name_lowercase

    field_type = getJavaTypeByOracleFieldType(removeSingleQuoteMark(csv_columns[COLUMN_INDEX_FIELD_TYPE]))
    field_size = removeSingleQuoteMark(csv_columns[COLUMN_INDEX_FIELD_SIZE])
    field_comment = removeSingleQuoteMark(csv_columns[COLUMN_INDEX_FIELD_COMMENT])

    if(first_class):
      a_table = Table(table_name)
      a_table.setParentClass(parent_class)
      first_class = False
      current_table_name = table_name
    
    if(current_table_name != table_name):
      table_list.append(a_table)
      a_table = Table(table_name)
      a_table.setParentClass(parent_class)
      
      current_table_name = table_name
    
    a_table.addField(Field(field_name, field_type, field_size, field_comment))
  line_count += 1
table_list.append(a_table)

print "Java files to generate: "+str(len(table_list))

initialize_global_variables = True if configuration['main']['global_variables_inicialization'] == 'True' else False
show_getter_comment = True if configuration['main']['show_getter_comment'] == 'True' else False
show_setter_comment = True if configuration['main']['show_setter_comment'] == 'True' else False
generate_empty_constructor = True if configuration['main']['generate_empty_constructor'] == 'True' else False
generate_constructor_initializer = True if configuration['main']['generate_constructor_initializer'] == 'True' else False
identation = removeSingleQuoteMark(identation_string)

createDirectoryIfNotExist('./output/')

for table in table_list:
  generated_file_path = "./output/"+table.getTableName()+".java"
  file = open(generated_file_path, "w+")
  file.write(table.toClass(initialize_global_variables, identation, show_getter_comment, show_setter_comment, generate_empty_constructor, generate_constructor_initializer))
  file.close()
  print "  - file "+generated_file_path+' generated.'
