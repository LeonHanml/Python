
import pymysql
import sys
import os
import time
import datetime
import time,codecs
BASE_DIR = os.path.dirname(__file__)

class loadData():
        def __init__(self):
                try:


                        self.conn=pymysql.connect(host='10.250.100.17', user="",passwd="",port=3306,db="campaign",charset="utf8",ursorclass=pymysql.cursors.DictCursor)
                        self.cursor=self.conn.cursor()#social_media
                        print ("The connection is successful")
                except:
                        print ( "Connection failed ")
                finally:
                        print ( "")

        def getFile(self,fileName):
                data = codecs.open(fileName)
                dataout = codecs.open(fileName)
                for i in range(100):
                        item = data.readline()
                        itemEles = item.split(" ")
                        if len(item) <0 |item.__contains__("CREATE TABLE"):

                                continue
                        else:
                                if item.__contains__("TABLE"):
                                        tableName ="Table Name："+ itemEles[4].replace("`","")
                                        item.replace("","")
                                        dataout.writeline(tableName)
                                elif len(itemEles) > 0:
                                        str = itemEles[0]

                        print(i)




if __name__=="__main__":

        data =["1","3","4","5","6","7","6","7","6","7"]
        tomorrow = datetime.datetime.now().date()
        today = datetime.datetime.today()
        print(tomorrow)
        print(today.date())






