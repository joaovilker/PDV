# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estoque.ui'
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

class Ui_FrameEstoque(object):
    def setEstoque(self, FrameEstoque):
        FrameEstoque.setObjectName(_fromUtf8("FrameEstoque"))
        FrameEstoque.resize(900, 493)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        FrameEstoque.setFont(font)
        FrameEstoque.setStyleSheet(_fromUtf8(""))
        FrameEstoque.setFrameShape(QtGui.QFrame.StyledPanel)
        FrameEstoque.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_estoque = QtGui.QFrame(FrameEstoque)
        self.ct_frame_estoque.setGeometry(QtCore.QRect(0, 0, 900, 493))
        self.ct_frame_estoque.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.ct_frame_estoque.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_frame_estoque.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_estoque.setObjectName(_fromUtf8("ct_frame_estoque"))
        self.ct_estoque = QtGui.QFrame(self.ct_frame_estoque)
        self.ct_estoque.setGeometry(QtCore.QRect(30, 20, 500, 423))
        self.ct_estoque.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 5px solid #fFf;\n"
"border-radius: 20px;\n"
""))
        self.ct_estoque.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_estoque.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_estoque.setObjectName(_fromUtf8("ct_estoque"))
        self.lb_header_1 = QtGui.QLabel(self.ct_estoque)
        self.lb_header_1.setGeometry(QtCore.QRect(25, 10, 450, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.lb_header_1.setFont(font)
        self.lb_header_1.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_header_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_header_1.setObjectName(_fromUtf8("lb_header_1"))
        self.lb_estoque = QtGui.QLabel(self.ct_estoque)
        self.lb_estoque.setGeometry(QtCore.QRect(25, 60, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_estoque.setFont(font)
        self.lb_estoque.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_estoque.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_estoque.setObjectName(_fromUtf8("lb_estoque"))
        self.tx_cod_produto = QtGui.QLineEdit(self.ct_estoque)
        self.tx_cod_produto.setGeometry(QtCore.QRect(105, 60, 60, 25))
        self.tx_cod_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_cod_produto.setObjectName(_fromUtf8("tx_cod_produto"))
        self.lb_estoque_2 = QtGui.QLabel(self.ct_estoque)
        self.lb_estoque_2.setGeometry(QtCore.QRect(25, 95, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_estoque_2.setFont(font)
        self.lb_estoque_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_estoque_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_estoque_2.setObjectName(_fromUtf8("lb_estoque_2"))
        self.tx_produto = QtGui.QLineEdit(self.ct_estoque)
        self.tx_produto.setGeometry(QtCore.QRect(105, 95, 370, 25))
        self.tx_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_produto.setObjectName(_fromUtf8("tx_produto"))
        self.lb_estoque_4 = QtGui.QLabel(self.ct_estoque)
        self.lb_estoque_4.setGeometry(QtCore.QRect(25, 130, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_estoque_4.setFont(font)
        self.lb_estoque_4.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_estoque_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_estoque_4.setObjectName(_fromUtf8("lb_estoque_4"))
        self.tx_fornecedor_estoque = QtGui.QComboBox(self.ct_estoque)
        self.tx_fornecedor_estoque.setGeometry(QtCore.QRect(105, 130, 370, 25))
        self.tx_fornecedor_estoque.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_fornecedor_estoque.setEditable(True)
        self.tx_fornecedor_estoque.setObjectName(_fromUtf8("tx_fornecedor_estoque"))
        self.lb_estoque_5 = QtGui.QLabel(self.ct_estoque)
        self.lb_estoque_5.setGeometry(QtCore.QRect(25, 165, 130, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_estoque_5.setFont(font)
        self.lb_estoque_5.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_estoque_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_estoque_5.setObjectName(_fromUtf8("lb_estoque_5"))
        self.tx_quantidade = QtGui.QLineEdit(self.ct_estoque)
        self.tx_quantidade.setGeometry(QtCore.QRect(160, 165, 90, 25))
        self.tx_quantidade.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_quantidade.setObjectName(_fromUtf8("tx_quantidade"))
        self.lb_estoque_6 = QtGui.QLabel(self.ct_estoque)
        self.lb_estoque_6.setGeometry(QtCore.QRect(255, 165, 125, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_estoque_6.setFont(font)
        self.lb_estoque_6.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_estoque_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_estoque_6.setObjectName(_fromUtf8("lb_estoque_6"))
        self.tx_quantidade_min = QtGui.QLineEdit(self.ct_estoque)
        self.tx_quantidade_min.setGeometry(QtCore.QRect(385, 165, 90, 25))
        self.tx_quantidade_min.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_quantidade_min.setObjectName(_fromUtf8("tx_quantidade_min"))
        self.lb_estoque_7 = QtGui.QLabel(self.ct_estoque)
        self.lb_estoque_7.setGeometry(QtCore.QRect(25, 200, 130, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_estoque_7.setFont(font)
        self.lb_estoque_7.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_estoque_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_estoque_7.setObjectName(_fromUtf8("lb_estoque_7"))
        self.tx_preco_de_compra = QtGui.QLineEdit(self.ct_estoque)
        self.tx_preco_de_compra.setGeometry(QtCore.QRect(160, 200, 90, 25))
        self.tx_preco_de_compra.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_preco_de_compra.setObjectName(_fromUtf8("tx_preco_de_compra"))
        self.lb_estoque_8 = QtGui.QLabel(self.ct_estoque)
        self.lb_estoque_8.setGeometry(QtCore.QRect(255, 200, 125, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_estoque_8.setFont(font)
        self.lb_estoque_8.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_estoque_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_estoque_8.setObjectName(_fromUtf8("lb_estoque_8"))
        self.tx_preco_de_venda = QtGui.QLineEdit(self.ct_estoque)
        self.tx_preco_de_venda.setGeometry(QtCore.QRect(385, 200, 90, 25))
        self.tx_preco_de_venda.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_preco_de_venda.setObjectName(_fromUtf8("tx_preco_de_venda"))
        self.lb_estoque_9 = QtGui.QLabel(self.ct_estoque)
        self.lb_estoque_9.setGeometry(QtCore.QRect(25, 235, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lb_estoque_9.setFont(font)
        self.lb_estoque_9.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_estoque_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_estoque_9.setObjectName(_fromUtf8("lb_estoque_9"))
        self.tx_obs_estoque = QtGui.QPlainTextEdit(self.ct_estoque)
        self.tx_obs_estoque.setGeometry(QtCore.QRect(105, 235, 370, 75))
        self.tx_obs_estoque.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_obs_estoque.setObjectName(_fromUtf8("tx_obs_estoque"))
        self.bt_cad_produto = QtGui.QPushButton(self.ct_estoque)
        self.bt_cad_produto.setGeometry(QtCore.QRect(25, 370, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cad_produto.setFont(font)
        self.bt_cad_produto.setObjectName(_fromUtf8("bt_cad_produto"))
        self.bt_cancelar = QtGui.QPushButton(self.ct_estoque)
        self.bt_cancelar.setGeometry(QtCore.QRect(125, 370, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cancelar.setFont(font)
        self.bt_cancelar.setObjectName(_fromUtf8("bt_cancelar"))
        self.ct_estoque2 = QtGui.QFrame(self.ct_frame_estoque)
        self.ct_estoque2.setGeometry(QtCore.QRect(570, 20, 300, 423))
        self.ct_estoque2.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 2px solid #fff;\n"
"border-radius: 20px;"))
        self.ct_estoque2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_estoque2.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_estoque2.setObjectName(_fromUtf8("ct_estoque2"))
        self.lb_header_2 = QtGui.QLabel(self.ct_estoque2)
        self.lb_header_2.setGeometry(QtCore.QRect(75, 10, 150, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.lb_header_2.setFont(font)
        self.lb_header_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_header_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_header_2.setObjectName(_fromUtf8("lb_header_2"))
        self.tabela_estoque = QtGui.QTableWidget(self.ct_estoque2)
        self.tabela_estoque.setGeometry(QtCore.QRect(5, 60, 290, 250))
        self.tabela_estoque.setStyleSheet(_fromUtf8("background: #FFF; border: none; border-radius: 0"))
        self.tabela_estoque.setAutoScroll(True)
        self.tabela_estoque.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabela_estoque.setTextElideMode(QtCore.Qt.ElideRight)
        self.tabela_estoque.setObjectName(_fromUtf8("tabela_estoque"))
        self.tabela_estoque.setColumnCount(3)
        self.tabela_estoque.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabela_estoque.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_estoque.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_estoque.setHorizontalHeaderItem(2, item)
        self.tabela_estoque.verticalHeader().setVisible(False)
        self.tx_buscar_produto = QtGui.QLineEdit(self.ct_estoque2)
        self.tx_buscar_produto.setGeometry(QtCore.QRect(50, 370, 200, 30))
        self.tx_buscar_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_buscar_produto.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_buscar_produto.setObjectName(_fromUtf8("tx_buscar_produto"))
        self.label = QtGui.QLabel(self.ct_estoque2)
        self.label.setGeometry(QtCore.QRect(100, 340, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF url(\'/Files/Python/AeR/Images/buscar.png\') no-repeat  right ;\n"
"color: #000;\n"
""))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.tradEstoque(FrameEstoque)
        QtCore.QMetaObject.connectSlotsByName(FrameEstoque)

    def tradEstoque(self, FrameEstoque):
        FrameEstoque.setWindowTitle(_translate("FrameEstoque", "Frame", None))
        self.lb_header_1.setText(_translate("FrameEstoque", "Cadastro / Editor produto", None))
        self.lb_estoque.setText(_translate("FrameEstoque", "Código", None))
        self.lb_estoque_2.setText(_translate("FrameEstoque", "Produto", None))
        self.lb_estoque_4.setText(_translate("FrameEstoque", "Fornecedor", None))
        self.lb_estoque_5.setText(_translate("FrameEstoque", "Qtde. Disponível", None))
        self.lb_estoque_6.setText(_translate("FrameEstoque", "Qtde. Minima", None))
        self.lb_estoque_7.setText(_translate("FrameEstoque", "Preço de Compra", None))
        self.lb_estoque_8.setText(_translate("FrameEstoque", "Preço de Venda", None))
        self.lb_estoque_9.setText(_translate("FrameEstoque", "Obs.", None))
        self.bt_cad_produto.setText(_translate("FrameEstoque", "Cadastrar", None))
        self.bt_cancelar.setText(_translate("FrameEstoque", "Cancelar", None))
        self.lb_header_2.setText(_translate("FrameEstoque", "Todos os produtos", None))
        item = self.tabela_estoque.horizontalHeaderItem(0)
        item.setText(_translate("FrameEstoque", "Cod:", None))
        item = self.tabela_estoque.horizontalHeaderItem(1)
        item.setText(_translate("FrameEstoque", "Descrição", None))
        item = self.tabela_estoque.horizontalHeaderItem(2)
        item.setText(_translate("FrameEstoque", "QTDE", None))
        self.tx_buscar_produto.setPlaceholderText(_translate("FrameEstoque", "Buscar", None))
        self.label.setText(_translate("FrameEstoque", "Pesquisar", None))

