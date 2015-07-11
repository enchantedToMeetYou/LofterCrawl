#coding=utf-8
import sys
import os

import pymysql

FILE_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append('{0}/../config'.format(FILE_PATH))
import AppSetting

class MysqlManager(object):
    @staticmethod
    def get_conn():
        return pymysql.connect(**AppSetting.local_data_base)

    @staticmethod
    def create_table():
        conn = MysqlManager.get_conn()
        cur = conn.cursor()
        sql1 = '''  DROP TABLE IF EXISTS LOFTER_IAMGE_SETS; '''
        sql2 = '''
                CREATE TABLE IF NOT EXISTS LOFTER_IMAGE_SETS (
                ImageSetName varchar(40),
				ImageName varchar(40),
                Category TEXT,
                Description TEXT,
				ImageURL TEXT,
                URL TEXT
                )engine=InnoDB DEFAULT charset=utf8;
                '''
        sql3 =  '''  ALTER TABLE LOFTER_IMAGE_SETS ADD CONSTRAINT UNIQUE_PHOTOID_PHOTONAME UNIQUE (ImageSetName,ImageName);''' 
		
        try:
            cur.execute(sql1)
            cur.execute(sql2)
            cur.execute(sql3)
            conn.commit()
            return True
        except Exception as e:
            print e
            return False
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()

                
    @staticmethod
    def insert_items_into_photos(items):
        conn = MysqlManager.get_conn()
        cur = conn.cursor()
        sql = '''
              INSERT INTO LOFTER_IMAGE_SETS 
              (ImageSetName, ImageName, Category, Description, ImageURL, URL) 
              VALUES(%s,%s,%s,%s,%s,%s) 
              ON DUPLICATE KEY UPDATE 
              ImageSetName=%s,
			  ImageName=%s,
              Category=%s,
              Description=%s,
			  ImageURL=%s,
              URL=%s
              '''
        try:
            cur.executemany(sql, items)
            conn.commit()
            return True
        except Exception as e:
            print e
            return False
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()

if __name__ == '__main__':
    #print MysqlManager.get_realtime_cheat_user('guid_str')
    MysqlManager.create_table() 
    item = [('23','34','56','78','9','10')*2]	
    MysqlManager.insert_items_into_photos(item)
	#print MysqlManager.get_return_cash()
