# -*- coding: utf-8 -*-
import mysql.connector
from conexao import Conexao


class CrudProdutos(object):

    def __init__(self, cod_produto="", descricao="", qtde_minima="", qtde_disponivel="", valor_compra="",
                 valor_venda="", fornecedor="", tipo="", obs="", lst_produtos ="", dic_produtos=""):
        self.cod_produto = cod_produto
        self.descricao = descricao
        self.qtde_minima = qtde_minima
        self.qtde_disponivel = qtde_disponivel
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.fornecedor = fornecedor
        self.tipo_produto = tipo
        self.obs = obs
        self.lst_produtos = lst_produtos
        self.dic_produtos = dic_produtos

    def crud_lista_produtos(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        self.cod_produto = []
        self.descricao = []
        self.qtde_disponivel = []



        try:
            c.execute(""" SELECT id_produto, produto, quantidade_estoque FROM produtos""")

            for linha in c.fetchall():
                self.cod_produto.append(linha[0])
                self.descricao.append(linha[1])
                self.qtde_disponivel.append(linha[2])

            c.close()
        except mysql.connector.Error as err:
            print err

    def crud_busca_produto(self, cod):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        self.cod_produto = []
        self.descricao = []
        self.qtde_disponivel = []
        self.valor_venda = []

        try:
            c.execute(""" SELECT id_produto, produto, quantidade_estoque, valor_venda FROM produtos 
            WHERE produto LIKE  "%{}%" """
                      .format(cod))
            for linha in c.fetchall():
                self.cod_produto.append(linha[0])
                self.descricao.append(linha[1])
                self.qtde_disponivel.append(linha[2])
                self.valor_venda.append(linha[3])
            c.close()

        except mysql.connector.Error as err:
            print err

    def cadastra_produto(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:

            c.execute(""" INSERT INTO produtos VALUES ( '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') 
                     ON DUPLICATE KEY UPDATE produto='{}', quantidade_minima='{}', quantidade_estoque='{}', 
                     valor_compra='{}', valor_venda='{}', fornecedor='{}', tipo='{}', obs='{}'  """
                      .format(self.cod_produto, self.descricao, self.qtde_minima, self.qtde_disponivel,
                              self.valor_compra, self.valor_venda, self.fornecedor, self.tipo_produto, self.obs,
                              self.descricao, self.qtde_minima, self.qtde_disponivel, self.valor_compra,
                              self.valor_venda, self.fornecedor, self.tipo_produto, self.obs
                              ))
            conecta.conecta.commit()
            c.close()

        except mysql.connector.Error as err:
            print err

    def busca_edicao(self, cod):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT * FROM produtos WHERE id_produto = '{}' """.format(cod))
            busca = c.fetchone()
            self.cod_produto = busca[0]
            self.descricao = busca[1]
            self.qtde_minima = busca[2]
            self.qtde_disponivel = busca[3]
            self.valor_compra = busca[4]
            self.valor_venda = busca[5]
            self.fornecedor = busca[6]
            self.tipo_produto = busca[7]
            self.obs = busca[8]
        except mysql.connector.Error as err:
            print err



# busca = CrudProdutos()
# busca.crud_lista_produtos()
# print busca.dic_produtos
# print busca.descricao
# busca.descricao = "Caneca Cerêmica"
# busca.qtde_minima = '5'
# busca.qtde_disponivel = '12'
# busca.valor_compra = '7.90'
# busca.valor_venda = '25.00'
# busca.fornecedor = '1'
# busca.tipo_produto = '1'
# busca.obs = "Nenhuma"
# busca.cadastra_produto()

