# -*- coding: utf-8 -*-

from conexao import Conexao
import mysql.connector

class CrudPedidos(object):
    def __init__(self, cod_pedido="", cod_produto="", cliente="", data_aviso="", data_entrega="", status="", entrada="", devedor="",
                 valor_total = "", id_relacao="", produto = "", qtde="", valor_produto="", total_produto="", tema="",
                 obs="", lst_status_pedido="", dic_status_pedidos=""):
        self.cod_pedido = cod_pedido
        self.cliente = cliente
        self.data_aviso = data_aviso
        self.data_entrega = data_entrega
        self.status_pedido = status
        self.entrada = entrada
        self.valor_total = valor_total
        self.saldo_devedor = devedor
        self.id_relacao = id_relacao
        self.produto = produto
        self.qtde = qtde
        self.valor_produto = valor_produto
        self.total_produto = total_produto
        self.tema = tema
        self.obs = obs
        self.lst_status_pedido = lst_status_pedido
        self.dic_status_pedido = dic_status_pedidos
        self.cod_produto = cod_produto

    def cad_pedido(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(""" INSERT INTO pedidos VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}') """
                      .format(self.cod_pedido, self.cliente, self.data_entrega, self.status_pedido, self.entrada,
                       self.saldo_devedor, self.valor_total))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print err

    def cad_pedido_produtos(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        # Buscando ùltimo ID pedido
        try:
            c.execute(""" SELECT id_pedido FROM pedidos ORDER BY id_pedido DESC LIMIT 1""")
            ultimo_id = c.fetchone()[0]
            c.execute(""" INSERT INTO relacao_pedido VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
                      .format(self.id_relacao, ultimo_id, self.produto, self.qtde, self.valor_produto,
                              self.total_produto, self.tema, self.obs))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print err

    def busca_pedidos(self, busca):
        import datetime
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(""" SELECT pedidos.*, clientes.nome, status_pedido.status_pedido FROM pedidos
            INNER JOIN clientes ON pedidos.cliente = clientes.id_cliente
            INNER JOIN status_pedido ON pedidos.status = status_pedido.cod_status_pedido
            """)

            self.cod_pedido = []
            self.cliente = []
            self.status_pedido = []
            self.data_entrega = []
            self.entrada = []
            self.saldo_devedor = []
            self.valor_total = []

            for linha in c.fetchall():
                self.cod_pedido.append(linha[0])
                self.cliente.append(linha[7])
                self.status_pedido.append(linha[8])
                self.data_entrega.append(datetime.date.strftime(linha[2], "%d-%m-%Y"))
                self.entrada.append(linha[4])
                self.saldo_devedor.append(linha[5])
                self.valor_total.append(linha[6])


        except mysql.connector.Error as err:
            print err

    def combo_status_data(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT * FROM status_pedido """)
            self.lst_status_pedido = []
            self.dic_status_pedido = {}
            for linha in c.fetchall():
                self.lst_status_pedido.append(linha[1])
                self.dic_status_pedido.update({linha[1]: linha[0]})

            c.close()
        except mysql.connector.Error as err:
            print err

        return self.lst_status_pedido

    def selecionar_pedido(self, cod):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT relacao_pedido.*, pedidos.*, clientes.* , produtos.*  from relacao_pedido
            INNER JOIN pedidos ON  relacao_pedido.cod_pedido = pedidos.id_pedido
            INNER JOIN clientes ON pedidos.cliente = id_cliente
            INNER JOIN produtos ON relacao_pedido.produto = produtos.id_produto
              
            WHERE id_pedido = {}""".format(cod) )

            self.cod_produto = []
            self.produto = []
            self.qtde = []
            self.valor_produto = []
            self.tema = []
            self.obs = []
            self.total_produto = []



            for linha in c.fetchall():
                self.cod_produto.append(linha[1])
                self.cliente = (linha[15])
                self.produto.append(linha[29])
                self.qtde.append(linha[3])
                self.valor_produto.append(linha[4])
                self.tema.append(linha[6])
                self.total_produto.append(linha[5])
                self.obs.append(linha[7])
                self.valor_total = linha[14]
                self.entrada = linha[12]
                self.saldo_devedor = linha[13]







        except mysql.connector.Error as err:
            print err




#
busca = CrudPedidos()
busca.selecionar_pedido(14)
print busca.produto

# busca.produto = 2
# busca.qtde = 2
# busca.valor_produto = "25.00"
# busca.total_produto = "50.00"
# busca.tema = 1
# busca.obs = "nenhuma"
# busca.cad_pedido_produtos()






