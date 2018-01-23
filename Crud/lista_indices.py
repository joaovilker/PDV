# -*- coding: utf-8 -*-

from conexao import Conexao
import mysql.connector


class ListasIndices(object):
    def __init__(self, lst_status="", dic_status="", lista_estados="", lst_nivel="", dic_nivel=""):
        self.lst_status = lst_status
        self.dic_status = dic_status
        self.lista_estados = lista_estados
        self.lst_nivel = lst_nivel
        self.dic_nivel = dic_nivel

    def lista_status(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        self.lst_status = []
        self.dic_status = {}

        try:
            c.execute("SELECT * FROM status_usuarios")
            for linha in c.fetchall():
                self.lst_status.append(linha[1])
                self.dic_status.update({linha[1]: linha[0]})
            c.close()

        except mysql.connector.Error as err:
            print err

    def todos_estados(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT id, uf FROM estado """)
            self.lista_estados = []

            for linha in c.fetchall():
                self.lista_estados.append(linha[1])

            c.close()

        except mysql.connector.Error as err:
            print err

    def combobox_nivel(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(""" SELECT * FROM nivel_acesso """)
            self.lst_nivel = []
            for linha in c.fetchall():
                self.lst_nivel.append(linha[1])

        except mysql.connector.Error as err:
            print err
