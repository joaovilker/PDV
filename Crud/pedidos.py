# -*- coding: utf-8 -*-

from conexao import Conexao
import mysql.connector

class CrudPedidos(object):
    def __init__(self, cod_produto="", produto="", qtde="", valor="", lst_produto = "", dic_produto = ""):
        self.cod_produto = cod_produto
        self.produto = produto
        self.qtde = qtde
        self.valor = valor
        self.lst_produto = lst_produto
        self.dic_produto = dic_produto

    def cad_pedido(self):
        conecta = Conexao



