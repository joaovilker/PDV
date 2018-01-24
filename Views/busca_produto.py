# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'busca_produto.ui'
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

class Ui_DialogBuscarProduto(object):
    def setBuscarProduto(self, DialogBuscarProduto):
        DialogBuscarProduto.setObjectName(_fromUtf8("DialogBuscarProduto"))
        DialogBuscarProduto.resize(400, 350)
        self.frame = QtGui.QFrame(DialogBuscarProduto)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 350))
        self.frame.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 380, 330))
        self.frame_2.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 5px solid #fFf;\n"
"border-radius: 20px;\n"
""))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.lb_titulo_modal = QtGui.QLabel(self.frame_2)
        self.lb_titulo_modal.setGeometry(QtCore.QRect(90, 20, 200, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.lb_titulo_modal.setFont(font)
        self.lb_titulo_modal.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_titulo_modal.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_titulo_modal.setObjectName(_fromUtf8("lb_titulo_modal"))
        self.lb_info = QtGui.QLabel(self.frame_2)
        self.lb_info.setGeometry(QtCore.QRect(20, 70, 80, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lb_info.setFont(font)
        self.lb_info.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_info.setObjectName(_fromUtf8("lb_info"))
        self.tx_busca_produto = QtGui.QLineEdit(self.frame_2)
        self.tx_busca_produto.setGeometry(QtCore.QRect(110, 70, 250, 25))
        self.tx_busca_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_busca_produto.setObjectName(_fromUtf8("tx_busca_produto"))
        self.table_busca_produto = QtGui.QTableWidget(self.frame_2)
        self.table_busca_produto.setGeometry(QtCore.QRect(20, 110, 340, 192))
        self.table_busca_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solide #FFF;\n"
"background: #FFF;\n"
"color: #000"))
        self.table_busca_produto.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_busca_produto.setObjectName(_fromUtf8("table_busca_produto"))
        self.table_busca_produto.setColumnCount(3)
        self.table_busca_produto.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_busca_produto.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_busca_produto.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_busca_produto.setHorizontalHeaderItem(2, item)
        self.table_busca_produto.verticalHeader().setVisible(False)

        self.tradBuscarProduto(DialogBuscarProduto)
        QtCore.QMetaObject.connectSlotsByName(DialogBuscarProduto)

    def tradBuscarProduto(self, DialogBuscarProduto):
        DialogBuscarProduto.setWindowTitle(_translate("DialogBuscarProduto", "Buscar Produto", None))
        self.lb_titulo_modal.setText(_translate("DialogBuscarProduto", "Buscar Produto", None))
        self.lb_info.setText(_translate("DialogBuscarProduto", "Produto", None))
        item = self.table_busca_produto.horizontalHeaderItem(0)
        item.setText(_translate("DialogBuscarProduto", "Cod.", None))
        item = self.table_busca_produto.horizontalHeaderItem(1)
        item.setText(_translate("DialogBuscarProduto", "Produto", None))
        item = self.table_busca_produto.horizontalHeaderItem(2)
        item.setText(_translate("DialogBuscarProduto", "Qtde.", None))

