#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import numpy as np
import matplotlib.pyplot as plt

host = '10.250.100.23'
port = 3306
user = 'storm'
passwd = 'hiWMAtvo8kYkxbjU'
db = 'realtime'
conn = MySQLdb.Connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
cursor = conn.cursor()
qushi = np.dtype([('pv', np.uint32), ('uv', np.uint32), ('rc', np.uint32), ('un', np.uint32), ('id', np.uint32),
                  ('min', np.string_)])
sql1 = "select pv ,uv,rc ,un,id,min from shopflow_total_pvuv where date = '2017-09-05' and pv >0 order by id"
# sql2 = "select pv ,uv,rc ,un,id,min from shopflow_total_incre_pvuv where date = '2017-08-11'and pv>0 order by id"
sql3 = "select pv ,uv,rc ,un,id,min from shopflow_total_basic_bymin where date = '2017-09-04'order by id"
# and pv>0

cursor.execute(sql1)
result = cursor.fetchall()
data = np.fromiter(result, dtype=qushi, count=-1)
fig = plt.figure()
plt.subplot2grid((2, 2), (0, 0))



# plt.plot(x1, y1,'r', label='broadcast')
# plt.plot(x2, y2,'b',label='join')
# plt.xticks(x1, group_labels, rotation=0)
# id = int(data['id'])
# pv = int(data['pv'])
# uv = int(data['uv'])
# plt.plot(id, pv,'r', label='pv')
# plt.plot(id, uv,'b',label='uv')
plt.title('PvuvHan')
plt.xlabel('Time')
plt.ylabel('Count')
plt.plot(data['id'], data['pv'], 'b', label='pv')
plt.plot(data['id'], data['uv'], 'g', label='uv')
plt.plot(data['id'], data['rc'], 'r', label='uv')
plt.plot(data['id'], data['un'], 'b', label='uv')
# plt.xticks(x3, group_labels, rotation=0)



cursor2 = conn.cursor()
cursor2.execute(sql3)
result2 = cursor2.fetchall()
data2 = np.fromiter(result2, dtype=qushi, count=-1)
# plt.subplot2grid((2, 2), (0, 1))
# plt.title('PvuvLiu')
# plt.xlabel('Time')
# plt.ylabel('Count')
# plt.plot(data2['id'], data2['pv'], 'b', label='pv')
# plt.plot(data2['id'], data2['uv'], 'g', label='uv')
# plt.plot(data2['id'], data2['rc'], 'r', label='uv')
# plt.plot(data2['id'], data2['un'], 'b', label='uv')

# plt.subplot2grid((2, 2), (1, 0))
# plt.title('00')
# plt.xlabel('Time')
# plt.ylabel('Count')
# plt.plot(data2['id'],  data['pv']-data2['pv'], 'b', label='pv')
# plt.plot(data2['id'], data2['uv'], 'g', label='uv')
# plt.plot(data2['id'], data2['rc'], 'r', label='uv')
# plt.plot(data2['id'], data2['un'], 'b', label='uv')

# cursor2 = conn.cursor()
# cursor2.execute(sql2)
# result2 = cursor2.fetchall()
# data2 = np.fromiter(result2, dtype=qushi, count=-1)
# plt.subplot2grid((2, 1), (1, 0))
# plt.title('PvuvIncre')
# plt.xlabel('Time')
# plt.ylabel('Count')
# plt.bar(data2['id'], data2['pv'])
# plt.legend(bbox_to_anchor=[0.3, 1])
plt.grid()
plt.show()








































# 如题，我知道plot函数代表不同颜色的标示符一共有八种：
# 标记符    颜色
# r             红
# g            绿
# b            蓝
# c          蓝绿
# m         紫红
# y           黄
# k           黑
# w          白
