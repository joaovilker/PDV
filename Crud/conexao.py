# -*- coding: utf-8 -*-
import mysql.connector

class Conexao(object):
    def __init__(self):
        try:
            self.conecta = mysql.connector.connect(host="127.0.0.1", database="azulerosa", user="andre",
                                                   password="rsp", charset="utf8", use_unicode=True)
            c = self.conecta.cursor()
            c.close()
        except mysql.connector.Error as err:
            print err