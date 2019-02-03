# TableToBean
Reads CSV file export from Oracle all_tab_columns table to generate Java Beans.

**USAGE**:

```
python TableToBean.py <CSV input file>
```

For configuration variables see ```config.ini``` file.

### Configurable
- Global variables format(lowercase | camelcase)
- Global variables inicialization
- Set parent class (extends)
- Identation
- Java type per Oracle Data type
- Generate comments for getter/setter
- Generate empty constructor(no parameters)
- Generate constructor initializer

CSV input file content could be generated as follow:

```
SELECT ''''||table_name||''','''||column_name||''','''||data_type||''','''||data_length||''','''||comments||''''
FROM all_tab_columns NATURAL JOIN all_col_comments
ORDER BY table_name, column_id;
```

Notes:
  - Fields order is: Table name, Column name, Oracle Data type.
  - Sorted by Table name is mandatory.
  - It hasn't column's header.
  - Values must be quoted by single quote mark.

### Example:

CSV input file:
```
'CAT','ID_CAT','VARCHAR2','7','Cat identification'
'CAT','AGE','NUMBER','2','how old is cat?'
'CAT','SIZE','CHAR','2','S/M/XL'
```

Execution:
```
python TableToBean.py input.csv
```

Output:
```
public class Cat {
	private String id_cat;
	private String age;
	private String size;

	public Cat(String id_cat, String age, String size){
		this.id_cat = id_cat;
		this.age = age;
		this.size = size;
	}

	/**
	 * Cat identification
	 */
	public String getIdCat(){
		return this.id_cat;
	}

	/**
	 * Cat identification
	 */
	public void setIdCat(String id_cat){
		this.id_cat = id_cat;
	}

	/**
	 * how old is cat?
	 */
	public String getAge(){
		return this.age;
	}

	/**
	 * how old is cat?
	 */
	public void setAge(String age){
		this.age = age;
	}

	/**
	 * S/M/XL
	 */
	public String getSize(){
		return this.size;
	}

	/**
	 * S/M/XL
	 */
	public void setSize(String size){
		this.size = size;
	}
}
```

### Requirements for Ubuntu:

On terminal execute:
```
  pip install cx_Oracle
  pip install configparser
  
  sudo apt-get install libaio1
  sudo apt-get install libaio-dev
```

And then follow [this instructions](https://oracle.github.io/odpi/doc/installation.html#linux) from Oracle docs.



Contributions are welcome.
