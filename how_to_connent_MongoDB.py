首先在同目录下创建一个 .py 文件，用来配置文件

举例:配置文件名为 config.py
     main文件名为 toutiao.py
     
首先在 config.py 中配置数据库
MONGO_URL = 'localhost'      # 链接地址为本地 localhost
MONGO_DB = 'toutiao'         # 数据库名称
MONGO_TABLE = 'toutiao'      # 表单名称

然后在 toutiao.py 中添加这个库
1. 在 toutiao.py 文件的开头用  from config import * (import * 的意思就是可以把 config 中的所有变量引入进来）

2. import pymongo

3. client = pymongo.MongoClient(MONGO_URL, connect=False)
   db = client[MONGO_DB]
  
以上3步就声明好了这个mongodb数据库对象

接下来定义一个存储到MongoDB的方法：

4. def save_to_mongo(result):                        # result 注意是一个字典形式
    if db[MONGO_TABLE].insert(result):
        print('Successfully Saved to Mongo', result)
        return True
    return False
    
5. 最后在函数中调用一下save_to_mongo这个函数就可以了！
