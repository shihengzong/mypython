# -*- coding: UTF-8 -*-

# 数据库连接
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("192.168.237.135",
                     "root",
                     "123456",
                     "zsh_database",
                     charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)

# 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# # 创建数据表SQL语句
# sql = """CREATE TABLE EMPLOYEE (
#          ID INT not null auto_increment PRIMARY KEY,
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""

# cursor.execute(sql)

# # SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 8000),
#                 ('Jane', 'jacy', 18, 'N', 3000)
#       """
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()

# SQL 查询语句
sql = "SELECT * FROM zsh_article \
       WHERE id > %s" % 1
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    res_key = ("id", "title", "content", "is_use")
    list_res = []
    for row in results:
        # for elem in row:
        one_of_list = dict(zip(res_key, row))
        # one_of_list['id'] = row[0]
        # one_of_list['title'] = row[1]
        # one_of_list['content'] = row[2]
        # one_of_list['is_use'] = row[3]
        list_res.append(one_of_list)
    #   print(one_of_list)
    print(list_res)
except:
    print("Error: unable to fecth data")

# # SQL 更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()

# 关闭数据库连接
db.close()