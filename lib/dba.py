# coding:utf-8
import sqlite3

class Sqlite_db:
    """"""
    path=""
    
    def __init__(self,path_):
        """Constructor"""
        path=path_
        conn=sqlite3.connect(path)
        cur=conn.cursor()
        cur.execute('select * from portinfo')
        rows=cur.fetchall()
        print(rows)
        
    def load_Device_info(self):
        """"""
        
    def init_port_box(self):
        """"""
        
    def update_act(self):
        """"""
        