from pymysql import *

class Mysqlpython:
    def __init__(self, database , host  , user  , password  , port):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.port = port

    # 创建数据连接和游标对象
    def open(self):
        self.db = connect(host=self.host,
                          user=self.user,
                          password=self.password,
                          port=self.port,
                          database=self.database,
                          charset="utf8")
        self.cur = self.db.cursor()

    # 关闭游标对象和数据库连接对象
    def close(self):
        self.cur.close()
        self.db.close()

    # 执行sql命令
    def executesql(self, sql, L=[]):
        self.open()

        self.cur.execute(sql, L)
        self.db.commit()

        self.close()
    # 批量执行sql命令
    def executesqlmany(self, sql, L=[]):
        self.open()

        self.cur.executemany(sql, L)
        self.db.commit()
        self.close()


    # 查询功能
    def querysql_all(self, sql, L=[]):
        self.open()
        self.cur.execute(sql, L)
        # fecthall 返回的是多维元组
        result = self.cur.fetchall()
        return result

    def query_all(self, sql, L=[]):
        result = []
        self.open()
        for lx in L:
            self.cur.execute(sql, lx)
        # fecthall 返回的是多维元组
            res = self.cur.fetchall()
            result.append(res)

        return result

    def querysql_one(self, sql, L=[]):
        self.open()
        self.cur.execute(sql, L)
        # fecthall 返回的是多维元组
        result = self.cur.fetchone()
        return result
if __name__ == "__main__":
    sqlh = Mysqlpython()
    arr =[]
    ins = " select 1+1 from dua;"
    r =sqlh.querysql(ins, [])
    print(r[0])
