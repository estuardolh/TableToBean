# TableToBean
Reads database tables CSV export and generate Java Beans.

**USAGE**:

```
python TableToBean.py <CSV input file>
```

```config.ini``` contains configuration variables.

CSV input file content could be generated as follow:

```
select ''''||table_name||''','''||column_name||''','''||data_type||''''
from all_tab_columns
order by table_name, column_id;
```

Notes:
  - Fields order is: Table name, Column name, Oracle Data type.
  - Sorted by Table name is mandatory.
  - It hasn't column's header.
  - Values must be quoted by single quote mark.

### Example

CSV input file
```
'CAT','ID_CAT','VARCHAR2'
'CAT','AGE','NUMBER'
```

### Requirements for Ubuntu

on terminal execute:
```
  pip install cx_Oracle
  pip install configparser
  
  sudo apt-get install libaio1
  sudo apt-get install libaio-dev
```

And then follow [this instructions] from Oracle docs.(https://oracle.github.io/odpi/doc/installation.html#linux)
