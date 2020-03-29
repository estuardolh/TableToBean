# TableToBean
Reads CSV and generate Java Beans.

**How to use**:

```
./TableToBean.sh <CSV input file>
```
[Here](input.csv) an input example.

### Available configurations:
- Global variables format(lowercase | camelcase)
- Global variables inicialization
- Set parent class (extends)
- Identation
- Java type per Oracle Data type
- Generate comments for getter/setter
- Generate empty constructor(no parameters)
- Generate constructor initializer
- Generate toJson() method
- Reads Unicode encoding input CSV file

**File index:**

[configuration](/src/configuration.ini), [util query](/src/util-query.sql.ini)
