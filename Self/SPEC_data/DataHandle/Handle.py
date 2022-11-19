import csv

import pandas as pd
import pymysql

#数据处理

df = pd.read_csv(r"C:\\Users\\daimaoling\\Desktop\\数据中台\\project\\SPEC_data\\pachong\\Data\\CFP2006.csv")
pd.set_option("display.max.columns", None)
# print(df.head(10))
# 读取某一列数据
# x = df['TestSponsor'] 打印某一列
# print(x)
# print(df.dtypes) 打印表各个属性类型
# 字符串替换
df['Base'] = df['Base'].str.replace('&nbsp;', '')
df['Base'] = df['Base'].str.replace('NC', '0')
df['Peak'] = df['Peak'].str.replace('&nbsp;', '')
df['Peak'] = df['Peak'].str.replace('NC', '0')
df['Peak'] = df['Peak'].str.replace('Not Run', '-1')
df['Peak'] = df['Peak'].str.replace('--', '-2')
df['Base'] = df['Base'].astype(float)
df['Peak'] = df['Peak'].astype(float)
# print(df)
# print(df.dtypes)
df.to_csv(r"C:\\Users\\daimaoling\\Desktop\\数据中台\\project\\SPEC_data\\DataHandle\\NewData\\CFP2006.csv")
print("over")

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='daimaoling', db='specdata', charset= 'utf8')
# 创建游标对象
cursor = conn.cursor()
# 读入csv文件
with open("C:\\Users\\daimaoling\\Desktop\\数据中台\\project\\SPEC_data\\DataHandle\\NewData\\CFP2006.csv", mode='r',encoding='utf-8') as f:
    reader = csv.reader(f)
    # head = next(reader)
    # print(head)
    # 一行一行得存储，除去第一行和第一列
    for each in list(reader)[1:]:
        i = tuple(each[1:])
        sql = "insert into cfp2006 values" + str(i)
        cursor.execute(sql)
    conn.commit()  # 提交数据
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库



