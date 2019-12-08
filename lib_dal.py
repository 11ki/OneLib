# coding=utf-8
import pymssql
import sys
import re


class SQLServer:
    '''
    def __init__(self, server, user, password, database, charset):
        # 类的构造函数，初始化DBC连接信息
        self.server = server
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
    '''
    def __init__(self):
        self.server = '127.0.0.1:1433'
        self.user = 'LibAdmin'
        self.password = '123'
        self.database = 'library'
        self.charset = 'utf8'

    def __GetConnect(self):
        # 得到数据库连接信息，返回conn.cursor()
        if not self.database:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(server=self.server, user=self.user, password=self.password, database=self.database,charset=self.charset)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")  # 将DBC信息赋值给cur
        else:
            return cur

    def ExecQuery(self, table_name, column):
        '''
        执行查询语句
        返回一个包含tuple的list，list是元素的记录行，tuple记录每行的字段数值
        '''
        try:
            cur = self.__GetConnect()
            sql = "select * " + "from " + table_name + " where " + column
            # print(sql)
            cur.execute(sql)  # 执行查询语句
            result = cur.fetchall()  # fetchall()获取查询结果
            # 查询完毕关闭数据库连接
            self.conn.close()
            return result
        except:
            print(sys.exc_info())
            return 0
            # raise

    def ExecInsert(self, table_name, *column):
        try:
            sql = "insert into " + table_name + " values("
            cur = self.__GetConnect()
            for m in column:
                sql = sql + str(m) + ","
            sql = sql[:-1] + ")"
            # print(sql)
            cur.execute(sql)  # 执行查询语句
            self.conn.commit()
            self.conn.close()
        except pymssql.IntegrityError:
            return 2627
        except:
            print(sys.exc_info())

    def ExecDelete(self, table_name, column):
        try:
            cur = self.__GetConnect()
            sql = "delete from " + table_name + " where " + column
            cur.execute(sql)  # 执行查询语句
            # print(sql)
            self.conn.commit()
            self.conn.close()
        except:
            print(sys.exc_info())

    def ExecUpdate(self, table_name, *column):
        try:
            sql = "update " + table_name + " set "
            cur = self.__GetConnect()
            for m in column[:-1]:
                sql = sql + str(m) + ","
            sql = sql[:-1] + " where " + column[-1]
            # print(sql)
            cur.execute(sql)  # 执行查询语句
            self.conn.commit()
            self.conn.close()
        except:
            print(sys.exc_info())

    def ExecBorrow(self, *id):
        try:
            sql = "EXEC BorrowBook "
            for m in id:
                sql = sql + "\'" + m + "\',"
            sql = sql[:-1]
            # print(sql)
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
        except pymssql.OperationalError:
            print(sys.exc_info())
            b_str = str(sys.exc_info()[1]).split(',')[1].split('DB-Lib')[0]
            prompt = eval("%s'" % (b_str)).decode()
            return prompt
        except:
            print(sys.exc_info())
        self.conn.close()

    def ExecReturn(self, *id):
        try:
            sql = "EXEC ReturnBook "
            for m in id:
                sql = sql + "\'" + m + "\',"
            sql = sql[:-1]
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
        except pymssql.OperationalError:
            print(sys.exc_info())
            b_str = str(sys.exc_info()[1]).split(',')[1].split('DB-Lib')[0]
            prompt = eval("%s'"%(b_str)).decode()
            return prompt
        except:
            print(sys.exc_info())
        self.conn.close()

    '''
    def ExecAlter(self, sql):
        #执行增删改
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()


    def main():
        msg = SQLServer(
            server='127.0.0.1:1433',
            user='sa',
            password='123',
            database='BooksDB',
            charset='utf8')
        msg.ExecAlter(
            "insert into Reader values ('rd2018005','4','lly','CS','156576383',0)")
        result = msg.ExecQuery(
            "select * from Reader")
        for Value in result:
            print(Value)
    '''

if __name__=='__main__':
    msg = SQLServer()
    result = msg.ExecQuery("TB_Reader", "rdID=\'101\'")
    print(result)
