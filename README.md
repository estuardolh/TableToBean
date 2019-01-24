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

Input file:
```
'CAT','ID_CAT','VARCHAR2'
'CAT','AGE','NUMBER'
```

Execution:
```
python TableToBean.py input.csv
```

Output:
```
public class Cat {
  private String id_cat = "";
  private long age = 0;

  public Cat(String id_cat, long age){
    this.id_cat = id_cat;
    this.age = age;
  }

  public String getIdCat(){
    return this.id_cat;
  }

  public void setIdCat(String id_cat){
    this.id_cat = id_cat;
  }

  public long getAge(){
    return this.age;
  }

  public void setAge(long age){
    this.age = age;
  }
}
```

### Requirements for Ubuntu

On terminal execute:
```
  pip install cx_Oracle
  pip install configparser
  
  sudo apt-get install libaio1
  sudo apt-get install libaio-dev
```

And then follow [this instructions](https://oracle.github.io/odpi/doc/installation.html#linux) from Oracle docs.
