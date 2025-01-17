import pymysql
from flask import render_template
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

class master_flask_code:
    def __init__(self,database):
        self.user = 'root'
        self.password = ''
        self.host = 'localhost'
        self.database = database
    def find_max_id(self,table):
        conn = pymysql.connect(user=self.user, password=self.password, host=self.host, database=self.database,charset='utf8')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM "+table)
        data = cursor.fetchall()
        maxin = len(data)
        if maxin == 0:
            maxin = 1
        else:
            maxin += 1
        return maxin
    def insert_query(self,qry):
        conn = pymysql.connect(user=self.user, password=self.password, host=self.host, database=self.database,charset='utf8')
        cursor = conn.cursor()
        result=cursor.execute(qry)
        conn.commit()
        conn.close()
        return result
    def select_login(self,qry):
        conn = pymysql.connect(user=self.user, password=self.password, host=self.host, database=self.database,charset='utf8')
        cursor = conn.cursor()
        cursor.execute(qry)
        data = cursor.fetchall()
        check = len(data)
        if check == 0:
            return 'no'
        else:
            return 'yes'

    def select_single_colum(self, table, colum):
        conn = pymysql.connect(user=self.user, password=self.password, host=self.host, database=self.database,charset='utf8')
        qry1 = ("select " + colum + "  from " + table)
        cursor = conn.cursor()
        cursor.execute(qry1)
        data = cursor.fetchall()
        return data

    def select_entire_colum(self,table,colum):
        conn = pymysql.connect(user=self.user, password=self.password, host=self.host, database=self.database,charset='utf8')
        qry1=("select *  from "+table+" where symptoms LIKE '%"+colum+"%'")
        cursor = conn.cursor()
        cursor.execute(qry1)
        data = cursor.fetchall()
        return data

    def select_direct_query(self,qry):
        conn = pymysql.connect(user=self.user, password=self.password, host=self.host, database=self.database,charset='utf8')

        cursor = conn.cursor()
        cursor.execute(qry)
        data = cursor.fetchall()
        return data

    def send_email_without_attachment(self,to_mail,key):
        msg = MIMEMultipart()

        password = "Extazee2021"
        msg['From'] = "serverkey2018@gmail.com"
        msg['To'] = to_mail
        msg['Subject'] = "key"
        # file = str1
        # fp = open(file, 'rb')
        # img = MIMEImage(fp.read())
        # fp.close()
        # msg.attach(img)
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], (key))
        server.quit()



