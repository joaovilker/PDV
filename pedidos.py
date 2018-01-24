# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from Views.pedidos import Ui_ct_main_pedido
from Views.confirmacao import Ui_Dialog
from Views.busca_cliente import Ui_DialogBuscarCliente
from Class.Funcoes import Funcoes


class MainPedidos(Ui_ct_main_pedido):
    def main_pedidos(self, frame):
        super(MainPedidos, self).setPedidos(frame)
        self.frame_geral_pedido.show()

        # Classes
        self.funcoes = Funcoes()

        # Estilo dos Botoes
        self.funcoes.estilo_botao_acao(self.bt_cadastrar_pedido, self.bt_cancelar_pedido)
        # Localizar CLiente
        self.bt_pedido_localizar_cliente.setIcon(QtGui.QIcon('Images/buscar.png'))
        self.bt_pedido_localizar_cliente.setIconSize(QtCore.QSize(20, 20))
        # Add produto
        self.bt_pedido_add_produto.setIcon(QtGui.QIcon('Images/add.png'))
        self.bt_pedido_add_produto.setIconSize(QtCore.QSize(20, 20))
        # Cadastrar Pedido
        self.bt_cadastrar_pedido.clicked.connect(self.confirmar_pedido)
        # Cancelar_pedido
        self.bt_cancelar_pedido.setText("Cancelar")

        # Estilo, acao e comando do Formulário
        # Buscar Cliente
        self.bt_pedido_localizar_cliente.clicked.connect(self.janela_busca_cliente)



        # Tamanho, acao  e conteudo tabela  produtos pedido
        self.tabela_pedido_add.setColumnWidth(0, 200)
        self.tabela_pedido_add.setColumnWidth(1, 70)
        self.tabela_pedido_add.setColumnWidth(2, 70)
        self.tabela_pedido_add.setColumnWidth(3, 70)
        self.tabela_pedido_add.setColumnWidth(4, 30)

        # Tamanho, acao  e conteudo tabela Pedidos Pendentes
        self.tabela_pedidos.setColumnWidth(0, 40)
        self.tabela_pedidos.setColumnWidth(1, 80)
        self.tabela_pedidos.setColumnWidth(2, 160)
        self.tabela_pedidos.horizontalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        self.tabela_pedidos.verticalHeader().setVisible(False)

    #Janela Buscar cliente
    def janela_busca_cliente(self):
        Dialog = QtGui.QDialog()
        Janela = Ui_DialogBuscarCliente()
        Janela.setBuscarCliente(Dialog)
        #Funcoes da Janela
        def selecionar_cliente_popup(row):
            self.tx_pedido_cod_cliente.setText(str(Janela.tableWidget.item(row, 0).text()))
            self.tx_pedido_nome_cliente.setText(Janela.tableWidget.item(row, 1).text())
            Dialog.close()
        # Ajustes de Parametros

        #Tabela Resultado
        Janela.tableWidget.setColumnWidth(0, 50)
        Janela.tableWidget.setColumnWidth(1, 280)
        Janela.tableWidget.setItem
        Janela.tableWidget.horizontalHeader().setVisible(False)
        Janela.tableWidget.insertRow(0)
        Janela.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem("50"))
        Janela.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem("Teste2"))
        Janela.tableWidget.cellDoubleClicked.connect(selecionar_cliente_popup)
        Dialog.exec_()


    #Janela Confirmação
    def confirmar_pedido(self):
        Janela = Ui_Dialog()
        Dialog = QtGui.QDialog()
        Janela.setConfirmacao(Dialog)
        Dialog.exec_()
