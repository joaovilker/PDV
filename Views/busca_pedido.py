# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'busca_pedido.ui'
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

class Ui_BuscaPedido(object):
    def setBuscaPedido(self, BuscaPedido):
        BuscaPedido.setObjectName(_fromUtf8("BuscaPedido"))
        BuscaPedido.resize(800, 600)
        BuscaPedido.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.frame = QtGui.QFrame(BuscaPedido)
        self.frame.setGeometry(QtCore.QRect(20, 20, 760, 560))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.frame.setFont(font)
        self.frame.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 5px solid #fFf;\n"
"border-radius: 20px;\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 30, 80, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(190, 30, 300, 25))
        self.lineEdit.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(500, 30, 90, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tableWidget = QtGui.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(50, 110, 660, 400))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(_fromUtf8("background: #FFF; border: none; border-radius: 0"))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.verticalHeader().setVisible(False)

        self.retranslateUi(BuscaPedido)
        QtCore.QMetaObject.connectSlotsByName(BuscaPedido)

    def retranslateUi(self, BuscaPedido):
        BuscaPedido.setWindowTitle(_translate("BuscaPedido", "Buscar Pedido", None))
        self.label.setText(_translate("BuscaPedido", "Buscar:", None))
        self.pushButton.setText(_translate("BuscaPedido", "OK", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("BuscaPedido", "Cod", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("BuscaPedido", "Cliente", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("BuscaPedido", "Status", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("BuscaPedido", "Data Entrega", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("BuscaPedido", "Entrada", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("BuscaPedido", "Saldo Devedor", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("BuscaPedido", "Total", None))

