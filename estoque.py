# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from Views.estoque import Ui_FrameEstoque
from Crud.estoque import CrudProdutos
from Crud.lista_indices import ListasIndices
from Class.Funcoes import Funcoes
from Views.confirmacao import Ui_Dialog


class MainEstoque(Ui_FrameEstoque):

    def main_estoque(self, frame):
        super(MainEstoque, self).setEstoque(frame)
        self.ct_frame_estoque.show()

        # Classes
        self.indices = ListasIndices()
        self.funcoes = Funcoes()

        # Lista Status
        self.indices.lista_status()

        self.tx_cod_produto.setReadOnly(True)


        # Estilo botoes
        self.bt_cad_produto.setStyleSheet("color: #FFF; border: 2px solid #0CA3D2; border-radius:10px;"
                                               "background: #FFF; color: #000")
        self.bt_cancelar.setStyleSheet("color: #FFF; border: 2px solid red; border-radius:10px;"
                                              "background: #FFF; color: #000")

        # Tamanho, acao  e conteudo da tabela produtos
        self.tabela_estoque.setColumnWidth(0, 40)
        self.tabela_estoque.setColumnWidth(1, 205)
        self.tabela_estoque.setColumnWidth(2, 45)
        self.tabela_estoque.horizontalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        self.tabela_estoque.verticalHeader().setVisible(False)
        self.tabela_estoque.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        #Selecionar da Tabela
        self.tabela_estoque.cellDoubleClicked.connect(self.selecionar)

        # #Acao
        # Cadastro
        self.bt_cad_produto.clicked.connect(self.confirmar)
        # Cancelar
        self.bt_cancelar.clicked.connect(self.cancelar)

        # Preencher a tabela
        self.busca_produto()


        # Buscar da Tabela
        self.tx_buscar_produto.returnPressed.connect(self.busca_produto)

    def selecionar(self, row):
        busca = CrudProdutos()
        busca.busca_edicao(str(self.tabela_estoque.item(row, 0).text()))
        self.tx_cod_produto.setText(str(busca.cod_produto))
        self.tx_produto.setText(unicode(busca.descricao))
        self.tx_quantidade.setText(str(busca.qtde_disponivel))
        self.tx_quantidade_min.setText(str(busca.qtde_minima))
        self.tx_preco_de_compra.setText(format(busca.valor_compra, ".2f"))
        self.tx_preco_de_venda.setText(format(busca.valor_venda, ".2f"))
        self.tx_obs_estoque.setPlainText(busca.obs)

        return False

    def cancelar(self):
        for filho in self.ct_estoque.findChildren(QtGui.QLineEdit):
            filho.clear()

        self.tx_obs_estoque.clear()

    # Busca Campo pesquisa e listagem da tabela
    def busca_produto(self):
        # self.campo =  self.tx_buscar_produto.text()
        #
        # if len(self.campo) > 3:
        #     print self.tx_buscar_produto.text()
        while self.tabela_estoque.rowCount() > 0:
            self.tabela_estoque.removeRow(0)
        busca = CrudProdutos()
        busca.crud_busca_produto(unicode(self.tx_buscar_produto.text()).encode("utf-8"))

        i = 0
        while i < len(busca.descricao):
            self.tabela_estoque.insertRow(i)
            self.tabela_estoque.setItem(i, 0, QtGui.QTableWidgetItem(str(busca.cod_produto[i])))
            self.tabela_estoque.setItem(i, 1, QtGui.QTableWidgetItem(busca.descricao[i]))
            self.tabela_estoque.setItem(i, 2, QtGui.QTableWidgetItem(str(busca.qtde_disponivel[i])))
            i += 1

    # Janela de Confirmação
    def confirmar(self):
        Janela = Ui_Dialog()
        Dialog = QtGui.QDialog()
        Janela.setConfirmacao(Dialog)
        Janela.lb_info.setText("Produto:")
        Janela.lb_titulo_modal.setText("Cadastrar / Atualizar?")
        Janela.lb_descricao.setText(unicode(self.tx_produto.text()))
        Janela.buttonBox.width()
        Janela.buttonBox.setStyleSheet("color: #FFF; border: 2px solid #0CA3D2; border-radius:10px;"
                                               "background: #FFF; color: #000; width: 100px; height: 30px")
        QtCore.QObject.connect(Janela.buttonBox, QtCore.SIGNAL("accepted()"), self.cadastra_produto)
        Dialog.exec_()


    # Cadastro / Atualização de produto
    def cadastra_produto(self):
        cadastro = CrudProdutos()
        cadastro.cod_produto = unicode(self.tx_cod_produto.text()).encode("utf8")
        cadastro.descricao = unicode(self.tx_produto.text()).encode("utf8")
        cadastro.qtde_minima = unicode(self.tx_quantidade_min.text()).encode("utf8")
        cadastro.qtde_disponivel = unicode(self.tx_quantidade.text()).encode("utf8")
        cadastro.valor_compra = unicode(self.tx_preco_de_compra.text()).encode("utf8")
        cadastro.valor_venda = unicode(self.tx_preco_de_venda.text()).encode("utf8")
        cadastro.fornecedor = unicode(self.tx_fornecedor_estoque.currentText()).encode("utf8")
        cadastro.obs = unicode(self.tx_obs_estoque.toPlainText()).encode("utf8")
        cadastro.cadastra_produto()

        for filho in self.ct_estoque.findChildren(QtGui.QLineEdit):
            filho.clear()

        self.tx_obs_estoque.clear()
        self.tx_buscar_produto.clear()
        self.busca_produto()









