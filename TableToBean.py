import sys

from Table import Table
from Field import Field

def removeSingleQuoteMark(text):
  return text.replace("'","")

def getJavaTypeByOracleFieldType(oracle_field_type):
  res = ''
  if(oracle_field_type == "VARCHAR2"):
    res = Field.TYPE_JAVA_STRING
  elif(oracle_field_type == "NUMBER"):
    res = Field.TYPE_JAVA_LONG
  else:
    res = Field.TYPE_JAVA_STRING
  return res
  
def getCamelCase(text, first_char_uppered = False):
  res = ''
  
  STATE_PASS = 0
  STATE_UPPER = 2
  
  state = STATE_PASS
  
  first_char_uppered_done = False
  
  for char in text:    
    if(state == STATE_PASS):
      if(char == '_' or
          char == '-' or
          char == ' '):
        # ignore
        state = STATE_UPPER
      else:
        if(first_char_uppered == True and first_char_uppered_done == False):
          res += char.upper()
          first_char_uppered_done = True
        else:
          res += char.lower()
          
    elif(state == STATE_UPPER):
      res += char.upper()
      state = STATE_PASS
      
  return res
  
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

    table_name = getCamelCase(removeSingleQuoteMark(csv_columns[COLUMN_INDEX_TABLE_NAME]), True)
    field_name = getCamelCase(removeSingleQuoteMark(csv_columns[COLUMN_INDEX_FIELD_NAME]), True)
    field_type = getJavaTypeByOracleFieldType(removeSingleQuoteMark(csv_columns[COLUMN_INDEX_FIELD_TYPE]))
    
    if(first_class):
      a_table = Table(table_name)
      first_class = False
      current_table_name = table_name
    
    if(current_table_name != table_name):
      table_list.append(a_table)
      a_table = Table(table_name)
      
      current_table_name = table_name
    
    a_table.addField(Field(field_name, field_type))
  line_count += 1
table_list.append(a_table)

print "Tables collected: "+str(len(table_list))

for tab in table_list:
  print tab.toClass()
