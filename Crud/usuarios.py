# -*- coding: utf-8 -*-
import mysql.connector
from conexao import Conexao


class CrudUsuarios(object):
    def __init__(self, id_usuario="", usuario="", senha="", nome_usuario="", sobrenome="", telefone="",
                 cpf="", endereco="", num="", bairro="", complemento="", cep="", referencia="", cidade="", estado="",
                 nivel="", status=""):
        self.id_usuario = id_usuario
        self.usuario = usuario
        self.senha = senha
        self.nome_usuario = nome_usuario
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
        self.nivel = nivel
        self.status = status

    # preencher dados na tabela clientes
    def crud_tabela_usuarios(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT id_user, usuario FROM usuarios """)
            self.id_usuario = []
            self.usuario = []

            for linha in c.fetchall():
                self.id_usuario.append(linha[0])
                self.usuario.append(linha[1])

            c.close()

        except mysql.connector.Error as err:
            print err

    # Buscar usuario selecionado na Tabela
    def buscar_usuarios_selecionado(self, cod):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT * FROM usuarios WHERE id_user = '{}' """.format(cod))

            for linha in c.fetchall():
                self.id_usuario = linha[0]
                self.usuario = linha[1]
                self.senha = linha[2]
                self.nome_usuario = linha[3]
                self.sobremone = linha[4]
                self.telefone = linha[5]
                self.cpf = linha[6]
                self.endereco = linha[7]
                self.num = linha[8]
                self.bairro = linha[9]
                self.comeplemento = linha[10]
                self.cep = linha[11]
                self.referencia = linha[12]
                self.cidade = linha[13]
                self.estado = int(linha[14])
                self.nivel = linha[15]
                self.status = linha[16]

            c.close()

        except mysql.connector.Error as err:
            print err

    # Buscar cliente na Tabela
    def busca_usuario_tabela(self, busca):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute("""SELECT id_user, usuario, nome FROM usuarios WHERE usuario LIKE "%{}%" OR nome LIKE
             '%{}%'""".format(busca, busca))

            self.id_usuario = []
            self.usuario = []
            self.sobremone = []

            for linha in c.fetchall():
                self.id_usuario.append(linha[0])
                self.usuario.append(linha[1])

            c.close()
        except mysql.connector.Error as err:
            print err

    # Inserir ou Atualizar clientes
    def cadastro_usuarios(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO usuarios (id_user, usuario, nome, sobrenome, telefone, cpf, endereco, num, bairro,
            complemento, cep, referencia, cidade, estado, nivel, status)
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', 
            '{}', '{}', '{}', '{}', '{}', '{}', '{}') 
            ON DUPLICATE KEY UPDATE usuario='{}', nome='{}', sobrenome='{}', telefone='{}', cpf='{}',
            endereco='{}', num='{}', bairro='{}', complemento='{}', cep='{}', referencia='{}', cidade='{}', estado='{}',
            nivel='{}', status='{}'
            """. format(self.id_usuario, self.usuario, self.nome_usuario, self.sobremone, self.telefone,
                        self.cpf, self.endereco,
                        self.num, self.bairro, self.comeplemento, self.cep, self.referencia, self.cidade, self.estado,
                        self.nivel, self.status,
                        self.usuario, self.nome_usuario, self.sobremone, self.telefone, self.cpf,
                        self.endereco, self.num, self.bairro, self.comeplemento, self.cep, self.referencia,
                        self.cidade, self.estado, self.nivel, self.status))

            conecta.conecta.commit()
            c.close()
            # print self.id_usuario
            # print self.estado
            # print self.id_usuario

        except mysql.connector.Error as err:
            print err

    def verifica_senha(self, senha):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT id_user, senha FROM usuarios WHERE id_user='{}' """.format(senha))
            for linha in c.fetchall():
                self.senha = linha[1]
            c.close()

        except mysql.connector.Error as err:
            print err

    def alterar_senha(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(""" UPDATE usuarios SET senha='{}' WHERE id_user='{}' """.format(self.senha, self.id_usuario))
            conecta.conecta.commit()
            # print self.senha
            # print self.id_usuario
        except mysql.connector.Error as err:
            print err
