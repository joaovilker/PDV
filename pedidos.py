# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from Views.pedidos import Ui_ct_main_pedido
from Views.confirmacao import Ui_Dialog
from Views.busca_cliente import Ui_DialogBuscarCliente
from Views.busca_produto import Ui_DialogBuscarProduto
from Class.Funcoes import Funcoes
from Crud.clientes import CrudCliente
from Crud.estoque import CrudProdutos


class MainPedidos(Ui_ct_main_pedido):
    def main_pedidos(self, frame):
        super(MainPedidos, self).setPedidos(frame)
        self.frame_geral_pedido.show()

        # Classes
        self.funcoes = Funcoes()
        self.produtos = CrudProdutos()
        self.produtos.crud_lista_produtos()

        # Estilo dos Botoes
        self.funcoes.estilo_botao_acao(self.bt_cadastrar_pedido, self.bt_cancelar_pedido)
        # Localizar CLiente
        self.bt_pedido_localizar_cliente.setIcon(QtGui.QIcon('Images/buscar.png'))
        self.bt_pedido_localizar_cliente.setIconSize(QtCore.QSize(20, 20))
        # Botao Localizar Produto
        self.bt_pedido_localizar_produto.setIcon(QtGui.QIcon('Images/buscar.png'))
        self.bt_pedido_localizar_produto.setIconSize(QtCore.QSize(20, 20))
        self.bt_pedido_localizar_produto.clicked.connect(self.janela_buscar_produto)
        # Add produto
        self.bt_pedido_add_produto.setIcon(QtGui.QIcon('Images/add.png'))
        self.bt_pedido_add_produto.setIconSize(QtCore.QSize(20, 20))
        # Cadastrar Pedido
        self.bt_cadastrar_pedido.clicked.connect(self.confirmar_pedido)
        # Cancelar_pedido
        self.bt_cancelar_pedido.setText("Cancelar")
        self.bt_cancelar_pedido.clicked.connect(self.cancelar_cad_pedido)

        # Estilo, acao e comando do Formulário
        # Buscar Cliente
        self.bt_pedido_localizar_cliente.clicked.connect(self.janela_busca_cliente)
        # Campo data com data atual
        self.tx_data_pedido.setDate(QtCore.QDate.currentDate())
        self.tx_data_notificacao.setDate(QtCore.QDate.currentDate())
        # Busca cod produto
        self.tx_pedido_cod_produto.setReadOnly(False)
        self.tx_pedido_cod_produto.returnPressed.connect(self.localizar_produto_codigo)
        # Campo produtos


        # Botao Concluir PEdido
        efeito = QtGui.QGraphicsDropShadowEffect()
        efeito.setColor(QtGui.QColor("#ff00ff"))
        efeito.setOffset(0, 0)
        efeito.setBlurRadius(15)
        self.bt_concluir_pedido.setGraphicsEffect(efeito)
        self.bt_concluir_pedido.setStyleSheet(" QPushButton{border-radius: 10px; border: none; background: #00ffff;}"
                            "QPushButton:disabled {background: #FFF}"
                            "QPushButton:hover {color: #FFF}")
        self.bt_concluir_pedido.setEnabled(False)


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
        # Funcoes da Janela
        # Selecionar CLiente e Fechar
        def selecionar_cliente_popup(row):
            self.tx_pedido_cod_cliente.setText(str(Janela.tableWidget.item(row, 0).text()))
            self.tx_pedido_nome_cliente.setText(Janela.tableWidget.item(row, 1).text())
            self.tx_pedido_telefone.setText(Janela.tableWidget.item(row, 2).text())
            Dialog.close()

        # Buscar Clientes
        def buscar_cliente():
            # Chamando Classe Crud Cliente
            busca_cliente = CrudCliente()
            busca_cliente.busca_tabela(Janela.lineEdit.text())

            #limpando Tabele
            while Janela.tableWidget.rowCount() > 0:
                Janela.tableWidget.removeRow(0)
            i = 0
            while i < len(busca_cliente.nome_cliente):
                Janela.tableWidget.insertRow(i)
                Janela.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(str(busca_cliente.cod_cliente[i])))
                Janela.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(busca_cliente.nome_cliente[i]))
                Janela.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem(str(busca_cliente.telefone[i])))
                i += 1

        # Chamando busca_clienter cliente
        Janela.lineEdit.returnPressed.connect(buscar_cliente)
        #Tabela Resultado
        Janela.tableWidget.setColumnWidth(0, 50)
        Janela.tableWidget.setColumnWidth(1, 180)
        Janela.tableWidget.setColumnWidth(2, 100)
        Janela.tableWidget.setItem
        Janela.tableWidget.horizontalHeader().setVisible(False)
        Janela.tableWidget.cellDoubleClicked.connect(selecionar_cliente_popup)
        Dialog.exec_()

    # Janela Buscar Produto
    def janela_buscar_produto(self):
        Janela = Ui_DialogBuscarProduto()
        Dialog = QtGui.QDialog()
        Janela.setBuscarProduto(Dialog)
        # Ajustes da Tabela
        Janela.table_busca_produto.setColumnWidth(0, 50)
        Janela.table_busca_produto.setColumnWidth(1, 210)
        Janela.table_busca_produto.setColumnWidth(2, 80)
        Dialog.exec_()


    def localizar_produto_codigo(self):
        self.produtos.busca_edicao(self.tx_pedido_cod_produto.text())
        self.tx_pedido_produto.setText(self.produtos.descricao)


    #Janela Confirmação
    def confirmar_pedido(self):
        Janela = Ui_Dialog()
        Dialog = QtGui.QDialog()
        Janela.setConfirmacao(Dialog)
        Dialog.exec_()

    #Cancelar
    def cancelar_cad_pedido(self):
        for filho in self.ct_frame_pedidos.findChildren(QtGui.QLineEdit):
            filho.clear()
        self.tx_data_notificacao.setDate(QtCore.QDate.currentDate())

        while self.tabela_pedido_add.rowCount() > 0:
            self.tabela_pedido_add.removeRow(0)


