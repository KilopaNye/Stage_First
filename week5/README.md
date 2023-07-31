###要求三:

```sql
mysql>  insert into member (name,username,password) value ('李四','aba321','aba321');
Query OK, 1 row affected (0.01 sec)

mysql>  insert into member (name,username,password) value ('小二','aba565','aba565');
Query OK, 1 row affected (0.00 sec)

mysql>  insert into member (name,username,password) value ('大一','aba878','aba878');
Query OK, 1 row affected (0.00 sec)

SELECT * FROM member;
```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/7bd87b24-17b5-4730-8315-496efa2a3a7b)


由近到遠排序:

```sql
mysql> select * from member order by time desc;
```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/a42ed2dc-09ce-48ed-ae6b-dd4d49712dbd)


取得排序後的指定範圍資料:

```sql
mysql> select * from member order by time desc limit 1,4;
```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/ee9f9229-d8c0-4fad-ba01-41e2c9671ea0)


取得username為’test’的資料:

```sql
mysql> select * from member where username='test';
```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/5c50c537-3179-4143-8599-d3394d794d9f)


取得username為’test’ 且 password為’test’的資料:

```sql
mysql> select * from member where username='test' and password='test';
```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/c6bbde89-58f1-4e5d-9fa1-db1b0234328f)


修改username為test的資料名稱 name=test2

```sql
mysql> update member set name='test2' where username='test';
```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/5889e840-cfba-47db-b543-5abd74132c7e)


---

### 要求四:
取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```sql
mysql> SELECT count(*) from member;
```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/7908d0ce-07af-4104-bab9-1102972bd1b7)


取得 member 資料表中，所有會員 follower_count 欄位的總和。

```sql
mysql> select sum(follower_count) as 總和 from member;

```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/5f0c7bd4-7bfd-4d1f-bce9-533ad8252968)


取得 member 資料表中，所有會員 follower_count 欄位的平均數。

```sql
mysql> select avg(follower_count) as 平均 from member;
```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/c654fd39-dcc0-4883-a316-6c3d80d69f03)


---

### 要求五:

範例資料:

```sql
mysql> CREATE TABLE message(
	  id bigint primary key auto_increment,
    member_id bigint not null,
    content VARCHAR(255) not null,
    like_count int unsigned default '0' not null ,
    time DATETIME NOT NULL DEFAULT NOW()
);
```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/d7e39953-a03e-40dd-83e3-12feef83cdf8)


使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者的姓名。

```sql
mysql> select name,content from member inner join message on member.id=message.member_id;
```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/5daddfe5-1038-48e3-a78c-6d89be539ebf)


使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有
留⾔，資料中須包含留⾔者的姓名。

```sql
mysql> select name,content from member inner join message on member.id=message.member_id where username='test';
```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/b641635b-4130-477d-8612-ab88975ae59c)


使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中
欄位 username 是 test 的所有留⾔平均按讚數。

```sql
mysql> select name,avg(like_count) as 留言平均按讚數 from member inner join message on member.id=message.member_id where username='test' group by message.member_id;
```

![image](https://github.com/KilopaNye/Stage_First/assets/98875404/90d4b566-788a-4bcd-b87c-568cfe527e04)

