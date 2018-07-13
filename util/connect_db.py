# coding:utf-8
import MySQLdb.cursors
import json


class OperationMysql:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='192.168.15.244',
            port=3306,
            user='lonch',
            passwd='lonch@123',
            db='clinicpe',
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor#设置返回结果为字典格式
        )
        self.cur = self.conn.cursor()

    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        # result = json.dumps(result)
        return result


if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one('select * from doctor_info WHERE work_unit="杜国强卫生室"')
    print res['skill']
    print type(res)
    data ={"name":"liuyujie","pwd":"123456"}
    print type(data)
    print json.dumps(data)

