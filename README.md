# TableToBean
Connects to an Oracle database and generate Java Beans.

**USAGE**:

```
python TableToBean.py <CSV input file>
```

Where CSV input file is output of the next query:

```
select ''''||table_name||''','''||column_name||''','''||data_type||''''
from all_tab_columns
order by column_id;
```

Notes:

  - ```Order By column_id``` is mandatory.

  - It hasn't column's header

###Example

CSV input file
```
'CAT','ID_CAT','VARCHAR2'
'CAT','AGE','NUMBER'
```

###Requirements for Ubuntu

From pip:
  
  - cx_Oracle

From apt:
  
  - libaio1
  - libaio-dev
  
From Oracle:
  
  - https://oracle.github.io/odpi/doc/installation.html#linux
