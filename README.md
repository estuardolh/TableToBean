# TableToBean
Connects to an Oracle database and generate Java Beans.

**USAGE**:

```
python TableToBean.py <CSV input file>
```

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

From pip:
  
  - cx_Oracle

From apt:
  
  - libaio1
  - libaio-dev
  
From Oracle:
  
  - https://oracle.github.io/odpi/doc/installation.html#linux
