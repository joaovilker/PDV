# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from Views.pedidos import Ui_ct_main_pedido
from Views.confirmacao import Ui_Dialog


class MainPedidos(Ui_ct_main_pedido):
    def main_pedidos(self, frame):
        super(MainPedidos, self).setPedidos(frame)
        self.frame_geral_pedido.show()

        # parametros Inicias
        # Estilo dos Botoes e Background
        # Localizar CLiente
        self.bt_pedido_localizar_cliente.setIcon(QtGui.QIcon('Images/buscar.png'))
        self.bt_pedido_localizar_cliente.setIconSize(QtCore.QSize(20, 20))
        # Add produto
        self.bt_pedido_add_produto.setIcon(QtGui.QIcon('Images/add.png'))
        self.bt_pedido_add_produto.setIconSize(QtCore.QSize(20, 20))
        # Cadastrar Pedido
        self.bt_cadastrar_pedido.setStyleSheet("color: #FFF; border: 2px solid #0CA3D2; border-radius:10px;"
                                               "background: #FFF; color: #000")
        self.bt_cadastrar_pedido.clicked.connect(self.confirmar_pedido)

        # Cancelar_pedido
        self.bt_cancelar_pedido.setText("Cancelar")
        self.bt_cancelar_pedido.setStyleSheet("color: #FFF; border: 2px solid red; border-radius:10px;"
                                              "background: #FFF; color: #000")

        self.tabela_pedido_add.setVerticalHeaderLabels(QtCore.QStringList(["Nome", "Idade"]))

        # Tamanho, acao  e conteudo da tabela produtos
        self.tabela_pedidos.setColumnWidth(0, 140)
        self.tabela_pedidos.setColumnWidth(1, 65)
        self.tabela_pedidos.setColumnWidth(2, 75)
        self.tabela_pedidos.horizontalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        self.tabela_pedidos.verticalHeader().setVisible(False)

    def confirmar_pedido(self):
        Janela = Ui_Dialog()
        Dialog = QtGui.QDialog()
        Janela.setConfirmacao(Dialog)
        Dialog.exec_()
