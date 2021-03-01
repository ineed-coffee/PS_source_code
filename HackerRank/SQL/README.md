# SQL Grammar

---

### `Modulation`

```mysql
SELECT *
FROM TABLE_NAME
WHERE FIELD%NUM=REMAIN;
```

​		

### `Unique value` 

```mysql
SELECT DISTINCT(FIELD_NAME)
FROM TABLE_NAME;
```

​	

### `Counting` 

```mysql
SELECT COUNT(FIELD_NAME)
FROM TABLE_NAME;
```

​	

### `Length of string` 

```mysql
SELECT LENGTH(FIELD_NAME)
FROM TABLE_NAME;
```

​	

### `Sort`

```mysql
SELECT FEILD1
FROM TABLE_NAME
ORDER BY FIELD2 ASC , FIELD3 DESC....;
```

​	

### `Limiting rows` 

```mysql
SELECT FIELD_NAME
FROM TABLE_NAME
LIMIT ROW_CNT;
```

​	

### `Connecting queries`

```mysql
(SELECT FIELD_NAME
FROM TABLE_NAME)
UNION
(SELECT FIELD_NAME
FROM TABLE_NAME);
```

​	

### `Substring` 

```mysql
SELECT LEFT("HELLO",1);
SELECT RIGHT("HELLO",1);
SELECT SUBSTR("HELLO",3,1);
```

​	

### `Regular Expression` 

```mysql
SELECT *
FROM TABLE_NAME
WHERE FIELD REGEXP "^[A-Z]+.*[0-1]$";
```

​	

### `CASE`

```mysql
SELECT
    CASE
        WHEN CONDITION1 THEN RETURN1
        WHEN CONDITION2 THEN RETURN2
        WHEN CONDITION3 THEN RETURN3
        ELSE RETURN4
    END AS CUSTOM_NAME
FROM TABLE_NAME;
```

​	

### `String concatenation`

```mysql
SELECT CONCAT(STR1,STR2)
FROM TABLE_NAME;
```

