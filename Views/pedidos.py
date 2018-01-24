# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pedidos.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ct_main_pedido(object):
    def setPedidos(self, ct_main_pedido):
        ct_main_pedido.setObjectName(_fromUtf8("ct_main_pedido"))
        ct_main_pedido.resize(900, 493)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        ct_main_pedido.setFont(font)
        ct_main_pedido.setStyleSheet(_fromUtf8(""))
        ct_main_pedido.setFrameShape(QtGui.QFrame.StyledPanel)
        ct_main_pedido.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_geral_pedido = QtGui.QFrame(ct_main_pedido)
        self.frame_geral_pedido.setGeometry(QtCore.QRect(0, 0, 900, 493))
        self.frame_geral_pedido.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.frame_geral_pedido.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_geral_pedido.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_geral_pedido.setObjectName(_fromUtf8("frame_geral_pedido"))
        self.ct_frame_pedidos = QtGui.QFrame(self.frame_geral_pedido)
        self.ct_frame_pedidos.setGeometry(QtCore.QRect(30, 20, 500, 423))
        self.ct_frame_pedidos.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 5px solid #fFf;\n"
"border-radius: 20px;\n"
""))
        self.ct_frame_pedidos.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_frame_pedidos.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_pedidos.setObjectName(_fromUtf8("ct_frame_pedidos"))
        self.lb_agendar_pedido = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_agendar_pedido.setGeometry(QtCore.QRect(25, 10, 450, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.lb_agendar_pedido.setFont(font)
        self.lb_agendar_pedido.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_agendar_pedido.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_agendar_pedido.setObjectName(_fromUtf8("lb_agendar_pedido"))
        self.lb_cliente_pedido = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_cliente_pedido.setGeometry(QtCore.QRect(25, 60, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_cliente_pedido.setFont(font)
        self.lb_cliente_pedido.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_cliente_pedido.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_cliente_pedido.setObjectName(_fromUtf8("lb_cliente_pedido"))
        self.tx_pedido_cod_cliente = QtGui.QLineEdit(self.ct_frame_pedidos)
        self.tx_pedido_cod_cliente.setGeometry(QtCore.QRect(135, 60, 40, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_pedido_cod_cliente.setFont(font)
        self.tx_pedido_cod_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:8px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_pedido_cod_cliente.setReadOnly(True)
        self.tx_pedido_cod_cliente.setObjectName(_fromUtf8("tx_pedido_cod_cliente"))
        self.bt_pedido_localizar_cliente = QtGui.QPushButton(self.ct_frame_pedidos)
        self.bt_pedido_localizar_cliente.setGeometry(QtCore.QRect(445, 55, 30, 30))
        self.bt_pedido_localizar_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.bt_pedido_localizar_cliente.setText(_fromUtf8(""))
        self.bt_pedido_localizar_cliente.setIconSize(QtCore.QSize(20, 20))
        self.bt_pedido_localizar_cliente.setObjectName(_fromUtf8("bt_pedido_localizar_cliente"))
        self.lb_telefone_pedido = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_telefone_pedido.setGeometry(QtCore.QRect(25, 95, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_telefone_pedido.setFont(font)
        self.lb_telefone_pedido.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_telefone_pedido.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_telefone_pedido.setObjectName(_fromUtf8("lb_telefone_pedido"))
        self.tx_pedido_telefone = QtGui.QLineEdit(self.ct_frame_pedidos)
        self.tx_pedido_telefone.setGeometry(QtCore.QRect(135, 95, 305, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_pedido_telefone.setFont(font)
        self.tx_pedido_telefone.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_pedido_telefone.setObjectName(_fromUtf8("tx_pedido_telefone"))
        self.lb_produto_pedido = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_produto_pedido.setGeometry(QtCore.QRect(25, 165, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_produto_pedido.setFont(font)
        self.lb_produto_pedido.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_produto_pedido.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produto_pedido.setObjectName(_fromUtf8("lb_produto_pedido"))
        self.bt_pedido_add_produto = QtGui.QPushButton(self.ct_frame_pedidos)
        self.bt_pedido_add_produto.setGeometry(QtCore.QRect(290, 195, 30, 30))
        self.bt_pedido_add_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.bt_pedido_add_produto.setText(_fromUtf8(""))
        self.bt_pedido_add_produto.setIconSize(QtCore.QSize(20, 20))
        self.bt_pedido_add_produto.setObjectName(_fromUtf8("bt_pedido_add_produto"))
        self.tx_pedido_produto = QtGui.QComboBox(self.ct_frame_pedidos)
        self.tx_pedido_produto.setGeometry(QtCore.QRect(135, 165, 305, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_pedido_produto.setFont(font)
        self.tx_pedido_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_pedido_produto.setObjectName(_fromUtf8("tx_pedido_produto"))
        self.lb_produto_quantidade = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_produto_quantidade.setGeometry(QtCore.QRect(25, 200, 70, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_produto_quantidade.setFont(font)
        self.lb_produto_quantidade.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_produto_quantidade.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produto_quantidade.setObjectName(_fromUtf8("lb_produto_quantidade"))
        self.tx_pedido_quantidade = QtGui.QLineEdit(self.ct_frame_pedidos)
        self.tx_pedido_quantidade.setGeometry(QtCore.QRect(100, 200, 30, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_pedido_quantidade.setFont(font)
        self.tx_pedido_quantidade.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:7px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_pedido_quantidade.setObjectName(_fromUtf8("tx_pedido_quantidade"))
        self.lb_produto_quantidade_2 = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_produto_quantidade_2.setGeometry(QtCore.QRect(25, 130, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_produto_quantidade_2.setFont(font)
        self.lb_produto_quantidade_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_produto_quantidade_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produto_quantidade_2.setObjectName(_fromUtf8("lb_produto_quantidade_2"))
        self.tx_data_pedido = QtGui.QDateEdit(self.ct_frame_pedidos)
        self.tx_data_pedido.setGeometry(QtCore.QRect(135, 130, 95, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_data_pedido.setFont(font)
        self.tx_data_pedido.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_data_pedido.setCalendarPopup(True)
        self.tx_data_pedido.setObjectName(_fromUtf8("tx_data_pedido"))
        self.lb_produto_quantidade_3 = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_produto_quantidade_3.setGeometry(QtCore.QRect(140, 200, 60, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_produto_quantidade_3.setFont(font)
        self.lb_produto_quantidade_3.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_produto_quantidade_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produto_quantidade_3.setObjectName(_fromUtf8("lb_produto_quantidade_3"))
        self.tx_pedido_quantidade_2 = QtGui.QLineEdit(self.ct_frame_pedidos)
        self.tx_pedido_quantidade_2.setGeometry(QtCore.QRect(210, 200, 70, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_pedido_quantidade_2.setFont(font)
        self.tx_pedido_quantidade_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_pedido_quantidade_2.setObjectName(_fromUtf8("tx_pedido_quantidade_2"))
        self.tabela_pedido_add = QtGui.QTableWidget(self.ct_frame_pedidos)
        self.tabela_pedido_add.setGeometry(QtCore.QRect(25, 235, 450, 130))
        self.tabela_pedido_add.setStyleSheet(_fromUtf8("background: #FFF; border: none; border-radius: 0"))
        self.tabela_pedido_add.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabela_pedido_add.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tabela_pedido_add.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tabela_pedido_add.setShowGrid(True)
        self.tabela_pedido_add.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_pedido_add.setObjectName(_fromUtf8("tabela_pedido_add"))
        self.tabela_pedido_add.setColumnCount(5)
        self.tabela_pedido_add.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabela_pedido_add.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_pedido_add.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_pedido_add.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_pedido_add.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_pedido_add.setHorizontalHeaderItem(4, item)
        self.tabela_pedido_add.verticalHeader().setVisible(False)
        self.bt_cadastrar_pedido = QtGui.QPushButton(self.ct_frame_pedidos)
        self.bt_cadastrar_pedido.setGeometry(QtCore.QRect(25, 370, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cadastrar_pedido.setFont(font)
        self.bt_cadastrar_pedido.setObjectName(_fromUtf8("bt_cadastrar_pedido"))
        self.bt_cancelar_pedido = QtGui.QPushButton(self.ct_frame_pedidos)
        self.bt_cancelar_pedido.setGeometry(QtCore.QRect(125, 370, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cancelar_pedido.setFont(font)
        self.bt_cancelar_pedido.setObjectName(_fromUtf8("bt_cancelar_pedido"))
        self.lb_produto_quantidade_4 = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_produto_quantidade_4.setGeometry(QtCore.QRect(240, 130, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_produto_quantidade_4.setFont(font)
        self.lb_produto_quantidade_4.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_produto_quantidade_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produto_quantidade_4.setObjectName(_fromUtf8("lb_produto_quantidade_4"))
        self.tx_data_notificacao = QtGui.QDateEdit(self.ct_frame_pedidos)
        self.tx_data_notificacao.setGeometry(QtCore.QRect(350, 130, 90, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_data_notificacao.setFont(font)
        self.tx_data_notificacao.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_data_notificacao.setCalendarPopup(True)
        self.tx_data_notificacao.setObjectName(_fromUtf8("tx_data_notificacao"))
        self.bt_concluir_pedido = QtGui.QPushButton(self.ct_frame_pedidos)
        self.bt_concluir_pedido.setGeometry(QtCore.QRect(225, 370, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_concluir_pedido.setFont(font)
        self.bt_concluir_pedido.setObjectName(_fromUtf8("bt_concluir_pedido"))
        self.lb_cliente_pedido_2 = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_cliente_pedido_2.setGeometry(QtCore.QRect(185, 60, 70, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_cliente_pedido_2.setFont(font)
        self.lb_cliente_pedido_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_cliente_pedido_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_cliente_pedido_2.setObjectName(_fromUtf8("lb_cliente_pedido_2"))
        self.tx_pedido_nome_cliente = QtGui.QLineEdit(self.ct_frame_pedidos)
        self.tx_pedido_nome_cliente.setGeometry(QtCore.QRect(265, 60, 170, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_pedido_nome_cliente.setFont(font)
        self.tx_pedido_nome_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_pedido_nome_cliente.setReadOnly(True)
        self.tx_pedido_nome_cliente.setObjectName(_fromUtf8("tx_pedido_nome_cliente"))
        self.ct_frame_pedidos_pendente = QtGui.QFrame(self.frame_geral_pedido)
        self.ct_frame_pedidos_pendente.setGeometry(QtCore.QRect(570, 20, 300, 423))
        self.ct_frame_pedidos_pendente.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 2px solid #fff;\n"
"border-radius: 20px;"))
        self.ct_frame_pedidos_pendente.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_frame_pedidos_pendente.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_pedidos_pendente.setObjectName(_fromUtf8("ct_frame_pedidos_pendente"))
        self.lb_pedidos_agendados = QtGui.QLabel(self.ct_frame_pedidos_pendente)
        self.lb_pedidos_agendados.setGeometry(QtCore.QRect(50, 10, 200, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.lb_pedidos_agendados.setFont(font)
        self.lb_pedidos_agendados.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_pedidos_agendados.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_pedidos_agendados.setObjectName(_fromUtf8("lb_pedidos_agendados"))
        self.tabela_pedidos = QtGui.QTableWidget(self.ct_frame_pedidos_pendente)
        self.tabela_pedidos.setGeometry(QtCore.QRect(5, 60, 290, 250))
        self.tabela_pedidos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabela_pedidos.setObjectName(_fromUtf8("tabela_pedidos"))
        self.tabela_pedidos.setColumnCount(3)
        self.tabela_pedidos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabela_pedidos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_pedidos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_pedidos.setHorizontalHeaderItem(2, item)
        self.tabela_pedidos.verticalHeader().setVisible(False)
        self.tx_buscar_pedidos = QtGui.QLineEdit(self.ct_frame_pedidos_pendente)
        self.tx_buscar_pedidos.setGeometry(QtCore.QRect(50, 370, 200, 30))
        self.tx_buscar_pedidos.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_buscar_pedidos.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_buscar_pedidos.setObjectName(_fromUtf8("tx_buscar_pedidos"))
        self.label_buscar_tarefa = QtGui.QLabel(self.ct_frame_pedidos_pendente)
        self.label_buscar_tarefa.setGeometry(QtCore.QRect(100, 340, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_buscar_tarefa.setFont(font)
        self.label_buscar_tarefa.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF url(\'/Files/Python/AeR/Images/buscar.png\') no-repeat  right ;\n"
"color: #000;\n"
""))
        self.label_buscar_tarefa.setTextFormat(QtCore.Qt.AutoText)
        self.label_buscar_tarefa.setAlignment(QtCore.Qt.AlignCenter)
        self.label_buscar_tarefa.setObjectName(_fromUtf8("label_buscar_tarefa"))

        self.tradPedidos(ct_main_pedido)
        QtCore.QMetaObject.connectSlotsByName(ct_main_pedido)

    def tradPedidos(self, ct_main_pedido):
        ct_main_pedido.setWindowTitle(_translate("ct_main_pedido", "Frame", None))
        self.lb_agendar_pedido.setText(_translate("ct_main_pedido", "Editor de Pedido", None))
        self.lb_cliente_pedido.setText(_translate("ct_main_pedido", "Cod. Cliente", None))
        self.lb_telefone_pedido.setText(_translate("ct_main_pedido", "Telefone", None))
        self.lb_produto_pedido.setText(_translate("ct_main_pedido", "Produto", None))
        self.lb_produto_quantidade.setText(_translate("ct_main_pedido", "Quant.", None))
        self.lb_produto_quantidade_2.setText(_translate("ct_main_pedido", "Data Agendada", None))
        self.lb_produto_quantidade_3.setText(_translate("ct_main_pedido", "Valor", None))
        item = self.tabela_pedido_add.horizontalHeaderItem(0)
        item.setText(_translate("ct_main_pedido", "Produto", None))
        item = self.tabela_pedido_add.horizontalHeaderItem(1)
        item.setText(_translate("ct_main_pedido", "Qtde.", None))
        item = self.tabela_pedido_add.horizontalHeaderItem(2)
        item.setText(_translate("ct_main_pedido", "Valor", None))
        item = self.tabela_pedido_add.horizontalHeaderItem(3)
        item.setText(_translate("ct_main_pedido", "Total", None))
        self.bt_cadastrar_pedido.setText(_translate("ct_main_pedido", "Cadastrar", None))
        self.bt_cancelar_pedido.setText(_translate("ct_main_pedido", "Cancelar", None))
        self.lb_produto_quantidade_4.setText(_translate("ct_main_pedido", "Data Notificar", None))
        self.bt_concluir_pedido.setText(_translate("ct_main_pedido", "Concluir", None))
        self.lb_cliente_pedido_2.setText(_translate("ct_main_pedido", "Nome", None))
        self.lb_pedidos_agendados.setText(_translate("ct_main_pedido", "Pedidos Pendentes", None))
        item = self.tabela_pedidos.horizontalHeaderItem(0)
        item.setText(_translate("ct_main_pedido", "Cod", None))
        item = self.tabela_pedidos.horizontalHeaderItem(1)
        item.setText(_translate("ct_main_pedido", "Data", None))
        item = self.tabela_pedidos.horizontalHeaderItem(2)
        item.setText(_translate("ct_main_pedido", "Cliente", None))
        self.tx_buscar_pedidos.setPlaceholderText(_translate("ct_main_pedido", "Buscar", None))
        self.label_buscar_tarefa.setText(_translate("ct_main_pedido", "Pesquisar", None))

