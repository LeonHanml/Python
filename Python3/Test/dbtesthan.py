
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


        def dataInsert(self,data):#172.26.93.6

                        try:
                                # sql="insert  into `PG_CAMPAIGN_API_SEM`(`MONITOR_CODE`,`PROMOTION_PLAN`,`MONITOR_URL`,`KEYWORD_CODE`,`MONITOR_CODE`)"





                                sql="insert  into PG_CAMPAIGN_API_GOOGLE ( `CAMPAIGN_ID`,`CAMPAIGN_NAME`,`MONITOR_CODE`,`WEBSITE_URL`,`DATE_TIME`,`COST`,`IMPRESSION`,`CLICK`,`ADD_USER`,`ROLE_ID`,`CREATE_TIME`  )" \
                                    " values ( '"+data[1]+"','"+data[0]+"','"+data[2].split("=")[1]+"','"+data[3]+ "','"+'0'+"','"+data[4]+"','"+data[5]+"','"+'pingou_test'+"','"+'61460c6ec3a24cd19c281350263d6b88'+"','"+''+"')"

                                num=self.cursor.execute(sql)
                                self.conn.commit()
                                print ( 'Insertion succeed')
                        except Exception as e:
                                print (e)
                        finally:
                                print ( "")

        def getMonitorCode(self,url):
                code = url.split("=")[1]
                return code

        def getByCondition(self,strName):

                sql="SELECT MAX(c_register_time) FROM moto_fans_info where c_profile_url= '"+strName+"'"
                num=self.cursor.execute(sql)
                row=self.cursor.fetchone()
                if row[0]!=None:
                   return row[0]
                else:
                   return ''
        def update(self,c_blogname,c_register_time,c_focus_num,c_fans_num,c_user_type,c_gender,c_age,c_province,c_weight,c_profile_url):
                        try:
                                #sql="insert  into `moto_fans_info`(`c_blogname`,`c_register_time`,`c_focus_num`,`c_fans_num`,`c_user_type`,`c_gender`,`c_age`,`c_province`,`c_weight`,`c_profile_url`) values ( '"
                                sql="UPDATE moto_fans_info SET c_blogname='' "
                                sql+= c_blogname+"',c_register_time='"+c_register_time+"',c_focus_num='"+c_focus_num+"',c_fans_num='"+c_fans_num
                                sql+="',c_user_type='"+c_user_type+"',c_gender='"+c_gender+"',c_age='"+c_age+"',c_province='"+c_province+"',c_weight='"+c_weight+"' "
                                sql+="where c_profile_url='"+c_profile_url+"'"
                                num=self.cursor.execute(sql)
                                self.conn.commit()
                                print ( 'update succeed')
                        except Exception as e:
                                print (e)
                        finally:
                                print ("")

        def delete(self):

                sql="DELETE FROM moto_fans_info "
                num=self.cursor.execute(sql)
                return num
        def getByDate(self):
                try:

                        sql="SELECT MAX(t_date) FROM g_weibo_content where key_word='MOTO'"
                        num=self.cursor.execute(sql)
                        row=self.cursor.fetchone()
                        if row[0]!=None:
                                print ( row[0])
                                return row[0]
                        else:
                                return '0000-00-00 00:00:00'
                except:
                        print ( "Fail to get date")
                        return '0000-00-00 00:00:00'
                finally:
                        print (  '')
        def getByDate_V(self):
                try:

                        sql="SELECT MONITOR_CODE,KEYWORD_CODE FROM PG_AD_KEYWORD "
                        num=self.cursor.execute(sql)
                        results = self.cursor.fetchall()
                        for row in results:
                                # result.append(row[0])
                                print ( row[0]+'\t'+str(int(row[1][1:])))
                                # return row[0]
                        else:
                                return '0000-00-00 00:00:00'
                except:
                        print ( "Fail to get date")
                        return '0000-00-00 00:00:00'
                finally:
                        print (  '')
if __name__=="__main__":
        # while(1):
        #         try:
        #                 print ( test()
        #         except:
        #                 h=1
        #         finally:
        #                 print ( "hhh"
        data =["1","3","4","5","6","7","6","7","6","7"]
        tomorrow = datetime.datetime.now().date()
        today = datetime.datetime.today()
        print(tomorrow)
        print(today.date())


        # code = loadData().getMonitorCode(url = "http://www.thinkworld.com.cn/activity/X1Carbon17/index.html?pmf_source=Z00000779T055")
        # print (datetime().now().date())
        # data=codecs.open(u'D:\\Program Files (x86)\\Tencent\\Qq\\291334449\FileRecv\\Demo.txt','r','utf-8')
        # item=data.readline()
        # while len(item)>0:
        #     keywords=item.replace('\r\n','').split('\t')
        #
        #     if len(keywords)<6:
        #         print ( keywords)
        #     loadData().dataInsert(keywords)
        #
        #     print ( keywords)
        #     item=data.readline()
        # print ( int('021')
        # key=[u'1','2','3','4']

         #print ( loadData().getById('3801978582849989')
        # conn=MySQLdb.connect(host='localhost', user="root",passwd="root",port=3306,db="test",charset="utf8")#MySQLdb.connect(host=ip,user="root",passwd="root",db="svmtest",charset="utf8", local_infile = 1)#"crawler_db2"
        # cursor=conn.cursor()
        #         #myfile=open(resultFile,'r')
        #         #print ( myfile.readline().decode("utf8").encode("gb18030")
        #         #sql="load data local infile '"+resultFile+"' ignore into table classifyResults fields terminated by '\t' lines terminated by '\n'"
        #
        # sql="SELECT * FROM g_weibo_content "
        # print ( sql
        # num=cursor.execute(sql)
        # print ( num
        # row=cursor.fetchone()
        # print ( row[0]
        #print ( int(time.time())



