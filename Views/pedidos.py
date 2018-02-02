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
        ct_main_pedido.resize(900, 524)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        ct_main_pedido.setFont(font)
        ct_main_pedido.setStyleSheet(_fromUtf8(""))
        ct_main_pedido.setFrameShape(QtGui.QFrame.StyledPanel)
        ct_main_pedido.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_geral_pedido = QtGui.QFrame(ct_main_pedido)
        self.frame_geral_pedido.setGeometry(QtCore.QRect(0, 0, 900, 524))
        self.frame_geral_pedido.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.frame_geral_pedido.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_geral_pedido.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_geral_pedido.setObjectName(_fromUtf8("frame_geral_pedido"))
        self.ct_frame_pedidos = QtGui.QFrame(self.frame_geral_pedido)
        self.ct_frame_pedidos.setGeometry(QtCore.QRect(30, 20, 840, 453))
        self.ct_frame_pedidos.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 5px solid #fFf;\n"
"border-radius: 20px;\n"
""))
        self.ct_frame_pedidos.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_frame_pedidos.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_pedidos.setObjectName(_fromUtf8("ct_frame_pedidos"))
        self.lb_agendar_pedido = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_agendar_pedido.setGeometry(QtCore.QRect(200, 10, 440, 30))
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
        self.lb_cliente_pedido.setGeometry(QtCore.QRect(25, 85, 100, 25))
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
        self.tx_pedido_cod_cliente.setGeometry(QtCore.QRect(135, 85, 40, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_pedido_cod_cliente.setFont(font)
        self.tx_pedido_cod_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:8px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_pedido_cod_cliente.setObjectName(_fromUtf8("tx_pedido_cod_cliente"))
        self.bt_pedido_localizar_cliente = QtGui.QPushButton(self.ct_frame_pedidos)
        self.bt_pedido_localizar_cliente.setGeometry(QtCore.QRect(720, 80, 40, 30))
        self.bt_pedido_localizar_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.bt_pedido_localizar_cliente.setText(_fromUtf8(""))
        self.bt_pedido_localizar_cliente.setIconSize(QtCore.QSize(20, 20))
        self.bt_pedido_localizar_cliente.setObjectName(_fromUtf8("bt_pedido_localizar_cliente"))
        self.lb_telefone_pedido = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_telefone_pedido.setGeometry(QtCore.QRect(450, 85, 100, 25))
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
        self.tx_pedido_telefone.setGeometry(QtCore.QRect(570, 85, 135, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_pedido_telefone.setFont(font)
        self.tx_pedido_telefone.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_pedido_telefone.setReadOnly(True)
        self.tx_pedido_telefone.setObjectName(_fromUtf8("tx_pedido_telefone"))
        self.lb_produto_pedido = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_produto_pedido.setGeometry(QtCore.QRect(25, 155, 100, 25))
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
        self.bt_pedido_add_produto.setEnabled(False)
        self.bt_pedido_add_produto.setGeometry(QtCore.QRect(720, 185, 40, 30))
        self.bt_pedido_add_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.bt_pedido_add_produto.setText(_fromUtf8(""))
        self.bt_pedido_add_produto.setIconSize(QtCore.QSize(20, 20))
        self.bt_pedido_add_produto.setObjectName(_fromUtf8("bt_pedido_add_produto"))
        self.lb_produto_quantidade = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_produto_quantidade.setGeometry(QtCore.QRect(445, 155, 70, 25))
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
        self.tx_pedido_quantidade.setEnabled(False)
        self.tx_pedido_quantidade.setGeometry(QtCore.QRect(525, 155, 30, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_pedido_quantidade.setFont(font)
        self.tx_pedido_quantidade.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:7px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_pedido_quantidade.setObjectName(_fromUtf8("tx_pedido_quantidade"))
        self.lb_produto_quantidade_3 = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_produto_quantidade_3.setGeometry(QtCore.QRect(565, 155, 60, 25))
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
        self.tx_pedido_valor_produto = QtGui.QLineEdit(self.ct_frame_pedidos)
        self.tx_pedido_valor_produto.setGeometry(QtCore.QRect(635, 155, 70, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_pedido_valor_produto.setFont(font)
        self.tx_pedido_valor_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_pedido_valor_produto.setObjectName(_fromUtf8("tx_pedido_valor_produto"))
        self.tabela_pedido_add = QtGui.QTableWidget(self.ct_frame_pedidos)
        self.tabela_pedido_add.setGeometry(QtCore.QRect(25, 225, 790, 150))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(8)
        self.tabela_pedido_add.setFont(font)
        self.tabela_pedido_add.setStyleSheet(_fromUtf8("background: #FFF; border: none; border-radius: 0"))
        self.tabela_pedido_add.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabela_pedido_add.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabela_pedido_add.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tabela_pedido_add.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tabela_pedido_add.setShowGrid(True)
        self.tabela_pedido_add.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_pedido_add.setObjectName(_fromUtf8("tabela_pedido_add"))
        self.tabela_pedido_add.setColumnCount(7)
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
        item = QtGui.QTableWidgetItem()
        self.tabela_pedido_add.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_pedido_add.setHorizontalHeaderItem(6, item)
        self.tabela_pedido_add.verticalHeader().setVisible(False)
        self.lb_cliente_pedido_2 = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_cliente_pedido_2.setGeometry(QtCore.QRect(185, 85, 70, 25))
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
        self.tx_pedido_nome_cliente.setGeometry(QtCore.QRect(265, 85, 170, 25))
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
        self.tx_pedido_cod_produto = QtGui.QLineEdit(self.ct_frame_pedidos)
        self.tx_pedido_cod_produto.setEnabled(False)
        self.tx_pedido_cod_produto.setGeometry(QtCore.QRect(135, 155, 40, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_pedido_cod_produto.setFont(font)
        self.tx_pedido_cod_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:8px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_pedido_cod_produto.setReadOnly(True)
        self.tx_pedido_cod_produto.setObjectName(_fromUtf8("tx_pedido_cod_produto"))
        self.lb_cliente_pedido_3 = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_cliente_pedido_3.setGeometry(QtCore.QRect(185, 155, 70, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_cliente_pedido_3.setFont(font)
        self.lb_cliente_pedido_3.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_cliente_pedido_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_cliente_pedido_3.setObjectName(_fromUtf8("lb_cliente_pedido_3"))
        self.bt_pedido_localizar_produto = QtGui.QPushButton(self.ct_frame_pedidos)
        self.bt_pedido_localizar_produto.setEnabled(False)
        self.bt_pedido_localizar_produto.setGeometry(QtCore.QRect(720, 150, 40, 30))
        self.bt_pedido_localizar_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.bt_pedido_localizar_produto.setText(_fromUtf8(""))
        self.bt_pedido_localizar_produto.setIconSize(QtCore.QSize(20, 20))
        self.bt_pedido_localizar_produto.setObjectName(_fromUtf8("bt_pedido_localizar_produto"))
        self.tx_pedido_produto = QtGui.QLineEdit(self.ct_frame_pedidos)
        self.tx_pedido_produto.setGeometry(QtCore.QRect(265, 155, 170, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_pedido_produto.setFont(font)
        self.tx_pedido_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_pedido_produto.setReadOnly(True)
        self.tx_pedido_produto.setObjectName(_fromUtf8("tx_pedido_produto"))
        self.tx_total_pedido = QtGui.QLineEdit(self.ct_frame_pedidos)
        self.tx_total_pedido.setGeometry(QtCore.QRect(750, 390, 70, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setBold(False)
        font.setWeight(50)
        self.tx_total_pedido.setFont(font)
        self.tx_total_pedido.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_total_pedido.setText(_fromUtf8(""))
        self.tx_total_pedido.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_total_pedido.setReadOnly(True)
        self.tx_total_pedido.setObjectName(_fromUtf8("tx_total_pedido"))
        self.lb_produto_quantidade_5 = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_produto_quantidade_5.setGeometry(QtCore.QRect(660, 390, 80, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lb_produto_quantidade_5.setFont(font)
        self.lb_produto_quantidade_5.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_produto_quantidade_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produto_quantidade_5.setObjectName(_fromUtf8("lb_produto_quantidade_5"))
        self.lb_dados = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_dados.setGeometry(QtCore.QRect(25, 55, 80, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        font.setBold(True)
        font.setWeight(75)
        self.lb_dados.setFont(font)
        self.lb_dados.setObjectName(_fromUtf8("lb_dados"))
        self.lb_produto_pedido_2 = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_produto_pedido_2.setGeometry(QtCore.QRect(25, 190, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_produto_pedido_2.setFont(font)
        self.lb_produto_pedido_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_produto_pedido_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produto_pedido_2.setObjectName(_fromUtf8("lb_produto_pedido_2"))
        self.lb_produto_pedido_3 = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_produto_pedido_3.setGeometry(QtCore.QRect(265, 190, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_produto_pedido_3.setFont(font)
        self.lb_produto_pedido_3.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_produto_pedido_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produto_pedido_3.setObjectName(_fromUtf8("lb_produto_pedido_3"))
        self.tx_obs = QtGui.QLineEdit(self.ct_frame_pedidos)
        self.tx_obs.setGeometry(QtCore.QRect(375, 190, 330, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_obs.setFont(font)
        self.tx_obs.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tx_obs.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_obs.setFrame(False)
        self.tx_obs.setReadOnly(True)
        self.tx_obs.setObjectName(_fromUtf8("tx_obs"))
        self.tx_tema = QtGui.QComboBox(self.ct_frame_pedidos)
        self.tx_tema.setGeometry(QtCore.QRect(130, 190, 125, 25))
        self.tx_tema.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_tema.setEditable(True)
        self.tx_tema.setFrame(False)
        self.tx_tema.setObjectName(_fromUtf8("tx_tema"))
        self.lb_cliente_pedido_4 = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_cliente_pedido_4.setGeometry(QtCore.QRect(25, 120, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_cliente_pedido_4.setFont(font)
        self.lb_cliente_pedido_4.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_cliente_pedido_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_cliente_pedido_4.setObjectName(_fromUtf8("lb_cliente_pedido_4"))
        self.tx_data_entrega = QtGui.QDateEdit(self.ct_frame_pedidos)
        self.tx_data_entrega.setGeometry(QtCore.QRect(135, 120, 120, 25))
        self.tx_data_entrega.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:8px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_data_entrega.setFrame(False)
        self.tx_data_entrega.setDisplayFormat(_fromUtf8("dd/MM/yyyy"))
        self.tx_data_entrega.setCalendarPopup(True)
        self.tx_data_entrega.setObjectName(_fromUtf8("tx_data_entrega"))
        self.lb_cliente_pedido_5 = QtGui.QLabel(self.ct_frame_pedidos)
        self.lb_cliente_pedido_5.setGeometry(QtCore.QRect(265, 120, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_cliente_pedido_5.setFont(font)
        self.lb_cliente_pedido_5.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_cliente_pedido_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_cliente_pedido_5.setObjectName(_fromUtf8("lb_cliente_pedido_5"))
        self.combo_status_pedido = QtGui.QComboBox(self.ct_frame_pedidos)
        self.combo_status_pedido.setGeometry(QtCore.QRect(375, 120, 100, 25))
        self.combo_status_pedido.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.combo_status_pedido.setObjectName(_fromUtf8("combo_status_pedido"))
        self.bt_cadastrar_pedido_2 = QtGui.QPushButton(self.frame_geral_pedido)
        self.bt_cadastrar_pedido_2.setGeometry(QtCore.QRect(610, 480, 120, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cadastrar_pedido_2.setFont(font)
        self.bt_cadastrar_pedido_2.setObjectName(_fromUtf8("bt_cadastrar_pedido_2"))
        self.bt_cadastrar_pedido_3 = QtGui.QPushButton(self.frame_geral_pedido)
        self.bt_cadastrar_pedido_3.setGeometry(QtCore.QRect(470, 480, 120, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cadastrar_pedido_3.setFont(font)
        self.bt_cadastrar_pedido_3.setObjectName(_fromUtf8("bt_cadastrar_pedido_3"))
        self.bt_cadastrar_pedido = QtGui.QPushButton(self.frame_geral_pedido)
        self.bt_cadastrar_pedido.setGeometry(QtCore.QRect(50, 480, 120, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cadastrar_pedido.setFont(font)
        self.bt_cadastrar_pedido.setObjectName(_fromUtf8("bt_cadastrar_pedido"))
        self.bt_cancelar_pedido = QtGui.QPushButton(self.frame_geral_pedido)
        self.bt_cancelar_pedido.setGeometry(QtCore.QRect(190, 480, 120, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cancelar_pedido.setFont(font)
        self.bt_cancelar_pedido.setObjectName(_fromUtf8("bt_cancelar_pedido"))
        self.bt_concluir_pedido = QtGui.QPushButton(self.frame_geral_pedido)
        self.bt_concluir_pedido.setEnabled(False)
        self.bt_concluir_pedido.setGeometry(QtCore.QRect(330, 480, 120, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_concluir_pedido.setFont(font)
        self.bt_concluir_pedido.setObjectName(_fromUtf8("bt_concluir_pedido"))

        self.tradpedidos(ct_main_pedido)
        QtCore.QMetaObject.connectSlotsByName(ct_main_pedido)

    def tradpedidos(self, ct_main_pedido):
        ct_main_pedido.setWindowTitle(_translate("ct_main_pedido", "Frame", None))
        self.lb_agendar_pedido.setText(_translate("ct_main_pedido", "Cadastrar / Editar Pedido", None))
        self.lb_cliente_pedido.setText(_translate("ct_main_pedido", "Cod", None))
        self.lb_telefone_pedido.setText(_translate("ct_main_pedido", "Telefone", None))
        self.lb_produto_pedido.setText(_translate("ct_main_pedido", "Cod Produto", None))
        self.lb_produto_quantidade.setText(_translate("ct_main_pedido", "Quant.", None))
        self.lb_produto_quantidade_3.setText(_translate("ct_main_pedido", "Valor", None))
        item = self.tabela_pedido_add.horizontalHeaderItem(0)
        item.setText(_translate("ct_main_pedido", "cod", None))
        item = self.tabela_pedido_add.horizontalHeaderItem(1)
        item.setText(_translate("ct_main_pedido", "Produto", None))
        item = self.tabela_pedido_add.horizontalHeaderItem(2)
        item.setText(_translate("ct_main_pedido", "Qtde.", None))
        item = self.tabela_pedido_add.horizontalHeaderItem(3)
        item.setText(_translate("ct_main_pedido", "Valor", None))
        item = self.tabela_pedido_add.horizontalHeaderItem(4)
        item.setText(_translate("ct_main_pedido", "Tema", None))
        item = self.tabela_pedido_add.horizontalHeaderItem(5)
        item.setText(_translate("ct_main_pedido", "Obs", None))
        item = self.tabela_pedido_add.horizontalHeaderItem(6)
        item.setText(_translate("ct_main_pedido", "Total", None))
        self.lb_cliente_pedido_2.setText(_translate("ct_main_pedido", "Nome", None))
        self.lb_cliente_pedido_3.setText(_translate("ct_main_pedido", "Produto", None))
        self.tx_total_pedido.setPlaceholderText(_translate("ct_main_pedido", "Total", None))
        self.lb_produto_quantidade_5.setText(_translate("ct_main_pedido", "Total R$:", None))
        self.lb_dados.setText(_translate("ct_main_pedido", "Cliente:", None))
        self.lb_produto_pedido_2.setText(_translate("ct_main_pedido", "Tema", None))
        self.lb_produto_pedido_3.setText(_translate("ct_main_pedido", "Obs.", None))
        self.lb_cliente_pedido_4.setText(_translate("ct_main_pedido", "Data Entrega", None))
        self.lb_cliente_pedido_5.setText(_translate("ct_main_pedido", "Status", None))
        self.bt_cadastrar_pedido_2.setText(_translate("ct_main_pedido", "Buscar Pedidos", None))
        self.bt_cadastrar_pedido_3.setText(_translate("ct_main_pedido", "Temas", None))
        self.bt_cadastrar_pedido.setText(_translate("ct_main_pedido", "Cadastrar", None))
        self.bt_cancelar_pedido.setText(_translate("ct_main_pedido", "Cancelar", None))
        self.bt_concluir_pedido.setText(_translate("ct_main_pedido", "Concluir", None))

