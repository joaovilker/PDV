# -*- coding: utf-8 -*-
import mysql.connector
from conexao import Conexao


class CrudCliente(object):
    def __init__(self, cod_cliente="", nome_cliente="", sobrenome="", telefone="", cpf="", endereco="", num="",
                 bairro="", complemento="", cep="", referencia="", cidade="", estado=""):
        self.cod_cliente = cod_cliente
        self.nome_cliente = nome_cliente
        self.sobremone = sobrenome
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco
        self.num = num
        self.bairro = bairro
        self.comeplemento = complemento
        self.cep = cep
        self.referencia = referencia
        self.cidade = cidade
        self.estado = estado

    # preencher dados na tabela clientes
    def crud_tabela_cliente(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT id_cliente, nome, sobrenome FROM clientes """)
            self.cod_cliente = []
            self.nome_cliente = []
            self.sobremone = []

            for linha in c.fetchall():
                self.cod_cliente.append(linha[0])
                self.nome_cliente.append(linha[1])
                self.sobremone.append(linha[2])
            c.close()

        except mysql.connector.Error as err:
            print err

    # Buscar Cliente selecionado na Tabela
    def buscar_cliente_selecionado(self, cod):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT * from clientes WHERE id_cliente = '{}' """.format(cod))

            for linha in c.fetchall():
                self.cod_cliente = linha[0]
                self.nome_cliente = linha[1]
                self.sobremone = linha[2]
                self.telefone = linha[3]
                self.cpf = linha[4]
                self.endereco = linha[5]
                self.num = linha[6]
                self.bairro = linha[7]
                self.comeplemento = linha[8]
                self.cep = linha[9]
                self.referencia = linha[10]
                self.cidade = linha[11]
                self.estado = linha[12]
            c.close()

        except mysql.connector.Error as err:
            print err

    # Buscar cliente na Tabela
    def busca_tabela(self, busca):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute("""SELECT id_cliente, nome, sobrenome FROM clientes WHERE nome LIKE "%{}%" """.format(busca))

            self.cod_cliente = []
            self.nome_cliente = []
            self.sobremone = []

            for linha in c.fetchall():
                self.cod_cliente.append(linha[0])
                self.nome_cliente.append(linha[1])

            c.close()
        except mysql.connector.Error as err:
            print err

    # Inserir ou Atualizar clientes
    def cadastro_cliente(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO clientes VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
            '{}', '{}', '{}') ON DUPLICATE KEY UPDATE nome='{}', sobrenome='{}', telefone='{}', cpf='{}',
            endereco='{}', num='{}', bairro='{}', complemento='{}', cep='{}', referencia='{}', cidade='{}', estado='{}'
            """. format(self.cod_cliente, self.nome_cliente, self.sobremone, self.telefone, self.cpf, self.endereco,
                        self.num, self.bairro, self.comeplemento, self.cep, self.referencia, self.cidade, self.estado,
                        self.nome_cliente, self.sobremone, self.telefone, self.cpf, self.endereco, self.num,
                        self.bairro, self.comeplemento, self.cep, self.referencia, self.cidade, self.estado))
            conecta.conecta.commit()
            c.close()
            # print self.cod_cliente
            # print self.estado
            # print self.cod_cliente

        except mysql.connector.Error as err:
            print err
