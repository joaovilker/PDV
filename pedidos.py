# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from Views.pedidos import Ui_ct_main_pedido
from Views.confirma_pedido import Ui_Dialog_pedido
from Views.busca_cliente import Ui_DialogBuscarCliente
from Views.busca_produto import Ui_DialogBuscarProduto
from Class.Funcoes import Funcoes
from Crud.clientes import CrudCliente
from Crud.estoque import CrudProdutos
from Crud.pedidos import CrudPedidos
from buscaPedido import BuscaPedido


class MainPedidos(Ui_ct_main_pedido):
    def main_pedidos(self, frame):
        super(MainPedidos, self).setPedidos(frame)
        self.frame_geral_pedido.show()

        # Classes
        self.funcoes = Funcoes()
        self.produtos = CrudProdutos()
        self.produtos.crud_lista_produtos()

        self.pedidos = CrudPedidos()


        # Dasabilitando campos até serem preenchidos outros
        # Busca código e Lupa busca
        self.tx_pedido_cod_produto.setEnabled(True)
        self.bt_pedido_localizar_produto.setEnabled(True)
        self.tx_pedido_quantidade.setEnabled(True)
        self.tx_obs.setReadOnly(False)
        self.temas = ['Homem Aranha', 'Peppa Pig', 'Batman']
        self.tx_tema.addItems(self.temas)

        self.bt_cadastrar_pedido_2.clicked.connect(self.busca_pedidos)



        # Estilo dos Botoes
        self.funcoes.estilo_botao_acao(self.bt_cadastrar_pedido, self.bt_cancelar_pedido)
        # Localizar CLiente Stilo
        self.bt_pedido_localizar_cliente.setIcon(QtGui.QIcon('Images/buscar.png'))
        self.bt_pedido_localizar_cliente.setIconSize(QtCore.QSize(20, 20))
        # Botao Localizar Produto
        self.bt_pedido_localizar_produto.setIcon(QtGui.QIcon('Images/buscar.png'))
        self.bt_pedido_localizar_produto.setIconSize(QtCore.QSize(20, 20))
        self.bt_pedido_localizar_produto.clicked.connect(self.janela_buscar_produto)
        self.bt_pedido_add_produto.setIcon(QtGui.QIcon('Images/add.png'))
        self.bt_pedido_add_produto.setIconSize(QtCore.QSize(20, 20))
        self.bt_pedido_add_produto.clicked.connect(self.add_produto_tabela)




        # Cadastrar Pedido
        self.bt_cadastrar_pedido.setEnabled(False)
        self.bt_cadastrar_pedido.clicked.connect(self.confirmar_pedido)
        # Cancelar_pedido
        self.bt_cancelar_pedido.setText("Cancelar")
        self.bt_cancelar_pedido.clicked.connect(self.cancelar_cad_pedido)

        # Estilo, acao e comando do Formulário
        # Buscar Cliente
        self.bt_pedido_localizar_cliente.clicked.connect(self.janela_busca_cliente)
        # Botao acao
        self.tx_pedido_cod_cliente.returnPressed.connect(lambda : self.busca_cliente_cod(self.tx_pedido_cod_cliente.text()))
        # Busca cod produto
        self.tx_pedido_cod_produto.setValidator(QtGui.QIntValidator())
        self.tx_pedido_cod_produto.setReadOnly(False)
        self.tx_pedido_cod_produto.returnPressed.connect(lambda : self.localizar_produto_codigo(self.tx_pedido_cod_produto.text()))
        # Focus on return pressed
        self.tx_pedido_cod_cliente.setFocus()
        self.tx_pedido_cod_produto.returnPressed.connect(lambda: self.foco(self.tx_pedido_quantidade))
        self.tx_pedido_quantidade.returnPressed.connect(lambda: self.foco(self.tx_pedido_valor_produto))
        self.tx_pedido_valor_produto.returnPressed.connect(lambda : self.foco_combobox(self.tx_tema))
        self.tx_tema.setCurrentIndex(-1)
        self.tx_tema.currentIndexChanged.connect(lambda : self.foco(self.tx_obs))
        self.tx_obs.returnPressed.connect(self.add_produto_tabela)
        # Campo id Oculto
        self.id_pedido = QtGui.QLineEdit()
        self.id_pedido.setVisible(False)
        # Campo Status
        self.combo_status_pedido.addItem("Status")
        self.combo_status_pedido.addItems(self.pedidos.combo_status_data())
        self.combo_status_pedido.setCurrentIndex(2)
        self.combo_status_pedido.currentIndexChanged.connect(lambda : self.foco(self.tx_pedido_cod_produto))
        # Campo Data Entrega
        self.tx_data_entrega.setDate(QtCore.QDate.currentDate())
        self.tx_data_entrega.dateChanged.connect(lambda :self.foco_combobox(self.combo_status_pedido))
        # Calculo saldo devedor
        self.tx_entrada_pedido.returnPressed.connect(self.saldo_devedor)



        # Botao Concluir PEdido
        efeito = QtGui.QGraphicsDropShadowEffect()
        efeito.setColor(QtGui.QColor("#ff00ff"))
        efeito.setOffset(0, 0)
        efeito.setBlurRadius(15)
        self.bt_concluir_pedido.setGraphicsEffect(efeito)
        self.bt_concluir_pedido.setStyleSheet(" QPushButton{border-radius: 10px; border: none; background: #00ffff;}"
                            "QPushButton:disabled {background: #FFF}"
                            "QPushButton:hover {color: #FFF}")



        # Tamanho, acao  e conteudo tabela  produtos pedido
        self.tabela_pedido_add.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabela_pedido_add.setColumnWidth(0, 30)
        self.tabela_pedido_add.setColumnWidth(1, 150)
        self.tabela_pedido_add.setColumnWidth(2, 80)
        self.tabela_pedido_add.setColumnWidth(3, 80)
        self.tabela_pedido_add.setColumnWidth(4, 120)
        self.tabela_pedido_add.setColumnWidth(5, 210)
        self.tabela_pedido_add.setColumnWidth(6, 70)
        # Remover item
        self.tabela_pedido_add.cellDoubleClicked.connect(self.remover_item_tabela)


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
            self.bt_pedido_localizar_produto.setEnabled(True)
            self.tx_pedido_cod_produto.setEnabled(True)
            self.tx_data_entrega.setFocus()
            self.tx_data_entrega.selectAll()
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
        Janela.tableWidget.horizontalHeader().setVisible(False)
        Janela.tableWidget.cellDoubleClicked.connect(selecionar_cliente_popup)
        Dialog.exec_()

    # Busca Cliente cod
    def busca_cliente_cod(self, cod):
        busca_cliente = CrudCliente()
        busca_cliente.buscar_cliente_selecionado(cod)
        self.tx_pedido_cod_cliente.setText(str(busca_cliente.cod_cliente))
        self.tx_pedido_nome_cliente.setText(busca_cliente.nome_cliente)
        self.tx_pedido_telefone.setText(busca_cliente.telefone)
        self.bt_pedido_localizar_produto.setEnabled(True)
        self.tx_pedido_cod_produto.setEnabled(True)
        self.tx_data_entrega.setFocus()
        self.tx_data_entrega.selectAll()


    # Janela Buscar Produto
    def janela_buscar_produto(self):
        Janela = Ui_DialogBuscarProduto()
        Dialog = QtGui.QDialog()
        Janela.setBuscarProduto(Dialog)
        # Funcao Buscar Produto
        def buscar_produto():
            self.produtos.crud_busca_produto(Janela.tx_busca_produto.text())
            i = 0
            while i < len(self.produtos.descricao):
                Janela.table_busca_produto.insertRow(i)
                Janela.table_busca_produto.setItem(i, 0, QtGui.QTableWidgetItem(str(self.produtos.cod_produto[i])))
                Janela.table_busca_produto.setItem(i, 1, QtGui.QTableWidgetItem(self.produtos.descricao[i]))
                Janela.table_busca_produto.setItem(i, 2, QtGui.QTableWidgetItem(format(self.produtos.valor_venda[i], ".2f")))
                i += 1

        def selecionar_produto(row):
            self.localizar_produto_codigo(Janela.table_busca_produto.item(row, 0).text())
            self.tx_pedido_cod_produto.setText(Janela.table_busca_produto.item(row, 0).text())
            self.tx_pedido_quantidade.setText("1")
            self.bt_pedido_add_produto.setEnabled(True)
            self.tx_pedido_quantidade.setFocus()
            self.tx_pedido_quantidade.selectAll()
            Dialog.close()

        # Campo Buscar produto
        Janela.tx_busca_produto.returnPressed.connect(buscar_produto)
        # Ajustes da Tabela
        Janela.table_busca_produto.setColumnWidth(0, 50)
        Janela.table_busca_produto.setColumnWidth(1, 210)
        Janela.table_busca_produto.setColumnWidth(2, 75)
        Janela.table_busca_produto.cellDoubleClicked.connect(selecionar_produto)
        Dialog.exec_()


    def localizar_produto_codigo(self, cod):
        if len(cod) >= 1:
            self.produtos.busca_edicao(cod)
            self.tx_pedido_cod_produto.setText(str(self.produtos.cod_produto))
            self.tx_pedido_produto.setText(self.produtos.descricao)
            self.tx_pedido_valor_produto.setText(format(self.produtos.valor_venda, ".2f"))
            self.tx_pedido_quantidade.setText("1")
            self.bt_pedido_add_produto.setEnabled(True)



    def add_produto_tabela(self):
        if len(self.tx_pedido_cod_produto.text()) >= 1 :
            self.tabela_pedido_add.insertRow(0)
            self.tabela_pedido_add.setItem(0, 0, QtGui.QTableWidgetItem(self.tx_pedido_cod_produto.text()))
            self.tabela_pedido_add.setItem(0, 1, QtGui.QTableWidgetItem(self.tx_pedido_produto.text()))
            self.tabela_pedido_add.setItem(0, 2, QtGui.QTableWidgetItem(str(self.tx_pedido_quantidade.text())))
            self.tabela_pedido_add.setItem(0, 3, QtGui.QTableWidgetItem(str(self.tx_pedido_valor_produto.text())))
            self.tabela_pedido_add.setItem(0, 4, QtGui.QTableWidgetItem(self.tx_tema.currentText()))
            self.tabela_pedido_add.setItem(0, 5, QtGui.QTableWidgetItem(self.tx_obs.text()))
            total = float(self.tx_pedido_valor_produto.text()) * float(self.tx_pedido_quantidade.text())
            total = format(total, ".2f")
            self.tabela_pedido_add.setItem(0, 6, QtGui.QTableWidgetItem(str(total)))

            self.tx_pedido_cod_produto.clear()
            self.tx_pedido_produto.clear()
            self.tx_pedido_quantidade.clear()
            self.tx_pedido_valor_produto.clear()
            self.tx_tema.setCurrentIndex(-1)
            self.tx_pedido_cod_produto.setFocus()
            self.bt_pedido_add_produto.setEnabled(False)
            self.tx_obs.clear()
            self.soma_total()
            self.bt_cadastrar_pedido.setEnabled(True)



        else:
            self.tx_pedido_cod_produto.setFocus()


    # Soma Total
    def soma_total(self):
        i = 0
        total = 0
        while i < self.tabela_pedido_add.rowCount():
            total = total + float(self.tabela_pedido_add.item(i, 6).text())
            i += 1
        self.tx_total_pedido.setText(format(total, ".2f"))
        self.tx_saldo_devedor_pedido.setText(format(total, ".2f"))

    # Remover Item
    def remover_item_tabela(self, row):
        total = float(self.tx_total_pedido.text()) - float(self.tabela_pedido_add.item(row, 6).text())
        self.tx_total_pedido.setText(format(total, ".2f"))
        self.tabela_pedido_add.removeRow(row)

    #Confirmar e Cadastrar Pedido
    def confirmar_pedido(self):
        Janela = Ui_Dialog_pedido()
        Dialog = QtGui.QDialog()
        Janela.setConfPedido(Dialog)
        Janela.tx_data_entrega.setText(QtCore.QDate.toString(self.tx_data_entrega.date(), "dd-MM-yyyy"))
        Janela.tx_valor_entrada.setText(self.tx_entrada_pedido.text())
        Janela.tx_saldo_devedor.setText(self.tx_total_pedido.text())

        def cadastrar_pedido():
            cadastro = CrudPedidos()
            cadastro.cod_pedido = unicode(self.id_pedido.text()).encode("utf8")
            cadastro.cliente = unicode(self.tx_pedido_cod_cliente.text()).encode("utf8")
            cadastro.data_entrega = QtCore.QDate.toString(self.tx_data_entrega.date(), "yyyy-MM-dd")
            cadastro.status_pedido = self.combo_status_pedido.currentIndex()
            cadastro.entrada = unicode(self.tx_entrada_pedido.text()).encode("utf8")
            cadastro.saldo_devedor = unicode(self.tx_saldo_devedor_pedido.text()).encode("utf8")
            cadastro.valor_total = unicode(self.tx_total_pedido.text()).encode("utf8")
            cadastro.cad_pedido()

            # i = 0;
            # while i < self.tabela_pedido_add.rowCount():
            #     x = 0;
            #     for row in range(row)
            #     i += 1
            for row in range(self.tabela_pedido_add.rowCount()):
                cadastro.id_relacao = ""
                cadastro.produto = self.tabela_pedido_add.item(row, 0).text()
                cadastro.qtde = self.tabela_pedido_add.item(row, 2).text()
                cadastro.valor_produto = self.tabela_pedido_add.item(row, 3).text()
                cadastro.total_produto = self.tabela_pedido_add.item(row, 6).text()
                cadastro.tema = self.tabela_pedido_add.item(row, 4).text()
                cadastro.obs = self.tabela_pedido_add.item(row, 5).text()
                cadastro.cad_pedido_produtos()
            self.cancelar_cad_pedido()


        Janela.bt_ok_pedido.clicked.connect(cadastrar_pedido)
        Dialog.exec_()

    #Cancelar
    def cancelar_cad_pedido(self):
        for filho in self.ct_frame_pedidos.findChildren(QtGui.QLineEdit):
            filho.clear()


        while self.tabela_pedido_add.rowCount() > 0:
            self.tabela_pedido_add.removeRow(0)

    # Funcao foco lineedit
    def foco(self, botao):
        botao.setFocus()
        botao.selectAll()

    def foco_combobox(self, campo):
        campo.setFocus()

    # Buscar Pedidos
    def busca_pedidos(self):

        Dialog = QtGui.QDialog()
        Janela = BuscaPedido()
        Janela.buscaProduos(Dialog)
        def resultado(row):
            # Selecionando Cliente
            self.pedidos.selecionar_pedido(Janela.tableWidget.item(row, 0).text())
            self.busca_cliente_cod(self.pedidos.cliente)
            # Limpando Tabela
            while self.tabela_pedido_add.rowCount() > 0:
                self.tabela_pedido_add.removeRow(0)

            i = 0
            while i < len(self.pedidos.produto):
                self.tabela_pedido_add.insertRow(i)
                self.tabela_pedido_add.setItem(i, 0, QtGui.QTableWidgetItem(str(self.pedidos.cod_produto[i])))
                self.tabela_pedido_add.setItem(i, 1, (QtGui.QTableWidgetItem(self.pedidos.produto[i])))
                self.tabela_pedido_add.setItem(i, 2, (QtGui.QTableWidgetItem(str(self.pedidos.qtde[i]))))
                self.tabela_pedido_add.setItem(i, 3, (QtGui.QTableWidgetItem(format(self.pedidos.valor_produto[i], ".2f"))))
                self.tabela_pedido_add.setItem(i, 4, (QtGui.QTableWidgetItem(str(self.pedidos.tema[i]))))
                self.tabela_pedido_add.setItem(i, 5, (QtGui.QTableWidgetItem(self.pedidos.obs[i])))
                self.tabela_pedido_add.setItem(i, 6, (QtGui.QTableWidgetItem(format(self.pedidos.total_produto[i], ".2f"))))

                i += 1
            self.tx_total_pedido.setText(format(self.pedidos.valor_total, ".2f"))
            self.tx_saldo_devedor_pedido.setText(format(self.pedidos.saldo_devedor, ".2f"))
            self.tx_entrada_pedido.setText(format(self.pedidos.entrada, ".2f"))
            self.bt_cadastrar_pedido.setEnabled(True)


        Janela.tableWidget.cellDoubleClicked.connect(resultado)

        Dialog.exec_()

    # saldo Devedor
    def saldo_devedor(self):
        saldo = float(self.tx_total_pedido.text()) - float(self.tx_entrada_pedido.text())
        self.tx_saldo_devedor_pedido.setText(format(saldo, ".2f"))





