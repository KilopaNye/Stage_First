要求三:

```sql
mysql>  insert into member (name,username,password) value ('李四','aba321','aba321');
Query OK, 1 row affected (0.01 sec)

mysql>  insert into member (name,username,password) value ('小二','aba565','aba565');
Query OK, 1 row affected (0.00 sec)

mysql>  insert into member (name,username,password) value ('大一','aba878','aba878');
Query OK, 1 row affected (0.00 sec)

SELECT * FROM member;
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/afb54de2-12f7-46c3-bc6c-a7266c9959c0/Untitled.png)

由近到遠排序:

```sql
mysql> select * from member order by time desc;
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cfc31cd3-5125-4857-b079-e0015d57e3a4/Untitled.png)

取得排序後的指定範圍資料:

```sql
mysql> select * from member order by time desc limit 1,4;
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/be400602-2c91-404b-b4b7-139b3a0b09d3/Untitled.png)

取得username為’test’的資料:

```sql
mysql> select * from member where username='test';
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dedd2ef7-2b22-4f69-ade6-0fde50ed29cc/Untitled.png)

取得username為’test’ 且 password為’test’的資料:

```sql
mysql> select * from member where username='test' and password='test';
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9c2a4cc3-61e6-4b29-a203-81ec053b1082/Untitled.png)

修改username為test的資料名稱 name=test2

```sql
mysql> update member set name='test2' where username='test';
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65507d6b-ac93-48ee-b01b-598543fa41dd/Untitled.png)

---

### 要求四:

```sql
mysql> SELECT count(*) from member;
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/adcb1d12-c45a-456a-8b0e-67c7aca72ba7/Untitled.png)

取得 member 資料表中，所有會員 follower_count 欄位的總和。

```sql
mysql> select sum(follower_count) as 總和 from member;

```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ea6e9ed6-cbaa-4bea-9ba9-d1ae900dc1f8/Untitled.png)

取得 member 資料表中，所有會員 follower_count 欄位的平均數。

```sql
mysql> select avg(follower_count) as 平均 from member;
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ac996ca4-3637-47dc-a904-52313fe16cb5/Untitled.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8227d92c-8a69-417c-9b4b-da1bd48773f9/Untitled.png)

使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者的姓名。

```sql
mysql> select name,content from member inner join message on member.id=message.member_id;
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc64ebbd-cceb-4f36-871e-308c83c7e476/Untitled.png)

使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有
留⾔，資料中須包含留⾔者的姓名。

```sql
mysql> select name,content from member inner join message on member.id=message.member_id where username='test';
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f5fde6c-b2cc-4165-9f11-c21b26f1fe37/Untitled.png)

使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中
欄位 username 是 test 的所有留⾔平均按讚數。

```sql
mysql> select name,avg(like_count) as 留言平均按讚數 from member inner join message on member.id=message.member_id where username='test' group by message.member_id;
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bf2252b0-d4cd-40ed-aac9-d0c802ba9d13/Untitled.png)
