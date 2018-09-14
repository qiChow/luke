# coding=utf-8

import mysql.connector

class DB():
    def connetcdb(self):
        print("连接到mysql数据库...")

        db = mysql.connector.connect(user="root", passwd="luke@shopee", database="blackword", use_unicode=True)

        print('恭喜！数据库已连上')

        return db

    def createtable(db):
        # 使用cursor（）方法获取操作游标
        cursor = db.cursor()

        cursor.execute("DROP TABLE IF EXISTS blacklist_word")
        sql = """CREATE TABLE IF NOT EXISTS `blacklist_word`(
              `id` INT UNSIGNED AUTO_INCREMENT,
              `word` VARCHAR(100) NOT NULL,
              `creator` VARCHAR(40) NOT NULL,
              `create_time` DATE NOT NULL,
              PRIMARY KEY ( `id` ))ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

        cursor.execute(sql)

    def insertdb(db):
        cursor = db.cursor()

        sql = """INSERT INTO 
    
              blacklist_word(word,creator,create_time) 
    
              VALUES
    
              ('pig','zhangsan',now()),
    
              ('dog','lisi',now());"""

        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("插入数据失败！")
            db.rollback()

    def querydb(db):
        cursor = db.cursor()

        sql = "SELECT * FROM blacklist_word"

        dict = {}
        blacklist_words = []

        try:
            cursor.execute(sql)

            results = cursor.fetchall()

            for row in results:
                dict["word"] = row[1]
                dict["creator"] = row[2]
                dict["creator"] = row[3]
                blacklist_words.append(dict)
            return blacklist_words
        except:
            print("获取数据库中数据失败")

    def deletedb(db):
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 删除语句
        sql = "DELETE FROM blacklist_word WHERE id = '%d'" % (3)

        try:
           # 执行SQL语句
           cursor.execute(sql)
           # 提交修改
           db.commit()
        except:
            print('删除数据失败!')
            # 发生错误时回滚
            db.rollback()

    def updatedb(db):
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 更新语句
        sql = "UPDATE blacklist_word SET word = bitch WHERE id = '%d'" % (2)

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            print('更新数据失败!')
            # 发生错误时回滚
            db.rollback()

    def closedb(db):
        db.close()

