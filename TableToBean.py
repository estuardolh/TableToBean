import sys
import configparser

from Table import Table
from Field import Field
from FieldFormat import FieldFormat

configuration = configparser.ConfigParser()
configuration.read('config.ini')

database_type_dictionary = configuration['main']['database_type_dictionary']
database_types = configuration[database_type_dictionary]

parent_class = configuration['main']['parent_class']
identation_string = configuration['main']['identation']

def removeSingleQuoteMark(text):
  return text.replace("'","")

def getJavaTypeByOracleFieldType(oracle_field_type):
  return database_types[oracle_field_type]

INPUT_NUMBER_OF_COLUMNS = 3

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

    table_name = FieldFormat.getCamelCase(removeSingleQuoteMark(csv_columns[COLUMN_INDEX_TABLE_NAME]), True)

    field_name = removeSingleQuoteMark(csv_columns[COLUMN_INDEX_FIELD_NAME])
    field_name_camel_case = FieldFormat.getCamelCase(field_name)
    field_name_lowercase = field_name.lower()

    if(configuration['main']['global_variables_camelcase']=='True'):
      field_name = field_name_camel_case
    else:
      field_name = field_name_lowercase

    field_type = getJavaTypeByOracleFieldType(removeSingleQuoteMark(csv_columns[COLUMN_INDEX_FIELD_TYPE]))
    
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
    
    a_table.addField(Field(field_name, field_type))
  line_count += 1
table_list.append(a_table)

print "Java files to generate: "+str(len(table_list))

initialize_global_variables = configuration['main']['global_variables_inicialization']

identation = removeSingleQuoteMark(identation_string)

for table in table_list:
  generated_file_path = "./output/"+table.getTableName()+".java"
  file = open(generated_file_path, "w+")
  file.write(table.toClass(True if initialize_global_variables == 'True' else False, identation))
  file.close()
  print "  - file "+generated_file_path+' generated.'
