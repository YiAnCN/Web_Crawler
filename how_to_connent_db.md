首先在同目录下创建一个 .py 文件，用来配置文件

例如:配置文件名为 config.py，main文件名为 toutiao.py
     

- 在 config.py 中配置数据库

  ```python
  MONGO_URL = 'localhost'      # 链接地址为本地 localhost
  MONGO_DB = 'toutiao'         # 数据库名称
  MONGO_TABLE = 'toutiao'      # 表单名称
  ```

  

- 然后在 toutiao.py 中添加此配置文件`from config import *`

  

- 在 python 中操作 mongodb 数据库

  ```python
  import pymongo
  client = pymongo.MongoClient(MONGO_URL, connect=False)
  db = client[MONGO_DB]
  
  def save_to_mongo(result):
  	# result 注意是一个字典形式
  	if db[MONGO_TABLE].insert(result):
      	print('Successfully Saved to Mongo', result)
      	return True
  	return False
  
  save_to_mongo()
  ```

  

- 在 python 中操作 mysql 数据库

  ```python
  import pymysql
  db = pymysql.connect("localhost","root","654321","mysql" )
  cursor = db.cursor()
  def insert_info(result):
      sql = "INSERT INTO MONGO_TABLE() VALUES(result)"
      print(sql)
      cursor.execute(sql)
      db.commit()
  ```

  

